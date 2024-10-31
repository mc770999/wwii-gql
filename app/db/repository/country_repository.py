from app.db.database import session_maker
from app.db.models import City, Country


def get_country_by_id(country_id: int):
    with session_maker() as session:
        return session.query(Country).filter(Country.country_id == country_id).all()



def get_cities_by_country_id(country_id: int):
    with session_maker() as session:
        return session.query(City).filter(City.country_id == country_id).all()