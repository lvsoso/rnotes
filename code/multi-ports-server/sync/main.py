import threading
from typing import List

import uvicorn
from fastapi import FastAPI


class SharedState:
    def __init__(self):
        self.value = 0
        self.lock = threading.RLock()

    def get_value(self):
        with self.lock:
            return self.value

    def increase(self):
        with self.lock:
            self.value += 1


class MultiPortServer:
    def __init__(self, ports: List[int]):
        """
        初始化多端口服务器
        :param ports: 端口列表
        """
        self.ports = ports
        self.apps = {port: FastAPI() for port in ports}
        
    def run(self):
        """启动所有端口的服务"""
        def run_server(port: int):
            app = self.apps[port]
            uvicorn.run(app, host="0.0.0.0", port=port)

        threads = []
        for port in self.ports:
            thread = threading.Thread(
                target=run_server,
                args=(port,),
                daemon=True
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
            
    def get_app(self, port: int) -> FastAPI:
        """获取指定端口的FastAPI实例"""
        return self.apps[port]


server = MultiPortServer([8000, 8001, 8002])
shared_count = SharedState()

app1 = server.get_app(8000)
@app1.get("/")
async def root1():
    shared_count.increase()
    return {"message": f"This is port 8000, count {shared_count.get_value()}"}

app2 = server.get_app(8001)
@app2.get("/")
async def root2():
    shared_count.increase()
    return {"message": f"This is port 8002, count {shared_count.get_value()}"}

app2 = server.get_app(8002)
@app2.get("/")
async def root2():
    shared_count.increase()
    return {"message": f"This is port 8002, count {shared_count.get_value()}"}


if __name__ == "__main__":
    server.run()
