from django.shortcuts import render, get_object_or_404
from .forms import CalcForm, SrcParametersForm, AreaCalcParametersForm, AreaResParametersForm, DownloadForm, CommonWindParametersForm, WindOroPametersInAltForm
from .models import Calc, SrcParameters
from django.utils import timezone
from django.shortcuts import redirect
import os
from django.contrib.auth.decorators import login_required
from .prepCalc import allAdmActions
from .downloadCalc import downloadFiles
from .pagination import pagListPagNextPagPrev
import random
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from django.http import JsonResponse
from copy import deepcopy
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


class SignUpView(CreateView):
    template_name = 'adm/signup.html'
    form_class = UserCreationForm


def getMinNum(request, postsCount):
    minNum = 1
    if "min" in request.GET.keys():
        if request.GET['min'] != '':
            if int(request.GET['min'])>postsCount:
                minNum = 1
                return minId, True
            else:
                minNum = int(request.GET['min'])
                return minNum, True
        else:
            minNum = 1
            return minNum, False
    else:
        minNum = 1
        return minNum, False
    

def getMaxNum(request, minId, postsCount):
    if "max" in request.GET.keys():
        if request.GET['max'] != '':
            if int(request.GET['max']) < minId:
                maxNum =  postsCount
                return maxNum, True
            else:
                maxNum = int(request.GET['max'])
                return maxNum, True
        else:
            maxNum = postsCount
            return maxNum, False
    else:
        maxNum = postsCount
        return maxNum, False

@login_required(login_url='/accounts/login/')
def admListPart(request, pagId = 1):
    posts = Calc.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    if request.method == "GET":
        postsCount = len(posts)
        minNum, minNumFlag = getMinNum(request, postsCount)
        maxNum, maxNumFlag = getMaxNum(request, minNum, postsCount)
        print(maxNum)
        posts = posts[minNum-1:maxNum:]
        posts, pagList, pagNext, pagPrev = pagListPagNextPagPrev(posts, pagId)
        return render(request, 'adm/admList.html', {'posts': posts, 'currPagId': pagId, 'pagList': pagList, 
                                                    'pagNext': pagNext, 'pagPrev': pagPrev, 'minNum':minNum, 'maxNum':maxNum, 'minNumFlag': minNumFlag, 'maxNumFlag':maxNumFlag})

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


def startCalcLogic(request):
    print("Start calc button was pressed")
    form = CalcForm(request.POST)
    srcParam = SrcParametersForm(request.POST)
    areaCalcParam = AreaCalcParametersForm(request.POST)
    areaResParam = AreaResParametersForm(request.POST)
    meteoWindOroNew = CommonWindParametersForm(request.POST)
    if form.is_valid() and srcParam.is_valid() and areaCalcParam.is_valid() and areaResParam.is_valid() and meteoWindOroNew.is_valid():
        post = form.save(commit=False)
        post.areaResParam = areaResParam.save()
        post.areaCalcParam = areaCalcParam.save()
        post.srcParam = srcParam.save()
        post.author = request.user
        post.published_date = timezone.now()
        post.calcADMReturn = 0
        post.save()

        allAdmActions(post)
        post.save()
        m = meteoWindOroNew.save()
        post.windPhaseList.add(m)
        post.save()
        return redirect('calc_started', pk=post.pk)

def addWindPhaseLogic(request, pk):
    print("Add WindOroPhase button was pressed")
    post = get_object_or_404(Calc, pk=pk)
    meteoWindOroNew = CommonWindParametersForm(request.POST)
    if meteoWindOroNew.is_valid():
        print('windOroValid')
        post.save()
        m = meteoWindOroNew.save()
        post.windPhaseList.add(m)
        post.save()
        print(model_to_dict(m))
        return JsonResponse({'newWindOroPhase': model_to_dict(m)}, status=200)

def saveCalcLogic(request, pk):
    print("Save button was pressed")
    post = get_object_or_404(Calc, pk=pk)
    form = CalcForm(request.POST, instance=post)
    srcParam = SrcParametersForm(request.POST, instance=post.srcParam)
    areaCalcParam = AreaCalcParametersForm(request.POST, instance=post.areaCalcParam)
    areaResParam = AreaResParametersForm(request.POST, instance=post.areaResParam)
    meteoWindOroOldList = post.windPhaseList.all()
    meteoWindOroNew = CommonWindParametersForm(request.POST)
    if form.is_valid() and srcParam.is_valid() and areaCalcParam.is_valid() and areaResParam.is_valid() and meteoWindOroNew.is_valid():
        post = form.save(commit=False)
        post.areaResParam = areaResParam.save()
        post.areaCalcParam = areaCalcParam.save()
        post.srcParam = srcParam.save()
        post.save()
        m = meteoWindOroNew.save()
        post.windPhaseList.add(m)
        post.save()
        return redirect('calc_edit', pk=post.pk)

