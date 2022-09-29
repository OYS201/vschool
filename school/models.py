from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,BaseUserManager



class MyUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Provide an email option")

        # if not last_name:  
        #     raise ValueError("Provide a last_name option")

        # if not first_name:
        #     raise ValueError("Provide a first_name option")

        user=self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db) 
        return user

    def create_superuser(self,email,password=None,**extra_fields):
        user=self.create_user(
            email=self.normalize_email(email),
            password=password,
            **extra_fields
        )
        user.is_superuser=True   
        user.is_staff=True
        user.save(using=self._db)
        return user







# Create your models here.
class MyUser(AbstractBaseUser):
   first_name = models.CharField(max_length=200,null=True)
   last_name = models.CharField(max_length=200,null=True)
   phone=models.CharField(max_length=200,null=True,unique=True)
   address=models.CharField(max_length=200,null=True)
   photo=models.ImageField(upload_to="school",blank=True)
   email=models.EmailField(max_length=60,unique=True)
   index_number=models.CharField(max_length=10,unique=True,blank=True, null=True)
   last_login_at = models.DateTimeField(blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   is_staff = models.BooleanField(default=False)
   is_superuser = models.BooleanField(default=False)
   is_student = models.BooleanField(default=False)
   is_active = models.BooleanField(default=True)

   USERNAME_FIELD = "email"
   REQUIRED_FIELDS = []

#    REQUIRED_FIELDS=['first_name','last_name']

   objects= MyUserManager()



   def __str__(self):
       return self.first_name or self.email

   def has_perm(self,perm,obj=None):
       return True

       
       
   def has_module_perms(self,app_label):
       return True


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name
        







          
    
    



        
