"""tmsquare_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.post_list, name="post_list"),
    url(r'^blog/', include(('blog.urls', 'blog'), namespace='blog')),
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^logout/$', views.user_logout, name="user_logout"),
    url(r'^register/$', views.register, name="register"),

    # Password reset Url's
    
    #url(r'^password-reset/$', auth_views.password_reset, name="password_reset"),
    #url(r'^password-reset/done$', auth_views.password_reset_done, name="password_reset_done"),
    #url(r'^password-reset/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)/$', auth_views.password_reset_confirm, name="password_reset_confirm"),
    #url(r'^password-reset/complete/$', auth_views.password_reset_complete, name="password_reset_complete"),
    
    #or instead
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^oauth/', include('social_django.urls',namespace="social")),
    url(r'^like/$', views.like_post, name="like_post"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)