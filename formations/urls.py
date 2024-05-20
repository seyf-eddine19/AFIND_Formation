from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('a-propos/', views.about, name='about'),
    path('formations/', views.formations, name='formations'),
    path('formation/<int:pk>', views.formation_detail, name='formation'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('politique-de-confidentialite/', views.privacy_policy, name='privacy_policy'),
    path('conditions-generales-d-utilisation/', views.terms_of_service, name='terms_of_service'),
]
