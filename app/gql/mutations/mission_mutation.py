from graphene import Mutation, Int, Field, Boolean, Date, Float, ObjectType, InputObjectType
from app.db.models import Mission
from app.gql.types.mission_type import MissionType
from app.db.repository.missions_repository import add_mission, update_mission_result, delete_mission


class AddMission(Mutation):
    class Arguments:
        mission_id = Int()
        mission_date = Date(required=True)
        airborne_aircraft = Float(required=True)
        attacking_aircraft = Float(required=True)
        bombing_aircraft = Float(required=True)

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_date, airborne_aircraft, attacking_aircraft, bombing_aircraft):
        mission_to_insert = Mission(mission_date=mission_date, airborne_aircraft=airborne_aircraft, attacking_aircraft=attacking_aircraft,
                          bombing_aircraft=bombing_aircraft)
        add_mission(mission_to_insert)
        return AddMission(mission=mission_to_insert)


class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int()

    success = Field(Boolean)

    @staticmethod
    def mutate(root, info, mission_id):
        delete_mission(mission_id)
        return DeleteMission(success=True)


class InputMission(InputObjectType):

    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()


class UpdateMission(Mutation):
    class Arguments:
        input = InputMission(required=True)
        mission_id = Int()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, input, mission_id):
        mission_updated = (update_mission_result(mission_id, input))
        return UpdateMission(mission=mission_updated)


