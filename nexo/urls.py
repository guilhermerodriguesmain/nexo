from django.urls import path
from . import views

urlpatterns = (
    path(
        "",
        views.inicio,
        name="inicio",
    ),
    path(
        "movimentacoes/",
        views.movimentacoes_list,
        name="movimentacoes_list",
    ),
)
