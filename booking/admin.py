from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', include('booking.urls', namespace='booking')),
    # Optionally: path('', include('booking.urls')), to make booking root
]
