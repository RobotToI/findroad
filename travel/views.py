from django.shortcuts import render


def home(request):
    name = 'Nick'

    return render(request, 'home.html', {'name': name})


def about(request):
    name = 'Nick'

    return render(request, 'about.html', {'name': name})
