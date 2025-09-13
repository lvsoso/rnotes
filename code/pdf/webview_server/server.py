#!/usr/bin/env python3
"""Simple PDF file server with HTTP Range support.

Features:
- GET /list -> JSON list of available PDF filenames (in configured directory)
- GET /pdf/<filename> -> Serves PDF with Accept-Ranges and partial content (Range header)

Environment variables:
- PDF_DIR: Directory to search for PDF files (default: parent folder of this script)
- HOST: Bind host (default 127.0.0.1)
- PORT: Bind port (default 8765)

Range semantics supported:
- Single range: bytes=START-  , bytes=START-END, bytes=-SUFFIX
- Responds 206 Partial Content with Content-Range
- Reject multiple ranges (returns 501)
- Validates bounds (416 on invalid range)

CORS:
- Adds Access-Control-Allow-Origin: * for simplicity

This server has no external dependencies (pure stdlib).
"""
from __future__ import annotations
import json
import os
import posixpath
import re
import sys
import urllib.parse
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Optional, Tuple

PDF_DIR = os.environ.get("PDF_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", "8000"))

RANGE_RE = re.compile(r"bytes=([^,\"]+)")  # simple single-range extractor

def list_pdfs(directory: str):
    try:
        return [f for f in os.listdir(directory) if f.lower().endswith('.pdf') and os.path.isfile(os.path.join(directory, f))]
    except FileNotFoundError:
        return []

class PDFHandler(BaseHTTPRequestHandler):
    server_version = "PDFRangeHTTP/0.1"

    def _set_cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Range, Content-Type")
        self.send_header("Access-Control-Expose-Headers", "Accept-Ranges, Content-Range, Content-Length")

    def do_OPTIONS(self):  # CORS preflight
        self.send_response(HTTPStatus.NO_CONTENT)
        self._set_cors()
        self.send_header("Allow", "GET, HEAD, OPTIONS")
        self.end_headers()

    def do_HEAD(self):
        # Handle HEAD requests the same as GET but without body
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        if path == '/api/list':
            files = list_pdfs(PDF_DIR)
            data = json.dumps(files, ensure_ascii=False)
            encoded = data.encode('utf-8')
            self.send_response(HTTPStatus.OK)
            self._set_cors()
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(encoded)))
            self.end_headers()
            return
        if path.startswith('/api/pdf/'):
            name = path[len('/api/pdf/') :]
            return self.handle_pdf_head(name)
        self.send_response(HTTPStatus.NOT_FOUND)
        self._set_cors()
        self.end_headers()

    def handle_pdf_head(self, raw_name: str):
        # prevent path traversal
        decoded = urllib.parse.unquote(raw_name)
        safe = posixpath.normpath(decoded).lstrip('/')
        if safe.startswith('..'):
            self.send_response(HTTPStatus.FORBIDDEN)
            self._set_cors()
            self.end_headers()
            return
        file_path = os.path.join(PDF_DIR, safe)
        if not (os.path.isfile(file_path) and file_path.lower().endswith('.pdf')):
            self.send_response(HTTPStatus.NOT_FOUND)
            self._set_cors()
            self.end_headers()
            return
        
        file_size = os.path.getsize(file_path)
        self.send_response(HTTPStatus.OK)
        self._set_cors()
        self.send_header('Content-Type', 'application/pdf')
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Length', str(file_size))
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        if path == '/api/list':
            return self.handle_list()
        if path.startswith('/api/pdf/'):
            name = path[len('/api/pdf/') :]
            return self.handle_pdf(name)
        self.respond_text(HTTPStatus.NOT_FOUND, "Not Found")

    def handle_list(self):
        files = list_pdfs(PDF_DIR)
        data = json.dumps(files, ensure_ascii=False)
        encoded = data.encode('utf-8')
        self.send_response(HTTPStatus.OK)
        self._set_cors()
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def handle_pdf(self, raw_name: str):
        # prevent path traversal
        decoded = urllib.parse.unquote(raw_name)
        safe = posixpath.normpath(decoded).lstrip('/')
        if safe.startswith('..'):
            self.respond_text(HTTPStatus.FORBIDDEN, 'Forbidden')
            return
        file_path = os.path.join(PDF_DIR, safe)
        if not (os.path.isfile(file_path) and file_path.lower().endswith('.pdf')):
            self.respond_text(HTTPStatus.NOT_FOUND, 'File Not Found')
            return
        file_size = os.path.getsize(file_path)

        range_header = self.headers.get('Range')
        if range_header:
            # Reject multiple ranges
            if ',' in range_header:
                self.respond_text(HTTPStatus.NOT_IMPLEMENTED, 'Multiple ranges not supported')
                return
            ok, byte_range = self.parse_range(range_header, file_size)
            if not ok:
                self.send_response(HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE)
                self._set_cors()
                self.send_header('Content-Range', f'bytes */{file_size}')
                self.end_headers()
                return
            start, end = byte_range
            length = end - start + 1
            self.send_response(HTTPStatus.PARTIAL_CONTENT)
            self._set_cors()
            self.send_header('Content-Type', 'application/pdf')
            self.send_header('Accept-Ranges', 'bytes')
            self.send_header('Content-Range', f'bytes {start}-{end}/{file_size}')
            self.send_header('Content-Length', str(length))
            self.end_headers()
            with open(file_path, 'rb') as f:
                f.seek(start)
                remaining = length
                bufsize = 64 * 1024
                while remaining > 0:
                    chunk = f.read(min(bufsize, remaining))
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    remaining -= len(chunk)
            return
        # full content
        self.send_response(HTTPStatus.OK)
        self._set_cors()
        self.send_header('Content-Type', 'application/pdf')
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Length', str(file_size))
        self.end_headers()
        with open(file_path, 'rb') as f:
            bufsize = 64 * 1024
            while True:
                chunk = f.read(bufsize)
                if not chunk:
                    break
                self.wfile.write(chunk)

    def parse_range(self, header: str, file_size: int) -> Tuple[bool, Optional[Tuple[int, int]]]:
        # header like: bytes=START-END | bytes=START- | bytes=-SUFFIX
        m = RANGE_RE.match(header.strip())
        if not m:
            return False, None
        spec = m.group(1).strip()
        if '-' not in spec:
            return False, None
        start_s, end_s = spec.split('-', 1)
        if start_s == '':  # suffix range
            try:
                length = int(end_s)
            except ValueError:
                return False, None
            if length <= 0:
                return False, None
            if length > file_size:
                length = file_size
            start = file_size - length
            end = file_size - 1
            return True, (start, end)
        try:
            start = int(start_s)
        except ValueError:
            return False, None
        if end_s == '':
            end = file_size - 1
        else:
            try:
                end = int(end_s)
            except ValueError:
                return False, None
        if start < 0 or end < start or start >= file_size:
            return False, None
        if end >= file_size:
            end = file_size - 1
        return True, (start, end)

    def log_message(self, fmt, *args):  # quieter concise log
        sys.stderr.write("[%s] %s\n" % (self.log_date_time_string(), fmt % args))

    def respond_text(self, status: HTTPStatus, text: str):
        data = text.encode('utf-8')
        self.send_response(status)
        self._set_cors()
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

def run():
    addr = (HOST, PORT)
    httpd = ThreadingHTTPServer(addr, PDFHandler)
    print(f"Serving PDFs from {PDF_DIR} on http://{HOST}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")

if __name__ == '__main__':
    run()
