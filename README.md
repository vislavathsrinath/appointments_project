# Django Appointments Project

A simple Django project demonstrating an appointment booking system with a mock Stripe payment flow.

---

## Features

- **Appointment model**: Tracks `provider_name`, `appointment_time`, and `client_email`.
- **Booking form / API endpoint**: Allows clients to create appointments.
- **Mock Stripe payment integration**: Uses Stripe test keys to create a PaymentIntent or CheckoutSession.

---

## Requirements

- Python 3.12+
- Django 5.x
- Stripe Python SDK
- Other dependencies in `requirements.txt`

---

## Setup Instructions 


1. **Clone the repository and switch to `dev` branch**

```bash
git clone <repo-url>
cd <repo-folder>
git checkout dev

2. Create a virtual environment and activate it

python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Windows cmd
.venv\Scripts\activate.bat
# macOS/Linux
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Set environment variables
# Windows PowerShell
$env:DJANGO_SECRET_KEY="devsecret"
$env:DEBUG="1"
$env:STRIPE_SECRET_KEY="sk_test_..."
$env:STRIPE_PUBLISHABLE_KEY="pk_test_..."
$env:DOMAIN="http://localhost:8000"
5. Run migrations
python manage.py runserver
6. Start the development server
python manage.py runserver

