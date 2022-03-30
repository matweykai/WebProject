from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def univ_info(request):
    return render(request, 'website/about_univ.html')
