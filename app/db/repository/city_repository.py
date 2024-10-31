from sqlalchemy.orm import sessionmaker

from app.db.database import session_maker
from app.db.models import City

def get_all_cities():
    with session_maker() as session:
        return session.query(City).all()

def get_city_by_id(city_id: int):
    with session_maker() as session:
        return session.query(City).filter(City.city_id == city_id).first()
