from django.shortcuts import render


def d_index(request):
    return render(request, 'discovery/d_index.html')

