from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', include('booking.urls', namespace='booking')),
    # Make booking app available at the site root as well
    path('', include('booking.urls')),
    # Redirect the bare site root to the booking create page
    path('', RedirectView.as_view(url='/booking/create/', permanent=False)),
]

