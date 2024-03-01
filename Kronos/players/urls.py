from django.urls import path
from . import views

urlpatterns = [
    path('', views.players_home, name='players_home'),
    path('create_players', views.create_players, name='create_players'),
    path('<int:pk>', views.PlayersDetailView.as_view(), name="players-detail"),
    path('<int:pk>/update', views.PlayersUpdateView.as_view(), name="players-update"),
    path('<int:pk>/delete', views.PlayersDeleteView.as_view(), name="players-delete"),
    path('search/', views.search.as_view(), name='search_players')
]
