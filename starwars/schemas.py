import graphene

from ships.mutations import ShipMutations
from ships.queries import ShipQueries


class Query(ShipQueries, graphene.ObjectType):
    pass


class Mutation(ShipMutations, graphene.ObjectType):
    pass


SCHEMA = graphene.Schema(query=Query, mutation=Mutation)
