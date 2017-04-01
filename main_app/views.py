

from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.http import Http404
from .models import *
from userManagementApp.forms import MyRegistrationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def main(request):
    news_list =  News.objects.order_by('id')

    news_list = news_list.reverse()
    paginator = Paginator(news_list, 6)

    page = request.GET.get('page')

    try:
        news_l = paginator.page(page)
    except PageNotAnInteger:
        news_l= paginator.page(1)

    except EmptyPage:
        news_l = paginator.page(paginator.num_pages)


    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form': form,
                   'news': news_l,
                   "contacts": news_l}
        return render(request, 'index.html', context)
    context = {'form': MyRegistrationForm(),
               'news': news_l,
               "contacts": news_l}
    return render(request, 'index.html', context)


def smartphone(request):
    news_list = News.objects.order_by('id')
    news_list = news_list.reverse()
    news_list = news_list.filter(type_news = '3')
    paginator = Paginator(news_list, 6)

    page = request.GET.get('page')

    try:
        news_l = paginator.page(page)
    except PageNotAnInteger:
        news_l= paginator.page(1)

    except EmptyPage:
        news_l = paginator.page(paginator.num_pages)


    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form': form,
                   'news': news_l,
                   "contacts": news_l}
        return render(request, 'index.html', context)
    context = {'form': MyRegistrationForm(),
               'news': news_l,
               "contacts": news_l}
    return render(request, 'index.html', context)
def programm(request):
    news_list = News.objects.order_by('id')
    news_list = news_list.filter(type_news = '1')
    news_list = news_list.reverse()
    paginator = Paginator(news_list, 6)
    page = request.GET.get('page')


    try:
        news_l = paginator.page(page)
    except PageNotAnInteger:
        news_l= paginator.page(1)
    except EmptyPage:
        news_l = paginator.page(paginator.num_pages)


    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form': form,
                   'news': news_l,
                   "contacts": news_l}
        return render(request, 'index.html', context)
    context = {'form': MyRegistrationForm(),
               'news': news_l,
               "contacts": news_l}
    return render(request, 'index.html', context)
def computer(request):
    news_list = News.objects.order_by('id')
    news_list = news_list.filter(type_news = '2')
    news_list = news_list.reverse()
    paginator = Paginator(news_list, 6)
    page = request.GET.get('page')

    try:
        news_l = paginator.page(page)
    except PageNotAnInteger:
        news_l= paginator.page(1)
    except EmptyPage:
        news_l = paginator.page(paginator.num_pages)


    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form': form,
                   'news': news_l,
                   "contacts": news_l}
        return render(request, 'index.html', context)
    context = {'form': MyRegistrationForm(),
               'news': news_l,
               "contacts": news_l}
    return render(request, 'index.html', context)

def login(request):
    if request.method == 'POST':
        print('Post data=',request.POST)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/')
        else:
            return render(request,'error.html',{'username':username,'errors':True})
    raise Http404
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')



