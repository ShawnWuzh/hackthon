from django.db import models
from category.models import Category
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.


class Play(models.Model):
    title = models.CharField(max_length=120)
    time = models.DateTimeField(auto_now=False,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    owner = models.ForeignKey(User,related_name='owner')
    cate = models.ForeignKey(Category)
    target_num_participants = models.IntegerField()
    num_of_participants = models.IntegerField(default=0)
    participants = models.ManyToManyField(User,related_name='participants',blank=True)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return str(self.title)
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    class Meta:
        verbose_name_plural = 'plays'

    def get_absolute_url(self):
        return reverse('play:play',kwargs={'slug':self.slug})









