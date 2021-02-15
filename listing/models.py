from django.db import models
from django.utils.text import slugify
import uuid
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.urls import reverse
from .utils import unique_slug_generator

# Create your models here.
class State(models.Model) :
    name = models.CharField(max_length=50  ,verbose_name=_('name'))
    state_number = models.IntegerField() # registration number
    slug=models.SlugField(max_length = 60 , allow_unicode = True)
    class Meta : 
        verbose_name = "State"
        verbose_name_plural = "States"
    def save(self,*args, **kwargs) : 
        self.slug =slugify(self.name,allow_unicode=True)
        super(State,self).save(**kwargs)
    
    def __str__(self):
        return self.name
    
class City(models.Model) : 
    name = models.CharField(max_length=50 ,verbose_name=_('name'))
    state = models.ForeignKey(State, verbose_name=_("state"), on_delete=models.PROTECT) 
    slug=models.SlugField(max_length = 60 , allow_unicode = True)
    class Meta : 
        verbose_name = "City"
        verbose_name_plural = "Cities"
    def save(self,*args, **kwargs) : 
        self.slug = slugify(self.name,allow_unicode=True)
        super(City,self).save(**kwargs)
    def __str__(self):
        return self.name

class TransactionType(models.Model) : 
    name = models.CharField(max_length =50,unique=True,verbose_name=_('name'))
    slug=models.SlugField(max_length = 60 , allow_unicode = True)
    
    def save(self,*args, **kwargs) : 
        self.slug = slugify(self.name,allow_unicode=True)
        super(TransactionType,self).save(**kwargs)

    def __str__(self):
        return self.name
    
class RealestateType(models.Model) : 
    name = models.CharField(max_length=50,unique=True,verbose_name=_('name'))
    slug=models.SlugField(max_length = 60 , allow_unicode = True)
    
    def __str__(self):
        return self.name
    def save(self,*args, **kwargs) : 
        self.slug = slugify(self.name,allow_unicode = True)
        super(RealestateType,self).save(**kwargs)
    
    
class Realtor(models.Model) : 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.get_fullname()


def image_filepath(self,filename) :
    try :  
        path  = f"listing/listingimages/{self.realtor.user.id}/{filename}"
    except Exception as e :
        print(e)
        path  = f"listing/listingimages/{self.listing.realtor.id}/{filename}"
    return path  

    
class Listing(models.Model) : 
    title               = models.CharField(max_length=250,verbose_name=_("title"))
    transaction_type    = models.ForeignKey(TransactionType,verbose_name=_("Transaction Type"),on_delete=models.CASCADE)
    realestate_type     = models.ForeignKey(RealestateType,verbose_name=_("Realestate Type"),on_delete=models.CASCADE)
    state               = models.ForeignKey(State,verbose_name=_("state"), on_delete=models.CASCADE) 
    city                = models.ForeignKey(City,verbose_name=_("city"), on_delete=models.CASCADE)
    neiborhood          = models.CharField(max_length = 200,null = True , blank = True ,verbose_name=_("neiborhood")) 
    description         = models.TextField(verbose_name=_("description"),null=True,blank=True)
    square_meter        = models.FloatField(default=1,verbose_name=_("square meter"))
    n_bedrooms          = models.IntegerField(default = 1,verbose_name=_("number of bedrooms"))
    n_bathrooms         = models.IntegerField(default = 1,verbose_name=_("number of bathrooms"))
    garage              = models.BooleanField(default = False,verbose_name=_("garage"))
    price               = models.IntegerField(null=True,blank=True)
    added_on            = models.DateTimeField(auto_now_add = True,verbose_name=_("added on"))
    updated_on          = models.DateTimeField(auto_now=True,verbose_name=_("updated on"))
    status              = models.BooleanField(default = True,verbose_name=_("status"))
    realtor             = models.ForeignKey(Realtor,verbose_name=_("realtor"),on_delete = models.CASCADE)
    slug                = models.SlugField(max_length=250,unique=True,allow_unicode = True)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('listing-detail', kwargs = {"slug" : self.slug})
    def get_update_url(self):
        return reverse('listing-update', kwargs = {"slug" : self.slug})
    def get_delete_url(self):
        return reverse('listing-delete', kwargs = {"slug" : self.slug})

    def get_listing_byCity(self) : 
        
        return reverse('listing-bycity', kwargs = {"city" : self.city.slug})
    
    def get_listing_byState(self) : 
        
        return reverse('listing-bystate', kwargs = {"state" : self.state.slug})

class ListingImage(models.Model) : 
    image = models.ImageField(upload_to=image_filepath)
    listing = models.ForeignKey(Listing,related_name="images",on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name

def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug or instance.title != Listing.objects.filter(slug=instance.slug): 
        instance.slug = unique_slug_generator(instance)
        

pre_save.connect(pre_save_reciever, sender=Listing)
    



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_realtor(sender, instance, created, **kwargs):
    if created:
        Realtor.objects.create(user=instance)
    instance.realtor.save()