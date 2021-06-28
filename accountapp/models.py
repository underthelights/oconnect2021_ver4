from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email=None, password=None):
        if not username:
            raise ValueError('must have user username!')
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        superuser = self.create_user(
            username=username,
            email=email,
            password=password
        )
        superuser.is_admin = True
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save()
        return superuser