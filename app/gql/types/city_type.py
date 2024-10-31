from dataclasses import Field

from graphene import ObjectType, Int, String, List

import app.gql.types.country_type
from app.db.repository import city_repository as city_repo
from app.db.repository import country_repository as country_repo

class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    country_id = Int()

    country = List("app.gql.types.country_type.CountryType")

    @staticmethod
    def resolve_country(root, info):
        return country_repo.get_country_by_id(root.country_id)
