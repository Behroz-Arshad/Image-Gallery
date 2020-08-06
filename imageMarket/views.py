from django.shortcuts import render
from . models import Image,Category

# Create your views here.
def index(request):
    categories=Category.objects.all()
    images=Image.objects.all()
    data={'images':images,'categories':categories}
    return render(request,'imageMarket/index.html',data)

def categoryById(request,id):
    categories = Category.objects.all()
    catById=Category.objects.get(pk=id)
    images=Image.objects.filter(category=catById)
    data={'images':images,'categories':categories}

    return render(request,'imageMarket/index.html',data)