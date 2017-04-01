from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from userManagementApp.forms import MyRegistrationForm, UserChangeForm
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from main_app.views import *
from newsApp.views import *
from newsApp.form import *

def admin_page(request):
    users = User.objects.all()
    user_form = MyRegistrationForm()

    return render(request, 'admin_page.html', {'users': users, 'form': user_form})



def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin')


def get_user_form(request, user_id):
    """
    Возвращает заполненную форму для редактирования Пользователя(User) с заданным user_id
    """
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = MyRegistrationForm(instance=user)
        context = {'form': user_form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-registration_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


def create_user(request, user_id=None):
    """
    Создает Пользователя(User)
    Или редактирует существующего, если указан  user_id
    """
    if request.is_ajax():

        if not user_id:

            user = UserChangeForm(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            user = UserChangeForm(request.POST or None, instance=user)
        if user.is_valid():
            user.save()
            users = User.objects.all()
            html = loader.render_to_string('inc-users_list.html', {'users': users}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user.errors.as_json()
            return JsonResponse({'errors': errors})

    raise Http404
#------------------Длинная новость----------------------
def admin_news(request):
    news = Full_news.objects.all()
    return render(request, 'admin_news.html', {'news': news})


def admin_news_create(request):
    if request.method == 'POST':
        form = Full_newsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/news/')
        context = {'form': form}
        return render(request, 'admin_news_create.html', context)
    context = {'form': Full_newsForm()}
    return render(request, 'admin_news_create.html', context)


def admin_news_delete(request, id):
    news = get_object_or_404(Full_news, id=id)
    news.delete()
    return HttpResponseRedirect('/admin/news/')


def admin_news_update(request, id):
    news = get_object_or_404(Full_news, id=id)
    if request.method == 'POST':

        form = Full_newsForm(request.POST, request.FILES,instance=news)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/admin/news/')
        context = {'form': form  }
        return render(request, 'admin_news_update.html', context)
    context = {'form': Full_newsForm(instance=news)}
    return render(request, 'admin_news_update.html', context)

def admin_news_detail(request, id):
    news = get_object_or_404(Full_news, id=id)
    return render(request, 'admin_news_detail.html', {'news':news})

#--------------------------------Короткая новость--------------------
def admin_news_short(request):
    news = News.objects.all()
    return render(request, 'admin_news_short.html', {'news': news,'short': True})


def admin_news_create_short(request):
    if request.method == 'POST':
        form = NewsForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()

            return HttpResponseRedirect('/admin/news_short/')
        context = {'form': form}
        return render(request, 'admin_news_create.html', context)
    context = {'form': NewsForm()}
    return render(request, 'admin_news_create.html', context)


def admin_news_delete_short(request, id):
    news = get_object_or_404(News, id=id)
    news.delete()
    return HttpResponseRedirect('/admin/news_short/')


def admin_news_update_short(request, id):
    news = get_object_or_404(News, id=id)
    if request.method == 'POST':
        form = NewsForm(request.POST,request.FILES,instance=news)
        if form.is_valid():

            form.save()
            return HttpResponseRedirect('/admin/news_short/')
        context = {'form': form}
        return render(request, 'admin_news_update.html', context)
    context = {'form': NewsForm(instance=news)}
    return render(request, 'admin_news_update.html', context)

def admin_news_detail_short(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'admin_news_detail.html', {'short':news,'news':False})

