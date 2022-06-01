import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Yo!")


class Mutation(graphene.ObjectType):
    pass


SCHEMA = graphene.Schema(query=Query)
