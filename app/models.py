from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app import app

db = SQLAlchemy(app)


class TestTable(db.Model):
    __tablename__ = 'test'

    id = Column(UUID, primary_key=True)
    message = Column(Text)
    create_time = Column(DateTime(timezone=True))

    def __init__(self, message, create_time):
        self.message = message
        self.create_time = create_time

    def __repr__(self):
        return {
            "id": self.id,
            "message": self.message,
            "create_time": self.create_time
        }


def db_create():
    db.create_all()


def db_drop():
    db.drop_all()
