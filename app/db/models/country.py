from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Country(Base):
    __tablename__ = "countries"
    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String)


    city = relationship("City", back_populates="country")
