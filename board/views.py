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