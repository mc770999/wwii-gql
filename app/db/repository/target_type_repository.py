from sqlalchemy.orm import sessionmaker

from app.db.database import session_maker
from app.db.models import TargetType


def get_all_target_types():
    with session_maker() as session:
        return session.query(TargetType).all()


def get_target_type_by_id(target_type_id: int):
    with session_maker() as session:
        return session.query(TargetType).filter(TargetType.target_type_id == target_type_id).first()
