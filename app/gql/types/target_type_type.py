from graphene import ObjectType, Int, String, List, Field
from app.db.repository import target_type_repository as target_type_repo
from app.db.repository import target_repository as target_repo  # Import your target repository

class TargetTypeType(ObjectType):
    target_type_id = Int()
    target_type_name = String()

    targets = List("app.gql.types.target_type.TargetType")  # Adjust import according to your project structure

    @staticmethod
    def resolve_targets(root, info):
        return target_repo.get_targets_by_type_id(root.target_type_id)


