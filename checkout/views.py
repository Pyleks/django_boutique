from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_from = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_from,
        'stripe_public_key': 'pk_test_51Gyez9DsrD0PTTMnk2E1wSWmcTUFwtticNhUamlui4NmPBpADZEtw27bjuXax695SrBbsKrXVD40aQYR1WPvEiEq000Y5057fP',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
