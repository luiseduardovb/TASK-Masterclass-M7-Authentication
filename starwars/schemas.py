import graphene





from ships.mutations import ShipMutations
from ships.queries import ShipQueries
from users.queries import UserQuery
from users.mutations import UserMutation





class Query(UserQuery, ShipQueries, graphene.ObjectType):
    pass


class Mutation(UserMutation, ShipMutations, graphene.ObjectType):
    pass


SCHEMA = graphene.Schema(query=Query, mutation=Mutation)
