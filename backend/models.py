from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"


    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    gender = Column(String)

    date_of_birth = Column(String)
    time_of_birth = Column(String)
    place_of_birth = Column(String)

    questions = Column(String)

