from django.urls import path
from .views import *

urlpatterns = [
    path('readboard/', ReadboardView.as_view(), name='ReadboardView'),
    path('postboard/', CreateboardView.as_view(), name='PostboardView'),
    path('uploadboard', UploadboardView.as_view(), name='UploadboardView'),
    path('selectboard/<int:pk>', SelectboardView.as_view(), name='selectboardView'),
    path('deleteboard/<int:pk>', DeleteboardView.as_view(), name='deleteboardView'),
]
