from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class City(Base):
    __tablename__ = "cities"
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String)
    country_id =  Column(Integer, ForeignKey("countries.country_id"))
    latitude = Column(Float)
    longitude = Column(Float)

    target = relationship("Target", back_populates="city")
    country = relationship("Country", back_populates="city")
    #vacations = relationship("StudentVacation", back_populates="country")



