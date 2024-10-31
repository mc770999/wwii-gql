from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema

from app.db.database import init_db
from typing import List
from app.db.models import Mission, City
from app.db.repository.missions_repository import get_mission_country_take_part, get_all_missions, \
    get_mission_by_target_industry, get_mission_by_target_type_name, get_attack_results_by_type
from app.gql.query import Query

app = Flask(__name__)
schema = Schema(query=Query)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

if __name__ == "__main__":

    app.run()
