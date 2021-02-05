from django.shortcuts import render


def home(request):
    name = 'Nick'

    return render(request, 'home.html', {'name': name})
