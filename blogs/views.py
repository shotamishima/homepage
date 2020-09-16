from django.shortcuts import render


def home(request):
    return render(request, 'blogs/home_en.html')


def home_in_jp(request):
    return render(request, 'blogs/home_jp.html')
