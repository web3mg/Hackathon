# backend_main.py

from fastapi import FastAPI, Request
from pydantic import BaseModel
from agent_orchestrator import process_ticket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (optional, useful for frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the input model
class TicketInput(BaseModel):
    query: str

@app.post("/process_ticket")
async def process(input_data: TicketInput):
    result = process_ticket(input_data.query)
    return {"status": "success", "data": result}

@app.get("/")
async def root():
    return {"message": "AI-Driven Customer Support API is running."}
