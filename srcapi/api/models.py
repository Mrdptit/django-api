from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser,PermissionsMixin,
)
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
import string
import random
# Create your models here.
DEFAULT_COVER = 'https://www.google.com.vn/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwinz97z6KvYAhUfSI8KHVL7CsgQjRwIBw&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DQX4j_zHAlw8&psig=AOvVaw2alZ9a3n7ICEn89KdwdkAk&ust=1514520024404108'
DEFAULT_AVATAR = 'https://www.google.com.vn/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjXmYPb6KvYAhXLto8KHVlVDC8QjRwIBw&url=http%3A%2F%2Fwww.yxineff.com%2Fen%2Ffilmmakers%2Fnguyen-thuy-tien%2F&psig=AOvVaw010B5-zNbkVHktKfy_JPy0&ust=1514519967983392'
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid e-mail address')

        # Ensure that a username is set
        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username')

        user = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username'),
            first_name=kwargs.get('first_name', None),
            last_name=kwargs.get('last_name', None),
        )

        user.set_password(password)
        user.save(using = self.db)
        user.token = Token.objects.get_or_create(user=user)[0].key
        user.verify_key = random_generator()
        return user
    def create_staffuser(self, email, password=None, **kwargs):

        user = self.create_user(
            email,
            password = password,
            kwargs = kwargs,
        )
        user.staff = True
        user.save(using = self.db)
        return user
    def create_superuser(self, email, password=None, **kwargs):

        user = self.create_user(
            email,
            password = password,
            kwargs = kwargs,
        )
        user.staff = True
        user.admin = True
        return user
class  User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255,
        unique = True,
    )
    username = models.CharField(max_length = 255,default = email)
    last_name = models.CharField(max_length = 255,default= '')
    first_name = models.CharField(max_length = 255,default= '')
    token = models.CharField(max_length = 255,default= '')
    facebook_id = models.CharField(max_length = 255,default='')
    avatar = models.CharField(max_length = 255,default=DEFAULT_AVATAR)
    cover = models.CharField(max_length = 255, default=DEFAULT_COVER)
    active = models.BooleanField(default = True)
    staff = models.BooleanField(default= False)
    admin = models.BooleanField(default = False)
    is_superuser= models.BooleanField(default= False)
    create_date = models.DateTimeField(auto_now_add=True)
    verifyUser = models.BooleanField(default = False)
    verify_key = models.CharField(max_length=40,default ='')
    USERNAME_FIELD =    'email'
    REQUIRED_FILEDS = ['username']
    objects = UserManager()
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def has_perm(self, perm, obj = None):
        return True
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_active(self):
        return self.active
class KeyWord(models.Model):
    u_id = models.CharField(max_length = 255, default= '')
    key_word = models.CharField(max_length = 255, default = '')

class Value_Charater(models.Model):
    key_word = models.CharField(max_length = 255, default= '')
    value_key = models.CharField(max_length = 255, default= '')
    u_id = models.CharField(max_length = 255, default= '')