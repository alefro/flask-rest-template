from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Text, DateTime, Numeric
from sqlalchemy.dialects.postgresql import UUID

from app import app

db = SQLAlchemy(app)


class TestTable(db.Model):
    __tablename__ = 'test_table'

    id = Column(UUID, primary_key=True)
    title = Column(String(100), nullable=False)
    message = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    price = Column(Numeric(8, 2))

    def __init__(self, title='', message='', created_at=None, updated_at=None, price=0):
        self.title = title
        self.message = message
        self.created_at = created_at
        self.updated_at = updated_at
        self.price = price

    def __repr__(self):
        return {
            "id": self.id,
            "title": self.title,
            "message": self.message,
            "date": self.updated_at,
            "price": self.price
        }
