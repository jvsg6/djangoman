from django.shortcuts import render, get_object_or_404
from .forms import CalcForm
from .models import Calc
from django.utils import timezone
from django.shortcuts import redirect
import subprocess
def admIndex(request):
    posts = Calc.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'adm/admList.html', {'posts': posts})


def admCalc_start(request):
    if request.method == 'POST':
        pass
        #Do your stuff ,calling whatever you want from set_gpio.py

    return #Something, normally a HTTPResponse, using django

def calc_detail(request, pk):
    post = get_object_or_404(Calc, pk=pk)
    return render(request, 'adm/admCalcStarted.html', {'post': post})

def calc_started(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'adm/admCalcStarted.html', {'post': post})

def startAdm(pathToADM, pathToCalc):
    try:
        p = subprocess.Popen([pathToADM,  '--got=netcdf4','--db', pathToCalc], stdout=subprocess.PIPE)
    except OSError:
        print ("Error: Write valid path to ADM!")
        return
    return

def calc_new(request):
    if request.method == "POST":
        form = CalcForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            startAdm(post.pathToADM, post.pathToCalc)
            post.save()
            return redirect('calc_detail', pk=post.pk)
    else:
        form = CalcForm()
    return render(request, 'adm/admCalcCreate.html', {'form': form})