from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Vous devez renseigner votre adresse email")
        if not password:
            raise ValueError("Vous devez renseigner votre mot de passe")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_admin=True,
            is_staff=True
        )
        return user


# Cette classe represente le model utilisateur
class Utilisateur(AbstractBaseUser, PermissionsMixin):
    # Attributes
    email = models.EmailField(max_length=80, unique=True)
    is_active = models.BooleanField(default=True)  # can login
    admin = models.BooleanField(default=False)  # admin user is superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    code_validation = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'  # login require email

    REQUIRED_FIELDS = []

    objects = UserManager()

    # Methods
    def _str_(self):
        return self.email

    def get_email(self):
        return self.email

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.is_admin
    
    
    

# cette classe represente le model type_bien
class Type_Biens(models.Model):
    #Attributes
    nameType = models.CharField(max_length=35)
    
    
    
    
# cette classe represente le model groupe
class Groupe(models.Model):
    nomGroupe =  models.CharField(max_length=20)
    
    
    
# cette classe represente le model role
class Role(models.Model):
    nomRole = models.CharField
    statut =  models.BooleanField()
    # Foreign keys
    user = models.ForeignKey(
        Utilisateur, on_delete=models.CASCADE, related_name='user_Role')
    groupe = models.ForeignKey(
        Groupe, on_delete=models.CASCADE, related_name='Groupe_Role')
    
    
    
    
# Cette classe représente le model Biens
class Biens(models.Model):
    # Attributes
    nom = models.CharField(max_length=35)
    description = models.CharField(max_length=35)
    statuts = models.BooleanField(max_length=35)
    # Foreign keys
    user = models.ForeignKey(
        Utilisateur, on_delete=models.CASCADE, related_name='user_Biens')
    type_Biens = models.ForeignKey(
        Type_Biens, on_delete=models.CASCADE, related_name='Type_Biens')
    groupe = models.ForeignKey(
        Groupe, on_delete=models.CASCADE, related_name='Groupe_Biens')
    
    

    
# Cette classe represente le model temp_occupation
class temp_occupation(models.Model):
    #Attributes
    datetimedebut = models.DateTimeField(auto_now=False, auto_now_add=False)
    datetimefin = models.DateTimeField(auto_now=False, auto_now_add=False)
    validertemps = models.BooleanField()
    # Foreign keys
    user = models.ForeignKey(
        Utilisateur, on_delete=models.CASCADE, related_name='user_TempsOcc')
    biens = models.ForeignKey(
        Biens, on_delete=models.CASCADE, related_name='Biens_TempsOcc')