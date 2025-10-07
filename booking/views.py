from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import stripe

from .forms import AppointmentForm
from .models import Appointment

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            # create a Stripe Checkout Session (test mode using STRIPE_SECRET_KEY)
            domain = settings.DOMAIN.rstrip('/')
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': f"Appointment with {appointment.provider_name}"
                        },
                        # unit_amount is in cents (5000 = $50.00). Adjust as needed.
                        'unit_amount': 5000,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=f"{domain}{reverse('booking:success')}?session_id={{CHECKOUT_SESSION_ID}}",
                cancel_url=f"{domain}{reverse('booking:create')}",
                metadata={'appointment_id': str(appointment.id)},
            )

            appointment.stripe_checkout_session = session.id
            appointment.save()

            # redirect user to Stripe-hosted Checkout (test)
            return redirect(session.url)
    else:
        form = AppointmentForm()

    return render(request, 'booking/appointment_form.html', {'form': form})


def success(request):
    session_id = request.GET.get('session_id')
    # For this assessment we won't verify webhooks; this page just confirms a successful Checkout redirect.
    return render(request, 'booking/success.html', {'session_id': session_id})
