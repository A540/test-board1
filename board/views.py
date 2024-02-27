from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import board


# Create your views here.
class ReadboardView(APIView):
    def get(self, request):
        board_list = board.objects.all()

        return render(request, 'board/board.html', context={'board_list': board_list})

class CreateboardView(APIView):
    def get(self,request):
        return render(request, 'board/post.html')

class UploadboardView(APIView):
    def post(self, request):
        title = request.POST.get('title')
        name = request.POST.get('name')
        content = request.POST.get('content')

        create = board.objects.create(title=title, name=name, content=content)

        if create:
            return Response(status=200)
        else:
            return Response(status=204)

class SelectboardView(APIView):
    def get(self, request, pk):
        p_board = board.objects.get(id=pk)
        p_board.content = p_board.content.replace('\r\n', '<br>')

        return render(request, 'board/selectboard.html', context={'p_board': p_board})

class DeleteboardView(APIView):
    def post(self, request, pk):
        try:
            d_board = board.objects.get(id=pk)
            d_board.delete()
            return Response(status=200)
        except board.DoesNotExist:
            return Response(status=403)