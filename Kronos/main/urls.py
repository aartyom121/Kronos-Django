from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    # path('i', views.i, name="i"),
    path('for_admin', views.for_admin, name='for_admin')
]
