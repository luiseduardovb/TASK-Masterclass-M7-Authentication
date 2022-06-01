# Star Wars

Sorry I don't know any star war lines

## Setup

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Masterclass-M7-Authentication).
2. Install the project dependencies using `poetry install`.
3. Run the migrations using `poetry run manage migrate`.

## Authentication

1. Add `django-graphql-auth` and `django-graphql-jwt` using:

   ```bash
   poetry add django-graphql-auth django-graphql-jwt@0.3.0
   ```

2. Follow the steps [here](https://django-graphql-auth.readthedocs.io/en/latest/quickstart/#create-the-custom-user-model) to get `django-graphql-auth` set up.
   - **NOTE** since we made the installations above, any `pip install` step can be ignored
   - Make sure to add a custom user like described in the steps
   - Add a separate app for users and make sure to make migrations and migrate when creating your custom user model
   - Add the User and Me queries
     - The quickstart adds them in `starwars/schemas.py`, but add them in `users/queries.py` and import them instead (separation of concerns)
   - Add the registration mutation
     - The quickstart adds them in `starwars/schemas.py`, but add them in `users/mutations.py` and import them instead (separation of concerns)
3. Test out the login and registration on Altair.

## Permissions

1. We have a mutation in `ships/mutations.py` that creates space ships.
2. Add a `login_required` decorator to all the mutations here [this will help](https://django-graphql-jwt.domake.io/decorators.html#login-required).
3. We have a function called `get_user_from_context` that takes in a `info: ResolveInfo`, and we want to get the logged in user from the `info` object.
   - Right now the function just returns the first user found in the database
   - We want it to return the currently logged in user
4. Test out the create mutation in Altair.
5. Complete the delete mutation:
   - Find the space ship by `popping` the `id` out of `kwargs` and if it does not exist return a `False` status
   - Use the `get_user_from_context` to get the currently logged in user
   - Check if the logged in `user` matches the `creator`
     - Return a `False` status if the users do not match
     - Delete the space ship and return a `True` status if they do match
6. Test out the delete mutation in Altair.

### Permissions Bonus

1. Complete the update mutation:
   - Find the space ship by `popping` the `id` out of `kwargs` and if it does not exist throw a `GraphQLError`
   - Update the space ship by looping through the rest of `kwargs` and `setattr`
   - Save the updates at the end of the loop and return the updated space ship
2. Test out the update mutation in Altair.

### Permissions Bonus 2.0 🌶🌶🌶

1. Change your delete mutation `login_required` decorator to a custom one that checks if the user is logged in AND matches the id of the space ship.
   - This is a completely custom decorator so it cannot use `user_passes_test`.
2. Test out the delete mutation in Altair.

## File Uploads

1. Add `Pillow` to your project by running `poetry add pillow`.
2. Setup media files using [this article](https://testdriven.io/blog/django-static-files/).
3. Add an image field to the `SpaceShip` model.
   - Make it nullable
   - Make the default `None`
4. Make migrations and migrate.
5. Now add `graphene-file-upload` by running `poetry add graphene-file-upload`.
6. Add an `Upload` scalar to the relevant `SpaceShip` mutations.
   - Import it from `from graphene_file_upload.scalars import Upload`
   - Add it to `CreateSpaceShip` arguments
   - Add it to `UpdateSpaceShip` arguments
7. Test out your mutations on Altair.
