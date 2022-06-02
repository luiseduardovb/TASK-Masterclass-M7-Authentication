from typing import TYPE_CHECKING, Any, cast

from graphene_file_upload.scalars import Upload

import graphene
from graphql_jwt.decorators import login_required

from django.contrib.auth import get_user_model

from ships import models, types


if TYPE_CHECKING:
    from django.contrib.auth.models import AbstractUser

User = get_user_model()


def get_user_from_context(info: graphene.ResolveInfo) -> "AbstractUser":
    logged_in_user = info.context.user
    return logged_in_user


class CreateSpaceShip(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        banner = Upload()

    space_ship = graphene.Field(types.SpaceShipType)

    @login_required
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
        banner = Upload()

    space_ship = graphene.Field(types.SpaceShipType)

    @login_required
    def mutate(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> "UpdateSpaceShip":
        pass


class DeleteSpaceShip(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    status = graphene.Field(graphene.Boolean)

    @login_required
    def mutate(
        root, info: graphene.ResolveInfo, **kwargs: Any
    ) -> "DeleteSpaceShip":
        spaceship_id = kwargs.pop("id")
        user = get_user_from_context(info)
        try:
            spaceship_instance = models.SpaceShip.objects.get(pk=spaceship_id)
        except models.SpaceShip.DoesNotExist:
            return DeleteSpaceShip(status=False)

        if spaceship_instance.creator != user:
            return DeleteSpaceShip(status=False)  
        
        
        spaceship_instance.delete()
        return DeleteSpaceShip(status=True)



class ShipMutations(graphene.ObjectType):
    create_space_ship = CreateSpaceShip.Field()
    update_space_ship = UpdateSpaceShip.Field()
    delete_space_ship = DeleteSpaceShip.Field()
