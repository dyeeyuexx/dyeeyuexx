from fastapi import FastAPI, Request
import time
from typing import Optional

app = FastAPI()


@app.post("/process")
async def process_request(timeout: Optional[int] = 5):
    # 获取当前时间
    start_time = time.time()
    while (time.time() - start_time) < timeout:
        pass  # 等待直到达到指定的超时时间
    # 返回响应
    return {
        "message": f"Request processed within {timeout} seconds."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6060)