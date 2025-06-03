from django.shortcuts import render

# Create your views here.
def accueil(request):
    return render(request, 'Clients/index.html')

from django.shortcuts import render

def restaurants(request):
    # Exemple de données statiques (tu pourras plus tard récupérer depuis une base)
    restaurants_list = [
        {
            "name": "Le Gourmet",
            "description": "Un restaurant chic proposant une cuisine française raffinée...",
            "address": "123 Rue de la Paix, Lomé",
            "phone": "+228 90 12 34 56",
            "image": "https://source.unsplash.com/800x600/?restaurant,fine-dining"
        },
        {
            "name": "Saveurs d’Afrique",
            "description": "Découvrez les plats traditionnels africains préparés avec amour...",
            "address": "45 Avenue des Palmiers, Lomé",
            "phone": "+228 90 98 76 54",
            "image": "https://source.unsplash.com/800x600/?african-food,restaurant"
        },
        # Ajoute d'autres restaurants ici...
    ]

    context = {
        'restaurants': restaurants_list
    }
    return render(request, 'clients/restaurants.html', context)

from django.shortcuts import render

def menu(request):
    # Liste des plats (tu peux plus tard la récupérer depuis la base de données)
    plats = [
        {
            'nom': 'Burger Classic',
            'description': 'Bœuf, cheddar, laitue, tomate, sauce spéciale',
            'prix': '6.90€',
            'image': 'Clients/assets/images/menu/burger-classic.jpg'
        },
        {
            'nom': 'Frites Maison',
            'description': 'Frites croustillantes et dorées, sauce ketchup ou mayonnaise',
            'prix': '2.50€',
            'image': 'Clients/assets/images/menu/frites-maison.jpg'
        },
        {
            'nom': 'Salade César',
            'description': 'Laitue croquante, poulet grillé, parmesan et croûtons',
            'prix': '5.90€',
            'image': 'Clients/assets/images/menu/salade-cesar.jpg'
        },
        {
            'nom': 'Milkshake Vanille',
            'description': 'Milkshake onctueux à la vanille naturelle',
            'prix': '3.50€',
            'image': 'Clients/assets/images/menu/milkshake-vanille.jpg'
        },
        # Ajoute autant de plats que tu veux...
    ]

    return render(request, 'Clients/menu.html', {'plats': plats})

from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib import messages

def reservation(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        date = request.POST.get('date')
        heure = request.POST.get('heure')
        personnes = request.POST.get('personnes')
        message = request.POST.get('message')

        # Simule la sauvegarde en base

        messages.success(request, f"Merci {nom}, votre réservation pour {personnes} personnes le {date} à {heure} a bien été prise en compte !")

        return redirect('reservation')

    # Par exemple, si tu veux une liste de nombre de personnes possibles :
    personnes_possibles = range(1, 11)  # 1 à 10 personnes

    return render(request, 'Clients/reservation.html', {
        'personnes_possibles': personnes_possibles
    })

from django.shortcuts import render

def menu_detail(request):
    # Logique pour afficher le menu
    return render(request, 'menu_detail.html')
