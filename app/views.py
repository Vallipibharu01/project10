from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_Topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
        return HttpResponse('done')
            
    return render(request,'insert_Topic.html',d)

def insert_webpage(request):
    EWFO=webpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=webpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            e=WFDO.cleaned_data['email']
            u=WFDO.cleaned_data['url']
            WO=webpage.objects.get_or_create(topic_name=TO,name=n,email=e,URL=u)[0]
            WO.save()
        return HttpResponse('successfull')


    return render(request,'insert_webpage.html',d)

def insert_AccessRecord(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            n=AFDO.cleaned_data['name']
            WO=webpage.objects.get(pk=n)
            d=AFDO.cleaned_data['date']
            a=AFDO.cleaned_data['author']
            AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
            AO.save()
        return HttpResponse('successfully done')
    return render(request,'insert_AccessRecord.html',d)