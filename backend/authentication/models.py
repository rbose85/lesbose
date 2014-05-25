from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db import models

from django.utils import timezone


class UserManager(BaseUserManager):
    """
    Functions to create both standard and privileged auth.User instances.
    """

    def create_user(self, email, password=None, username=None):
        """
        Create a new auth.User instance from the given email and password.
        :param email: A required unique field for the new User instance.
        :param password: Required, or perhaps account verification via email?
        :param username: A unique field for the new User instance.
        :return User: the new instance of auth.User.
        """

        if not email:
            raise ValueError('Email address is required.')

        if not password:
            password = self.make_random_password()

        email = UserManager.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, username=None):
        """
        Create a new privileged User instance with given email and password.
        """

        superuser = self.create_user(username, email, password)

        superuser.is_active = True
        superuser.is_superuser = True
        superuser.save(using=self._db)

        return superuser


class User(AbstractBaseUser):
    """
    Define the constraints and minimum requirements of an auth.User instance.
    """

    username = models.CharField(max_length=30, unique=True, blank=True)
    email = models.EmailField(verbose_name='email address', max_length=255,
                              unique=True, db_index=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.username if self.username is not None else self.email

    def __unicode__(self):
        return self.get_short_name()
