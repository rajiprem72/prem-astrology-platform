from backend.database import engine
from backend.database import SessionLocal

from backend.models import Base
from backend.models import Customer

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

    mobile: str
    email: str

    date_of_birth: str
    time_of_birth: str
    place_of_birth: str

    preferred_language: str

    question1: str
    question2: str
    question3: str

    delivery_method: str

@app.get("/")
def home():
    return {
"message": "Prem Astrology Platform is running"
}

@app.post("/submit-order")
def submit_order(order: CustomerOrder):

    db = SessionLocal()

    customer = Customer(
        order_number="PA000001",

        name=order.name,
        gender=order.gender,

        mobile=order.mobile,
        email=order.email,

        date_of_birth=order.date_of_birth,
        time_of_birth=order.time_of_birth,
        place_of_birth=order.place_of_birth,

        preferred_language=order.preferred_language,

        question1=order.question1,
        question2=order.question2,
        question3=order.question3,

        delivery_method=order.delivery_method,

        order_status="Pending"
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return {
        "status": "success",
        "customer_id": customer.id,
        "customer": customer.name,
        "message": "Order saved successfully"
    }