from django.urls import path
from . import views

app_name = 'poemas'

urlpatterns = [
    path('/<str:categoria>/', views.listaPoemas, name="listaPoemas"),
    path('like/<int:poema_id>/', views.likePoema, name="likePoema")
]