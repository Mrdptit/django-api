from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser
)
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password = None):
        if not email:
            raise ValueError('Users must have email address')
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using = self.db)
        return user
    def create_staffuser(self, email, password):

        user = self.create_user(
            email,
            password = password,
        )
        user.staff = True
        user.save(using = self.db)
        return user
    def create_superuser(self,email,password):

        user = self.create_user(
            email,
            password = password,
        )
        user.staff = True
        user.admin = True
        return user
class  User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255,
        unique = True,
    )
    facebook_id = models.CharField(max_length = 255,default='')
    avatar = models.CharField(max_length = 255,default='')
    cover = models.CharField(max_length = 255, default='')
    active = models.BooleanField(default = True)
    staff = models.BooleanField(default= False)
    admin = models.BooleanField(default = False)
    USERNAME_FIELD =    'email'
    REQUIRED_FILEDS = []
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
    u_id = models.CharField(max_lenght = 255, default= '')
    key_word = models.CharField(max_length = 255, default = '')

class Value_Charater(models.Model):
    key_word = models.ForeignKey(KeyWord, on_delete=models.CASCADE)
    value_key = models.CharField(max_length = 255, default= '')