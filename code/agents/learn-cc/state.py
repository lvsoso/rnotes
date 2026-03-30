"""共享状态管理"""
import threading

shutdown_requests = {}
plan_requests = {}
tracker_lock = threading.Lock()
