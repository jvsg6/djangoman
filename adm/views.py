from django.shortcuts import render, get_object_or_404
from .forms import CalcForm, SrcParametersForm, AreaCalcParametersForm, AreaResParametersForm, DownloadForm, CommonWindParametersForm
from .models import Calc
from django.utils import timezone
from django.shortcuts import redirect
import os
from django.contrib.auth.decorators import login_required
from .prepCalc import allAdmActions
from .downloadCalc import downloadFiles
import random

@login_required(login_url='/accounts/login/')
def admListPart(request, pagId = 1):
    pagDelta = 3   # только нечетное!!! количество пагинаций
    pagShift = pagDelta//2
    calcDelta = 4    # Количество расчетов в одной пагинации
    pagCount = 0
    posts = Calc.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    calcCount = len(posts)
    if calcCount % calcDelta == 0:
        pagCount = calcCount//calcDelta
    else:
        pagCount = calcCount//calcDelta + 1

    pagList = []
    pagNext = -1
    pagPrev = -1
    posts = posts[calcDelta*(pagId - 1): calcDelta*pagId] #Расчеты в данной пагинации
    if pagId <= pagCount:
        if pagId < pagDelta:
            if pagCount - pagId >= pagShift:
                #pagList = range(1, pagId + pagShift + 1)
                pagList = range(1, pagDelta + 1)
            else:
                pagList = range(1, pagId + 1)
        else:
            if pagCount - pagId >= pagShift:
                pagList = range(pagId - pagShift, pagId + pagShift + 1)
            else:
                pagList = range(pagCount - pagDelta + 1, pagId+1)

    if pagId != 1:
        if pagId != pagCount:
            pagNext = pagId + 1
            pagPrev = pagId -1
        else:
            pagNext = -1
            pagPrev = pagId -1
    else:
        if pagId != pagCount:
            pagNext = pagId + 1
            pagPrev = -1
        else:
            pagNext = -1
            pagPrev = -1
    #pagList = [str(i) for i in pagList]
    #assert False
    return render(request, 'adm/admList.html', {'posts': posts, 'currPagId': pagId, 'pagList': pagList, 'pagNext': pagNext, 'pagPrev': pagPrev})

@login_required(login_url='/accounts/login/')
def admCalc_start(request):
    if request.method == 'POST':
        pass
        #Do your stuff ,calling whatever you want from set_gpio.py

    return #Something, normally a HTTPResponse, using django


@login_required(login_url='/accounts/login/')
def calc_download(request, pk):
    calc = get_object_or_404(Calc, pk=pk)
    if request.method == "POST":
        print ( request.POST.getlist('download'))
        return downloadFiles(request.POST.getlist('download'), calc)
    else:
        return render(request, 'adm/admDownload.html', {'post': calc})

@login_required(login_url='/accounts/login/')
def calc_details(request, pk):
    post = get_object_or_404(Calc, pk=pk)
    return render(request, 'adm/admCalcDetails.html', {'post': post})


@login_required(login_url='/accounts/login/')
def calc_started(request, pk):
    post = get_object_or_404(Calc, pk=pk)
    return render(request, 'adm/admCalcStarted.html', {'post': post})

def installRandomParameters():
    latInit = -88.0 + random.random()*176.0
    lonInit = -178.0 + random.random()*356.0
    srcParam = SrcParametersForm(initial={'lon': lonInit, 'lat': latInit})
    areaCalcParam = AreaCalcParametersForm(initial={'lonMin': lonInit-0.5, 'lonMax': lonInit+0.5, 'latMin': latInit-0.5, 'latMax': latInit+0.5})
    areaResParam = AreaResParametersForm(initial={'lonMin': lonInit-0.5, 'lonMax': lonInit+0.5, 'latMin': latInit-0.5, 'latMax': latInit+0.5, 'countLon': 50, 'countLat': 50})
    return srcParam, areaCalcParam, areaResParam

@login_required(login_url='/accounts/login/')
def calc_new(request):

        if request.method == "POST":
            print (request)
            print(request.POST)
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
                post.calcADMReturn = 0
                post.save()
                allAdmActions(post)
                post.save()
                return redirect('calc_started', pk=post.pk)
        else:
            form = CalcForm()
            srcParam = None
            areaCalcParam = None
            areaResParam = None
            if request.path == "/rand":
                print ("request.path", request.path)
                srcParam, areaCalcParam, areaResParam = installRandomParameters()
            else:
                print ("request.path", request.path)
                srcParam = SrcParametersForm()
                areaCalcParam = AreaCalcParametersForm()
                areaResParam = AreaResParametersForm()
        return render(request, 'adm/admCalcCreate.html', {'form': form, 'srcParam': srcParam, 'areaCalcParam': areaCalcParam, 'areaResParam': areaResParam,})
