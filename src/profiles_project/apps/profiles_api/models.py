from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Methods for our custom user model"""

    def create_user(self, email, name, password="None"):
        if not email:
            raise ValueError('Please provide an email address.')
        email = self.normalize_email(email)
        user = self.model(name = name, email = email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new super user"""

        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Repesent a User Profile inside our system"""

    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_super_user = models.BooleanField(default = False)
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Use to get a user's full name"""

        return self.name

    def get_short_name(self):
        """Use to get a user's short name"""

        return self.name

    def __str__(self):
        return self.email