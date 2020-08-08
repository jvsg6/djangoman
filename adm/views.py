import os
from copy import deepcopy


from ManualSource.forms import SrcParametersForm
from WindOro.forms import CommonWindParametersForm, WindOroPametersInAltForm
from .forms import CalcForm, AreaCalcParametersForm, AreaResParametersForm, DownloadForm
from django.contrib.auth.forms import UserCreationForm


from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .downloadCalc import downloadFiles
from .pagination import pagListPagNextPagPrev

from django.http import JsonResponse


from django.views.generic.edit import CreateView

from .models import Calc
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .tasks import allAdmActions

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
                return minNum, True
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
    areaCalcParam = AreaCalcParametersForm(initial={'lonMinCalc': lonInit-0.5, 'lonMaxCalc': lonInit+0.5, 'latMinCalc': latInit-0.5, 'latMaxCalc': latInit+0.5})
    areaResParam = AreaResParametersForm(initial={'lonMinRes': lonInit-0.5, 'lonMaxRes': lonInit+0.5, 'latMinRes': latInit-0.5, 'latMaxRes': latInit+0.5, 'countLonRes': 50, 'countLatRes': 50})
    return srcParam, areaCalcParam, areaResParam


def startCalcLogic(request, pk):
    print("Start calc button was pressed")
    post = get_object_or_404(Calc, pk=pk)

    form = CalcForm(request.POST, instance=post)
    srcParam = SrcParametersForm(request.POST, instance=post.srcParam)
    areaCalcParam = AreaCalcParametersForm(request.POST, instance=post.areaCalcParam)
    areaResParam = AreaResParametersForm(request.POST, instance=post.areaResParam)
    meteoWindOroNew = CommonWindParametersForm(request.POST)
    if form.is_valid() and srcParam.is_valid() and areaCalcParam.is_valid() and areaResParam.is_valid() and meteoWindOroNew.is_valid():
        post = form.save(commit=False)
        post.areaResParam = areaResParam.save()
        post.areaCalcParam = areaCalcParam.save()
        post.srcParam = srcParam.save()
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        allAdmActions.delay(post.pk)
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
                return startCalcLogic(request, pk)
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
        post.save()
        return redirect(calc_edit, pk = post.pk)

@login_required(login_url='/accounts/login/')
def calc_delete(request, pk):
    print ("------------------------------------------------------")
    print (request)
    print ("------------------------------------------------------")
    print(f"Delete calc {pk}")
    b = Calc.objects.get(pk=pk)
    b.delete()
    return redirect('admListPart', pagId = 1)

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
        post.setRandParameters()
        post.author = request.user
        post.published_date = timezone.now()
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