@login_required(login_url='/accounts/login/')
def calc_edit(request, pk, page = ""):
        print ("------------------------------------------------------")
        print (request)
        print ("------------------------------------------------------")
        if request.method == "POST":
            print("request")
            print (request)
            print("request.POST")
            print(request.POST)
            addWindPhaseKeys = ['csrfmiddlewaretoken', 'meteoPhaseStart', 'windConst', 'precipitationsRate', 'precipitationType', 'stab', 'roughness']
            addWindPhaseKeys.sort()
            postKeys = list(request.POST.keys())
            postKeys.sort()

            if 'start_calc' in request.POST:
                return startCalcLogic(request)
            elif postKeys == addWindPhaseKeys:
                return addWindPhaseLogic(request, pk)
            else:
                return saveCalcLogic(request, pk)
        else:
            post = get_object_or_404(Calc, pk=pk)
            form = CalcForm(instance=post)
            print(type(post), type(form))
            srcParam = SrcParametersForm(instance=post.srcParam)
            areaCalcParam = AreaCalcParametersForm(instance=post.areaCalcParam)
            areaResParam = AreaResParametersForm(instance=post.areaResParam)
            meteoWindOroOldList = post.windPhaseList.all()
            meteoWindOroNew = CommonWindParametersForm()
            dictToRender = {'form': form, 'srcParam': srcParam, 
                                                          'areaCalcParam': areaCalcParam, 
                                                          'areaResParam': areaResParam, "meteoWindOroOldList": meteoWindOroOldList, "meteoWindOroNew": meteoWindOroNew, "pk": pk}
            return render(request, 'adm/admCalcCreate.html', dictToRender)


@login_required(login_url='/accounts/login/')
def calc_new(request):
    print ("------------------------------------------------------")
    print (request)
    print ("------------------------------------------------------")

    print("Get in calc_new")
    print ("request.path", request.path)

    form = CalcForm(request.GET)
    srcParam = SrcParametersForm(request.GET)
    areaCalcParam = AreaCalcParametersForm(request.GET)
    areaResParam = AreaResParametersForm(request.GET)
    meteoWindOro = CommonWindParametersForm(request.GET)
    windOroInAlt = WindOroPametersInAltForm(request.GET)
    print(form.is_valid(),  srcParam.is_valid(), areaCalcParam.is_valid(), areaResParam.is_valid())
    if form.is_valid() and srcParam.is_valid() and areaCalcParam.is_valid() and areaResParam.is_valid() and meteoWindOro.is_valid():
        post = form.save(commit=False)
        post.areaResParam = areaResParam.save()
        post.areaCalcParam = areaCalcParam.save()
        post.srcParam = srcParam.save()
        post.author = request.user
        post.published_date = timezone.now()
        post.calcADMReturn = 0
        post.save()
        return redirect(calc_edit, pk = post.pk)


def setRandParametersForPost(post, areaResParam):
    countCalcs = Calc.objects.count()
    post.name = "Calculation " + str(countCalcs+1)
    latInit = -88.0 + random.random()*176.0
    lonInit = -178.0 + random.random()*356.0
    lonMin = lonInit-0.5
    lonMax = lonInit+0.5
    latMin = latInit-0.5
    latMax = latInit+0.5
    post.areaResParam.lonMin = lonMin
    post.areaResParam.latMin = latMin
    post.areaResParam.lonMax = lonMax
    post.areaResParam.latMax = latMax
    post.areaResParam.countLon = 51
    post.areaResParam.countLat = 51
    post.areaCalcParam.lonMin = lonMin
    post.areaCalcParam.latMin = latMin
    post.areaCalcParam.lonMax = lonMax
    post.areaCalcParam.latMax = latMax
    post.srcParam.lon = lonInit
    post.srcParam.lat = latInit


@login_required(login_url='/accounts/login/')
def calc_rand(request):
    print ("------------------------------------------------------")
    print (request)
    print ("------------------------------------------------------")

    print ("request.path", request.path)
    countCalcs = Calc.objects.count()
    form = CalcForm(request.GET)
    srcParam = SrcParametersForm(request.GET)
    areaCalcParam = AreaCalcParametersForm(request.GET)
    areaResParam = AreaResParametersForm(request.GET)
    meteoWindOro = CommonWindParametersForm(request.GET)    
    if form.is_valid() and srcParam.is_valid() and areaCalcParam.is_valid() and areaResParam.is_valid() and meteoWindOro.is_valid():
        post = form.save(commit=False)
        post.areaResParam = areaResParam.save(commit=False)
        post.areaCalcParam = areaCalcParam.save(commit=False)
        post.srcParam = srcParam.save(commit=False)
        setRandParametersForPost(post, areaResParam)
        post.author = request.user
        post.published_date = timezone.now()
        post.calcADMReturn = 0
        post.areaResParam = areaResParam.save()
        post.areaCalcParam = areaCalcParam.save()
        post.srcParam = srcParam.save()
        post.save()
        return redirect(calc_edit, pk = post.pk)

@login_required(login_url='/accounts/login/')
def addFullWindParameters(request, form):
    if request.method == "POST":
        print("request.POST")
        print(request.POST)
    else:
        windForm = CommonWindParametersForm()
        return render(request, 'adm/createCalc/admCommonWind.html', {'windForm': windForm})