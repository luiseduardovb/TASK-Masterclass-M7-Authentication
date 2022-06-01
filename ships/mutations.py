from typing import TYPE_CHECKING, Any, cast

import graphene
from django.contrib.auth import get_user_model

from ships import models, types


if TYPE_CHECKING:
    from django.contrib.auth.models import AbstractUser

User = get_user_model()


def get_user_from_context(info: graphene.ResolveInfo) -> "AbstractUser":
    return cast("AbstractUser", User.objects.first())


class CreateSpaceShip(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    space_ship = graphene.Field(types.SpaceShipType)

    def mutate(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> "CreateSpaceShip":
        user = get_user_from_context(info)
        space_ship = models.SpaceShip.objects.create(**kwargs, creator=user)
        return CreateSpaceShip(space_ship=space_ship)


class UpdateSpaceShip(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    space_ship = graphene.Field(types.SpaceShipType)

    def mutate(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> "UpdateSpaceShip":
        pass


class DeleteSpaceShip(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    status = graphene.Field(graphene.Boolean)

    def mutate(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> "DeleteSpaceShip":
        pass


class ShipMutations(graphene.ObjectType):
    create_space_ship = CreateSpaceShip.Field()
    update_space_ship = UpdateSpaceShip.Field()
    delete_space_ship = DeleteSpaceShip.Field()
