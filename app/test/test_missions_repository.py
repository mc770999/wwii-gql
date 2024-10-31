from typing import List

from app.db.models import Mission
from app.db.repository.missions_repository import get_mission_country_take_part


def test_get_missions_by_country():
    missions: List[Mission] = get_mission_country_take_part("ALBANIA")
    for m in missions:
        print(f"{[c.country_name for c in [c.country for c in [t.city for t in m.target]]]}")