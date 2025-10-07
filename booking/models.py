from django.db import models

class Appointment(models.Model):
    provider_name = models.CharField(max_length=255)
    appointment_time = models.DateTimeField()
    client_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    stripe_checkout_session = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.provider_name} @ {self.appointment_time.isoformat()} for {self.client_email}"
