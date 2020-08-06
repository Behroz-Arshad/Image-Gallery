
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('category/<int:id>',views.categoryById,name='categoryByID'),
]