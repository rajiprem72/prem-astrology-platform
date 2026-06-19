from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    order_number = Column(String)

    name = Column(String)
    gender = Column(String)

    mobile = Column(String)
    email = Column(String)

    date_of_birth = Column(String)
    time_of_birth = Column(String)
    place_of_birth = Column(String)

    preferred_language = Column(String)

    question1 = Column(String)
    question2 = Column(String)
    question3 = Column(String)

    delivery_method = Column(String)

    order_status = Column(String)