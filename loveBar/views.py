from django.shortcuts import render

def loveBar(request):
    return render(request, 'loveBar/barPage.html', {})
