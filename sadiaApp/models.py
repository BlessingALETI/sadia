from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# Modèle utilisateur personnalisé
class User(AbstractUser):
    groups = models.ManyToManyField('auth.Group', related_name='sadia_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='sadia_user_permissions')

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('client', 'Client'),
        ('restaurateur', 'Restaurateur'),
        ('livreur', 'Livreur'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    phone = models.CharField(max_length=15, blank=True, null=True)


# Modèle Restaurant
class Restaurant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'restaurateur'})  # Correction de SADIA → User
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True, null=True)

# Modèle Menu (Plats)
class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

# Modèle Commande
class Commande(models.Model):
    STATUS_CHOICES = [
        ('en_attente', 'En attente'),
        ('en_preparation', 'En préparation'),
        ('livraison', 'En livraison'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]
    client = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'client'})  # Correction de SADIA → User
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    items = models.ManyToManyField(Menu, through='CommandeItem')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en_attente')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

# Modèle pour gérer les articles dans une commande
class CommandeItem(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

# Modèle de Réservation
class Reservation(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'client'})  # Correction de SADIA → User
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateTimeField()
    number_of_people = models.PositiveIntegerField()

# Modèle Paiement
class Paiement(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[('carte', 'Carte Bancaire'), ('mobile', 'Mobile Money'), ('cash', 'Paiement à la livraison')])
    paid_at = models.DateTimeField(auto_now_add=True)

# Modèle Livraison
class Livraison(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    livreur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role': 'livreur'})  # Correction de SADIA → User
    delivery_status = models.CharField(max_length=20, choices=[('en_cours', 'En cours'), ('livree', 'Livrée')], default='en_cours')
    delivered_at = models.DateTimeField(null=True, blank=True)