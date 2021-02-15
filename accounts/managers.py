from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self,first_name,last_name,email,mobile,password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not first_name:
            raise ValueError(_('first name must be set'))
        if not last_name:
            raise ValueError(_('last name must be set'))
        if not email:
            raise ValueError(_('The Email must be set'))
        if not mobile:
            raise ValueError(_('The mobile must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name,last_name=last_name,mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,first_name,last_name,email,mobile,password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        if extra_fields.get('is_admin') is not True:
            raise ValueError(_('Superuser must have is_admin=True.'))
        return self.create_user(first_name,last_name,email,mobile,password,**extra_fields)