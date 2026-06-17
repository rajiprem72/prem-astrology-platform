from backend.database import engine
from backend.models import Base

Base.metadata.create_all(bind=engine)
print("Database tables created")

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
title="Prem Astrology Platform",
version="1.0.0"
)

class CustomerOrder(BaseModel):
    name: str
    gender: str
    date_of_birth: str
    time_of_birth: str
    place_of_birth: str
    questions: str

@app.get("/")
def home():
    return {
"message": "Prem Astrology Platform is running"
}

@app.post("/submit-order")
def submit_order(order: CustomerOrder):
    return {
"status": "success",
"customer": order.name,
"message": "Order received successfully"
}
