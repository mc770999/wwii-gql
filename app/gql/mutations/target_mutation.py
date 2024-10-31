from graphene import Mutation, Int, Field, Boolean, Date, Float, ObjectType, InputObjectType, String
from app.gql.types.target_type import TargetType
from app.db.models.target import Target
from app.gql.types.mission_type import MissionType
from app.db.repository.target_repository import add_target

class AddTarget(Mutation):
    class Arguments:
        target_id = Int()
        mission_id = Int()
        city_id = Int()
        target_industry = String()
        target_priority = Int()
        target_type_id = Int()

    target = Field(TargetType)

    @staticmethod
    def mutate(root, info, mission_id, city_id, target_industry, target_priority,target_type_id):
        target_to_insert = Target(
            mission_id=mission_id,
            city_id=city_id,
            target_industry=target_industry,
            target_priority=target_priority,
            target_type_id=target_type_id
        )
        add_target(target_to_insert)
        return AddTarget(target=target_to_insert)
