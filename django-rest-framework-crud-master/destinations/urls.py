from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateDestinationAPIView.as_view(), name='get_post_destinations'),
    path('<int:pk>/', views.RetrieveUpdateDestroyDestinationAPIView.as_view(), name='get_delete_update_destinations'),
]