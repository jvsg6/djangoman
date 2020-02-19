from django.shortcuts import render, get_object_or_404
from .forms import CalcForm, SrcParametersForm, AreaCalcParametersForm, AreaResParametersForm
from .models import Calc
from django.utils import timezone
from django.shortcuts import redirect
import os

from .prepCalc import allAdmActions



def admIndex(request):
    posts = Calc.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'adm/admList.html', {'posts': posts})


def admCalc_start(request):
    if request.method == 'POST':
        pass
        #Do your stuff ,calling whatever you want from set_gpio.py

    return #Something, normally a HTTPResponse, using django

def calc_details(request, pk):
    post = get_object_or_404(Calc, pk=pk)
    return render(request, 'adm/admCalcDetails.html', {'post': post})

def calc_started(request, pk):
    post = get_object_or_404(Calc, pk=pk)
    return render(request, 'adm/admCalcStarted.html', {'post': post})



def calc_new(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CalcForm(request.POST)
            srcParam = SrcParametersForm(request.POST)
            areaCalcParam = AreaCalcParametersForm(request.POST)
            areaResParam = AreaResParametersForm(request.POST)
            if form.is_valid() and srcParam.is_valid() and areaCalcParam.is_valid() and areaResParam.is_valid():
                post = form.save(commit=False)
                post.areaResParameters = areaResParam.save()
                post.areaCalcParameters = areaCalcParam.save()
                post.srcParameters = srcParam.save()
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                allAdmActions(post)
                return redirect('calc_started', pk=post.pk)
        else:
            form = CalcForm()
            srcParam = SrcParametersForm()
            areaCalcParam = AreaCalcParametersForm()
            areaResParam = AreaResParametersForm()
        return render(request, 'adm/admCalcCreate.html', {'form': form, 'srcParam': srcParam, 'areaCalcParam': areaCalcParam, 'areaResParam': areaResParam})
    else:
        return render(request, 'registration/login.html')
