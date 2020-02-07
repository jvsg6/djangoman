from django.shortcuts import render, get_object_or_404
from .forms import CalcForm
from .models import Calc
from django.utils import timezone
from django.shortcuts import redirect
from .forms import CalcForm
import subprocess
def admIndex(request):
    return render(request, 'admCalc/admIndex.html', {})


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

def startAdm():
    try:
        p = subprocess.Popen(['',  '--got=netcdf4','--db', ''], stdout=subprocess.PIPE)
    except OSError:
        print ("Error: Write valid path to ADM!")
        return
    return

def calc_new(request):
    if request.method == "POST":
        form = CalcForm(request.POST)
        if form.is_valid():
            startAdm()
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('calc_detail', pk=post.pk)
    else:
        form = CalcForm()
    return render(request, 'adm/admCalcCreate.html', {'form': form})
