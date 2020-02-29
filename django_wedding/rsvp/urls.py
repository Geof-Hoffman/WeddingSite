from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='rsvp-home'),  
    path('about/', views.about, name='rsvp-about'),
    path('guestbook/', views.guestbook, name='rsvp-guestbook'),
    path('events/', views.events, name='rsvp-events')

]
