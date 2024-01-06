from django import forms
from app.models import *

class TopicForm(forms.Form):
    topic_name=forms.CharField()

class webpageForm(forms.Form):
    tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    topic_name=forms.ChoiceField(choices=tl)
    name=forms.CharField()
    email=forms.EmailField()
    url=forms.URLField()

class AccessRecordForm(forms.Form):
    al=[[ao.pk,ao.name] for ao in webpage.objects.all()]
    name=forms.ChoiceField(choices=al)
    date=forms.DateField()
    author=forms.CharField()