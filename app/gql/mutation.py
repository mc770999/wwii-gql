from graphene import ObjectType, Field

from app.gql.mutations.mission_mutation import DeleteMission, AddMission, UpdateMission
from app.gql.mutations.target_mutation import AddTarget


class Mutation(ObjectType):
    add_mission = AddMission.Field()
    delete_mission = DeleteMission.Field()
    update_mission = UpdateMission.Field()
    add_target = AddTarget.Field()