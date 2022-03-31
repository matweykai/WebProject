from django.shortcuts import render
from django.views import generic
from .models import Direction


def index(request):
    return render(request, 'website/index.html')


def univ_info(request):
    return render(request, 'website/about_univ.html')


def project_info(request):
    return render(request, 'website/about_project.html')


def directions_view(request):
    grdnt_lst = list()
    directions = Direction.objects.all()

    grnts = ['purple_grad', 'green_grad', 'blue_grad']
    counter = 0

    for i in range(len(directions)):
        if i % 3 == 0:
            counter += 1
        grdnt_lst.append(grnts[(i + counter) % 3])

    context = {'gradient_lst': grdnt_lst,
               'directions': directions}

    return render(request, 'website/directions.html', context=context)
