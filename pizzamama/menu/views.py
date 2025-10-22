from django.shortcuts import render
from django.http import HttpResponse
from . models import Pizza

# Create your views here.
# menu/
def index(requests):
    '''pizzas = Pizza.objects.all()
    pizza_names_and_prices = [pizza.nom+ ":" +str(pizza.prix)+ "€" for pizza in pizzas]
    pizza_names_and_prices_str = ", ".join(pizza_names_and_prices)

    return HttpResponse(f"Les pizzas: {pizza_names_and_prices_str}")'''
    pizzas = Pizza.objects.all().order_by('prix')
    return render(requests, 'menu/index.html', {"pizzas":pizzas})

