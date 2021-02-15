from django.utils.text import slugify 
import random 
import string


def unique_slug_generator(instance) : 
    slug =  slugify(instance.title,allow_unicode=True)
    klass = instance.__class__
    while klass.objects.filter(slug=slug).exists() : 
        slug = f"{slug}-{random.randint(1,1000)}"
    return slug 