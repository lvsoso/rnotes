# PDF Range Server

纯 Python (标准库) PDF 静态文件服务器，支持 HTTP Range 分块传输，方便前端 pdf.js 或 `<embed>` 渐进式加载。

## 功能
- 列表接口: `GET /list` 返回当前目录下可用 PDF 文件数组（只扫描 `PDF_DIR` 目录根层级）。
- 文件接口: `GET /pdf/<filename>` 支持 `Range: bytes=...` 单段请求，返回 `206 Partial Content` 与 `Content-Range`。
- 返回头包含 `Accept-Ranges: bytes`，方便前端断点续传、滑动定位。
- 简单 CORS: `Access-Control-Allow-Origin: *`。
- 安全: 规范化路径，阻止 `../` 目录穿越；仅允许 `.pdf`。

## 启动
环境变量 (可选):
- `PDF_DIR` 指定 PDF 文件所在目录，默认为 `server.py` 上级目录（你的仓库根）
- `HOST` 默认 `127.0.0.1`
- `PORT` 默认 `8000`

运行：
```bash
python webview_server/server.py
```
输出示例：
```
Serving PDFs from /absolute/path/pdf-load on http://127.0.0.1:8000
```

## 访问示例
```bash
# 列出 pdf
curl http://127.0.0.1:8000/list

# 完整下载
curl -v http://127.0.0.1:8000/pdf/Unix-Linux.pdf -o /tmp/full.pdf

# 取前 500 字节
curl -v -H "Range: bytes=0-499" http://127.0.0.1:8000/pdf/Unix-Linux.pdf -o /tmp/part1

# 取从 500 到文件末尾
curl -v -H "Range: bytes=500-" http://127.0.0.1:8000/pdf/Unix-Linux.pdf -o /tmp/part2

# 取最后 1000 字节
curl -v -H "Range: bytes=-1000" http://127.0.0.1:8000/pdf/Unix-Linux.pdf -o /tmp/tail
```

## Range 行为说明
支持三种单段格式：
- `bytes=START-END`
- `bytes=START-` (到文件末尾)
- `bytes=-SUFFIX_LENGTH` (最后 N 字节)

不支持多段 (逗号分隔)，若发送多段会返回 `501 Not Implemented`。
非法范围返回 `416 Requested Range Not Satisfiable` 并带 `Content-Range: bytes */<file_size>`。

## 与前端配合
前端通过 fetch / XHR 加 `Range` 头即可渐进式加载。示例：
```js
async function fetchChunk(name, start, end){
  const r = await fetch(`http://127.0.0.1:8000/pdf/${encodeURIComponent(name)}`, {
    headers: { Range: `bytes=${start}-${end}` }
  });
  if(!r.ok && r.status !== 206) throw new Error('Bad status '+r.status);
  return await r.arrayBuffer();
}
```

## 后续可扩展
- ETag / If-Range 支持
- Last-Modified / 缓存控制
- 支持多 Range (multipart/byteranges)
- 目录递归或模糊搜索
- 限速 / 并发控制
- 简单鉴权 (token/header)

## License
MIT (可自由修改使用)
