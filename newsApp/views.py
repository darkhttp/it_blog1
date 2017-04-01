from django.shortcuts import render, HttpResponseRedirect,get_object_or_404

from newsApp.models import *
from main_app.models import *
# Create your views here.
def full_news(request,id):
    news = get_object_or_404(Full_news, id=id)
    return render(request, 'news.html',{'f_nw':news})
