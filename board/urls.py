from django.urls import path
from .views import ReadboardView, CreateboardView, UploadboardView

urlpatterns = [
    path('readboard/', ReadboardView.as_view(), name='ReadboardView'),
    path('postboard/', CreateboardView.as_view(), name='PostboardView'),
    path('uploadboard', UploadboardView.as_view(), name='PostboardView')
]
