from typing import List
import asyncio

import uvicorn
from fastapi import FastAPI


class AsyncMultiPortServer:
    def __init__(self, ports: List[int]):
        self.ports = ports
        self.apps = {port: FastAPI() for port in ports}
        
    async def run_server(self, port: int):
        """运行单个服务器"""
        config = uvicorn.Config(
            self.apps[port],
            host="0.0.0.0",
            port=port,
            loop="asyncio"
        )
        server = uvicorn.Server(config)
        await server.serve()
        
    async def run(self):
        """同时运行所有服务器"""
        await asyncio.gather(
            *[self.run_server(port) for port in self.ports]
        )
        
    def get_app(self, port: int) -> FastAPI:
        return self.apps[port]


server = AsyncMultiPortServer([8000, 8001, 8002])


app1 = server.get_app(8000)
@app1.get("/")
async def root1():
    return {"message": "This is port 8000"}

app2 = server.get_app(8001)
@app2.get("/")
async def root2():
    return {"message": "This is port 8001"}

app1 = server.get_app(8002)
@app1.get("/")
async def root1():
    return {"message": "This is port 8002"}

if __name__ == "__main__":
    asyncio.run(server.run())