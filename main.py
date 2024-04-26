from package.fastapi import FastAPI
from package.fastapi.responses import StreamingResponse
import openai 
import asyncio

openai.api_key = "OPENAI_API_KEY"
gpt_client = openai.OpenAI(api_key=openai.api_key)

app = FastAPI()


async def streamer():
    response = gpt_client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': "write a 10 line poem."}
        ],
        temperature=0,
        stream=True 
    )

    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content


@app.get("/")
async def index():
    return StreamingResponse(streamer(), media_type="text/html")