
from app.db.models import TargetType
from app.db.repository.missions_repository import (
    get_all_missions,
    get_mission_by_id,
    get_mission_by_target_type_name,
    get_attack_results_by_type,
    get_missions_by_date_range,
    get_mission_country_take_part,
    get_mission_by_target_industry
)
from graphene import ObjectType, Int, Float, Date, List, String, Field

from app.gql.types.mission_type import MissionType



class Query(ObjectType):
    all_missions = List(MissionType)
    mission_by_id = Field(MissionType, mission_id=Int(required=True))
    mission_by_target_type_name = List(MissionType, target_type_name=String(required=True))
    missions_by_date_range = List(MissionType, mission_date_start=Date(required=True), mission_date_end=Date(required=True))
    mission_country_take_part = List(MissionType, country_name=String(required=True))
    mission_by_target_industry = List(MissionType, target_type_name=String(required=True))


    @staticmethod
    def resolve_all_missions(root, info):
        return get_all_missions()

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        return get_mission_by_id(mission_id)

    @staticmethod
    def resolve_mission_by_target_type_name(root, info, target_type_name):
        return get_mission_by_target_type_name(target_type_name)


    @staticmethod
    def resolve_missions_by_date_range(root, info, mission_date_start, mission_date_end):
        return get_missions_by_date_range(mission_date_start, mission_date_end)

    @staticmethod
    def resolve_mission_country_take_part(root, info, country_name):
        return get_mission_country_take_part(country_name)

    @staticmethod
    def resolve_mission_by_target_industry(root, info, target_type_name):
        return get_mission_by_target_industry(target_type_name)


