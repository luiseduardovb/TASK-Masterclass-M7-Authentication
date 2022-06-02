
import graphene

from graphql_auth import mutations


class UserMutation(graphene.ObjectType):
   register = mutations.Register.Field()
   token_auth = mutations.ObtainJSONWebToken.Field()