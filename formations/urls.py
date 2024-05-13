from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('formations/', views.home, name='home'),
    path('formation/<int:pk>', views.formation_detail, name='formation'),
    path('enroll/<int:pk>', views.enroll_form, name='enroll'),
]
