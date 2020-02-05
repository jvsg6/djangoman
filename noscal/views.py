from django.shortcuts import render

def noscal(request):
    return render(request, 'noscal/noscalPage.html', {})
