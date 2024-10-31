from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Target(Base):
    __tablename__ = "targets"
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_id = Column(Integer, ForeignKey("missions.mission_id")) #forighn_key
    city_id = Column(Integer, ForeignKey("cities.city_id")) #forighn_key
    target_industry = Column(String)
    target_priority = Column(Integer)
    target_type_id = Column(Integer, ForeignKey("targettypes.target_type_id")) #forighn_key


    mission = relationship("Mission", back_populates="target")
    city = relationship("City", back_populates="target")
    target_type = relationship("TargetType", back_populates="target")
