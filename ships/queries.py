from typing import Any

import graphene
import graphene_django
from graphql import GraphQLError

from ships import models, types


class ShipQueries(graphene.ObjectType):
    ship = graphene.Field(types.SpaceShipType, id=graphene.Int())
    ships = graphene_django.DjangoListField(types.SpaceShipType)

    def resolve_ship(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> models.SpaceShip:
        try:
            return models.SpaceShip.objects.get(**kwargs)
        except models.SpaceShip.DoesNotExist as exc:
            raise GraphQLError(str(exc))
