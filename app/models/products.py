import uuid6
from sqlalchemy import String, Integer, Column

from app.models import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(String(36), 
                primary_key=True,
                default=lambda: str(uuid6.uuid7()),
                nullable=False
                ) 
    name = Column(String, nullable=False)
    stock = Column(Integer, nullable=False)