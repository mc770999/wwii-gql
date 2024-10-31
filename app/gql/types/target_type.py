from graphene import ObjectType, Int, String, Field
from app.db.repository import missions_repository as mission_repo
from app.db.repository import city_repository as city_repo
from app.db.repository import target_type_repository as target_type_repo

class TargetType(ObjectType):
    target_id = Int()
    mission_id = Int()
    city_id = Int()
    target_industry = String()
    target_priority = Int()
    target_type_id = Int()

    mission = Field("app.gql.types.mission_type.MissionType")
    city = Field("app.gql.types.city_type.CityType")
    target_type = Field("app.gql.types.target_type_type.TargetTypeType")


    @staticmethod
    def resolve_mission(root, info):
        return mission_repo.get_mission_by_id(root.mission_id)

    @staticmethod
    def resolve_city(root, info):
        return city_repo.get_city_by_id(root.city_id)

    @staticmethod
    def resolve_target_type(root, info):
        return target_type_repo.get_target_type_by_id(root.target_type_id)