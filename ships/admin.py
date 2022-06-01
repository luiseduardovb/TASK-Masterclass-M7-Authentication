from django.contrib import admin

from ships import models


to_register = [
    models.SpaceShip,
]

admin.site.register(to_register)
