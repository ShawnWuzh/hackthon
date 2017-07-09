from django.db import models
from play.models import Play
from django.template.defaultfilters import slugify

# Create your models here.

class Car(models.Model):
    url = models.URLField()
    slug = models.SlugField(unique=True)
    play_object = models.OneToOneField(Play,null=True,blank=True)

    def __str__(self):
        return str(self.url)
    def save(self,*args,**kwargs):
        self.slug = slugify(self.url)
        super().save(*args,**kwargs)





