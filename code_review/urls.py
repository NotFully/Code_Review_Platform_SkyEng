from django.urls import path
from . import views

app_name = 'code_review'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('reviewlist/<int:user_id>', views.reviewlist, name='reviewlist')
]

