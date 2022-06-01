import graphene_django

from ships import models


class SpaceShipType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.SpaceShip
