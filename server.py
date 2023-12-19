from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import asyncio
import time
import random

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
)

emojis = ['✋', '🤗', '😼', '👎', '💩', '🧠']

@app.get("/emoji")
async def example_endpoint():
    print('emoji')
    time.sleep(3)
    return {"emoji": emojis[random.randint(0, len(emojis)-1)]}

@app.get("/async_emoji")
async def example_endpoint():
    print('async emoji')
    await asyncio.sleep(3)
    return {"emoji": emojis[random.randint(0, len(emojis)-1)]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8100)
