from datetime import datetime

from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Date, DateTime


class Item(Base):
    __tablename__ = 'bank'
    aadhar = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    bankifsc = Column(String(255), nullable=False, unique=True)
    accountno = Column(Integer)
    status = Column(Integer)

    def __repr__(self):
        return f"<Item name={self.name} udise={self.udise}>"
