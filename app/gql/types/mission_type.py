from dataclasses import Field

from graphene import ObjectType, Int, Float, Date, List

import app.gql.types.target_type
from app.db.repository import missions_repository
from app.db.repository.target_repository import get_target_mission_by_id


class MissionType(ObjectType):
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()

    targets = List('app.gql.types.target_type.TargetType')

    @staticmethod
    def resolve_targets(root, info):
        return missions_repository.get_targets_by_mission_id(root.mission_id)