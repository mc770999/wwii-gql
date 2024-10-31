from sqlalchemy import func

from app.db.database import session_maker
from app.db.models import Target


def get_all_target_types():
    with session_maker() as session:
        return session.query(Target).all()


def get_target_mission_by_id(mission_id: int):
    with session_maker() as session:
        return session.query(Target).filter(Target.mission_id == mission_id).first()

def get_targets_by_type_id(target_type_id: int):
    with session_maker() as session:
        return session.query(Target).filter(Target.target_type_id == target_type_id).all()


def add_target(target):
    with session_maker() as session:
        id_t = session.query(func.max(Target.target_id)).scalar() + 1
        target.target_id = id_t
        session.add(target)
        session.commit()
        session.refresh(target)
    return target
