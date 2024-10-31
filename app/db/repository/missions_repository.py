from datetime import datetime, timedelta

from sqlalchemy.orm import joinedload
from sqlalchemy.testing.config import options
from app.db.models import Mission, Target, City, Country, TargetType  # Import the models
from sqlalchemy.orm import joinedload


from app.db.database import session_maker
from app.db.models import Mission, Target, City


def get_all_missions():
    with session_maker() as session:
        return session.query(Mission).all()


def get_mission_by_id(mission_id: int):
    with session_maker() as session:
        return (
            session.query(Mission)
            .filter(Mission.mission_id == mission_id)
            .first()
        )

def get_mission_by_target_type_name(target_type_name):
    with session_maker() as session:
        return (
            session.query(Mission)
            .join(Target, Target.mission_id == Mission.mission_id)
            .join(TargetType, TargetType.target_type_id == Target.target_type_id)
            .filter(TargetType.target_type_name == target_type_name)
            .all()
        )

def get_attack_results_by_type(attack_type_name):
    with session_maker() as session:
        results = (
            session.query(Mission)
            .join(Mission.target)
            .join(Target.target_type)
            .options(
                joinedload(Mission.target)
                .joinedload(Target.target_type)
            )
            .filter(TargetType.target_type_name == attack_type_name)
            .all()
        )
        return results

def get_missions_by_date_range(mission_date_start, mission_date_end):
    with session_maker() as session:
        return session.query(Mission).filter(
            Mission.mission_date >= mission_date_start,
            Mission.mission_date < mission_date_end).all()

def get_mission_country_take_part(country_name):
    with session_maker() as session:
        all_missions = (
            session.query(Mission)
            .join(Target)
            .join(City)
            .join(Country)
            .filter(Country.country_name == country_name)
            .all()
        )
        return all_missions


def get_mission_by_target_industry(target_type_name):
    with session_maker() as session:
        all_missions = (
            session.query(Mission)
            .join(Target, Target.mission_id == Mission.mission_id)
            .join(TargetType, TargetType.target_type_id == Target.target_type_id)
            .filter(TargetType.target_type_name == target_type_name)
            .all()
        )
        return all_missions

def get_targets_by_mission_id(mission_id: int):
    with session_maker() as session:
        return session.query(Target).filter(Target.mission_id == mission_id).all()



