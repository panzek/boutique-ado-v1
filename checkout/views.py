from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MIiVaFbqU4cBDZBnM0rdTb2LlbAl893koVO8JUcVUQLqW67dOeTX8Xx6GnUKmoT5KdPbtGIiVdPreJrZP7djCoN00FNPfs0DG',
        'client_secret': 'test client secret',
    }

    return render(request, 'checkout/checkout.html', context)

