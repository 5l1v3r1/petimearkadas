from django.shortcuts import render


def index(request):
    from random import randint
    number = randint(10,20)
    return render(request,"index.html",{"randomnum":number})
