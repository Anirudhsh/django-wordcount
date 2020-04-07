from django.http import HttpResponse
from django.shortcuts import render

def scount(request):
    alltext = request.GET['rawtext']
    print(alltext)
    print(type(alltext))
    totalwords=alltext.split()
    worddic={}
    for word in totalwords:
        if word in worddic:
            worddic[word]+=1
        else:
            worddic[word]=1
    return render(request,'countpage.html',{'myvar':len(totalwords),'yoursong':alltext,'worddic':worddic})
def xhome(request):
    return render(request,'home.html',{'myvar':'GREAT WORK'})
def showabout(request):
    return render(request,'about.html',{'myvar':'GREAT WORK'})