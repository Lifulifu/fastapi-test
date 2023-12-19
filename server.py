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
def emoji():
    print('/emoji start')
    time.sleep(3)
    print('/emoji start')
    return {"emoji": emojis[random.randint(0, len(emojis)-1)]}

@app.get("/async_emoji")
async def async_emoji():
    print('/async_emoji start')
    await asyncio.sleep(3)
    print('/async_emoji end')
    return {"emoji": emojis[random.randint(0, len(emojis)-1)]}


if __name__ == "__main__":
    uvicorn.run('__main__:app', host="0.0.0.0", port=8100, workers=4, reload=True)
