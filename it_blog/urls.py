"""it_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main_app.views import *
from newsApp.views import *
from django.conf import settings
from django.conf.urls.static import static
from userManagementApp.views import *
from adminApp.views import *
from django.conf.urls import include, url

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$',main),
    url(r'^smartphone$', smartphone ,name = 'smartphone'),
    url(r'^programm$', programm,name = 'programm'),
    url(r'^computer$', computer ,name = 'computer'),
    url(r'new/(\d+)$', full_news, name='news_detail'),

    url(r'^user/login/$',login),
    url(r'^user/logout/$',logout),
    url(r'^user/registration/$', registration),
    #url(r'^admin/$', admin_page, name='admin_users'),
    #url(r'^admin/delete/user/(\d+)$', delete_user),
    #url(r'^admin/get_user_form/(\d+)$', get_user_form),
    #url(r'^admin/create/user/(\d*)$', create_user),


]

urlpatterns += [
    url(r'admin/news/$', admin_news, name='admin_news'),
    url(r'^admin/create/news$', admin_news_create, name='news_create'),
    url(r'^admin/delete/news/(\d+)$', admin_news_delete, name='news_delete'),
    url(r'^admin/update/news/(\d+)$', admin_news_update, name='news_update'),
    url(r'^admin/detail/news/(\d+)$', admin_news_detail, name='news_detail_admin')
]
urlpatterns += [
    url(r'admin/news_short/$', admin_news_short, name='admin_news_short'),
    url(r'^admin/create/news_short$', admin_news_create_short, name='news_create_short'),
    url(r'^admin/delete/news_short/(\d+)$', admin_news_delete_short, name='news_delete_short'),
    url(r'^admin/update/news_short/(\d+)$', admin_news_update_short, name='news_update_short'),
    url(r'^admin/detail/news_short/(\d+)$', admin_news_detail_short, name='news_detail_admin_short')
]




if settings.DEBUG:
    #static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
