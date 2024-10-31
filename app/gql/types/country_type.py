from graphene import ObjectType, Int, String, List
from app.db.repository import country_repository

import app.gql.types.city_type


class CountryType(ObjectType):
    country_id = Int()
    country_name = String()
    cities = List("app.gql.types.city_type.CityType")

    @staticmethod
    def resolve_cities(root, info):
        return country_repository.get_cities_by_country_id(root.country_id)