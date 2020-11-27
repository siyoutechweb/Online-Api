from django.db import models
from django.contrib.auth.models import User , BaseUserManager,AbstractBaseUser
from shopApp.models import Store
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    store = models.ForeignKey(Store,on_delete=models.CASCADE,default=1)
    #new fields
    address = models.CharField(max_length=200,default='No address configured yet')
    country = models.CharField(max_length=200,default='No country configured yet')
    city = models.CharField(max_length=200,default='No city configured yet')
    street = models.CharField(max_length=200,default='No street configured yet')
    zip_code = models.IntegerField(default='1234')
    phone = models.CharField(max_length=200,default='No phone number configured yet')
    def set_store(storename):
        self.store=storename
    def __str__(self):
        return f'Profile for user {self.user.username}'


    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    post_save.connect(create_profile, sender=User)
