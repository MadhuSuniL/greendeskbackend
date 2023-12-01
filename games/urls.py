from django.urls import path
from .views import *

urlpatterns = [
    path('tic_tac_toe',TicTacToe.as_view())
]