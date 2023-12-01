from rest_framework.views import APIView
from rest_framework.response import Response
from .Games.Tic_Toe import play

class TicTacToe(APIView):
    
    def post(self, request):
        cell = request.data.get('cell')
        tic_tac_toe_matrix = request.data.get('tic_tac_toe_matrix')
        data,context = play(cell = cell,tic_tac_toe_matrix = tic_tac_toe_matrix)
        return Response({'tic_tac_toe_matrix':data,'context': context[0], 'is_game_over': context[1]})