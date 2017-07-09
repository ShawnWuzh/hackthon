from django.db import models
from django.template.defaultfilters import slugify
from django.shortcuts import reverse
# Create your models here.


class Category(models.Model):

    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='cates_imgs')
    def __str__(self):
        return str(self.title)
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def category_url(self):
        return reverse('category:category_detail',kwargs={'slug':self.slug})


    class Meta:
        verbose_name_plural = 'categories'



