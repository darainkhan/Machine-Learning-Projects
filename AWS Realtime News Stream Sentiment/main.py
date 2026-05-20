from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI application instance
app = FastAPI()

# Define a request body schema using Pydantic
class Message(BaseModel):
    text: str  # Expect a JSON object with a single string field called "text"

# Handle GET requests to the root path "/"
@app.get("/")
def read_root():
    return {"message": "Hello from realtime-sentiment-model!"}

# Handle POST requests to "/echo"
# This endpoint receives a JSON body matching the Message schema
@app.post("/echo")
def echo_message(msg: Message):
    # Return the text that was sent in the request body
    return {"received": msg.text}