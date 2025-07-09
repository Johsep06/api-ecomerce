from sqlalchemy import create_engine #, #Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base #, relationship

db = create_engine("sqlite:///banco.db")

Base = declarative_base()