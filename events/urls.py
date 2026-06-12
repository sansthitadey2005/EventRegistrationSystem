from django.urls import path
from .views import event_list, registration_list,delete_registration

urlpatterns = [
    path('events/', event_list),
    path('registrations/', registration_list),
    path('registrations/<int:pk>/', delete_registration),
]