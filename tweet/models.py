from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
# from django.conf import settings
# # Create your models here.

# User = settings.AUTH_USER_MODEL


# class User(models.Model):
#     username = models.CharField(max_length=70)
#     email = models.EmailField(max_length=70)
#     password = models.CharField(max_length=70)

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


def upload_to2(instance, filename):
    return 'xml/{filename}'.format(filename=filename)


class ImageUpload(models.Model):
    id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=100, null=True)
    object_name = models.CharField(max_length=100, null=True)
    x_min = models.IntegerField(null=True)
    x_max = models.IntegerField(null=True)
    y_min = models.IntegerField(null=True)
    y_max = models.IntegerField(null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    image_path = models.ImageField(_("Image"), upload_to=upload_to, null=True)
    xml_path = models.ImageField(_("XML"), upload_to=upload_to2, null=True)


# class CustomAccountManager(BaseUserManager):
#     def create_superuser(self, email, username, firstname, password, **other_fields):
#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)
#         if other_fields.get('is_staff') is not True:
#             raise ValueError('Error')
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError('Error')
#         return self.create_user(email, username, firstname, password, **other_fields)

#     def create_user(self, email, username, firstname, password, **other_fields):
#         if not email:
#             raise ValueError('Required Email')
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username,
#                           firstname=firstname, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user


# class NewUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=150, unique=True)
#     firstname = models.CharField(max_length=150, blank=True)
#     start_date = models.DateTimeField(default=timezone.now)
#     about = models.TextField(max_length=200)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     objects = CustomAccountManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELD = ['username', 'firstname']

#     def __str__(self):
#         return self.username

# class TweetLike(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)


# class Tweet(models.Model):
#     # id=models.AutoField(primary_key=True)
#     # Many users can have many tweets
#     parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     likes = models.ManyToManyField(
#         User, related_name='tweet_user', blank=True, through=TweetLike)
#     content = models.TextField(blank=True, null=True)
#     image = models.FileField(upload_to='images/', blank=True, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.content

#     @property
#     def is_retweet(self):
#         return self.parent != None
