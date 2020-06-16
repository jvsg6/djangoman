import sys
import os

def pagListPagNextPagPrev(posts, pagId):
    pagDelta = 3   # только нечетное!!! количество пагинаций оторое показывается
    pagShift = pagDelta//2
    calcDelta = 5    # Количество расчетов в одной пагинации
    pagCount = 0
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
    return posts, pagList, pagNext, pagPrev

