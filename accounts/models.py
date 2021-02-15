from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse




from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name          = models.CharField(max_length=30,verbose_name=_("first name"))
    last_name           = models.CharField(max_length=30,verbose_name=_("last name"))
    email               = models.EmailField(max_length=60 , verbose_name=_('email address'),unique=True)
    mobile              = models.CharField(max_length=30,verbose_name=_("phone number"),unique=True)
    date_joined         = models.DateTimeField(auto_now_add=True, verbose_name=_("date joined"))
    last_login          = models.DateTimeField(auto_now=True, verbose_name=_("last login"))

    is_active           = models.BooleanField(default=True , verbose_name=_("is active"))
    is_admin            = models.BooleanField(default=False , verbose_name=_("is admin"))
    is_superuser        = models.BooleanField(default=False , verbose_name=_("is superuser"))
    is_staff            = models.BooleanField(default=False , verbose_name=_("is staff"))
    
    USERNAME_FIELD      = "email"
    REQUIRED_FIELDS     = ["first_name","last_name","mobile"]

    objects             = CustomUserManager()

    class Meta : 
        verbose_name        = "User"
        verbose_name_plural = "Users"
    
    def __str__(self):
        return self.first_name
    
    def get_fullname(self) : 
        return str(f'{self.first_name} {self.last_name}')




def image_filepath(self,filename) : 
    _,ext = filename.split('.')
    path  = f"users/{self.pk}/images/profile_image.{ext}"
    return path 
def image_default() : 
    return "/users/default_image.png"

class Profile(models.Model) : 
    GENDER_CHOICES = (
        ("male","male"),
        ("female","female"),
        ("unknown","unknown"),
    )
    user                = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    username            = models.CharField(max_length = 10 , unique = True , null=True , blank= True , verbose_name=_('username'))
    date_of_birth       = models.DateField(null=True,blank=True,verbose_name=_('date of birth'))
    gender              = models.CharField(max_length=10 ,choices=GENDER_CHOICES,default=3,verbose_name=_('gender'))
    image               = models.ImageField(upload_to=image_filepath,default=image_default,blank=True,null=True,verbose_name=_('profile image'))
    slug                = models.SlugField(max_length=50 ,unique=True,verbose_name = _("slug"),allow_unicode=True)

    
    def __str__(self):
        return self.user.first_name
    def get_absolute_url(self):
        return reverse("profile-detail", kwargs={"slug":self.slug})
        #print(self.user)
    def get_update_url(self) : 
        return reverse("profile-update",kwargs={"slug":self.slug})
    def save(self, *args, **kwargs):
        slug = slugify(self.user,allow_unicode = True) 
        slug = slug + str(self.pk)
        if self.image is None  : 
            self.image = image_default()

        self.slug = slug 
         
        super(Profile, self).save(*args, **kwargs)
   
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()