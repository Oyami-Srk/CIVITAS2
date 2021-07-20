"""civitas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path
from . import views
from . import rspeech
from . import map
from django.conf.urls import include
from django.contrib.auth import views as loginViews
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.views),
    path('speech/', rspeech.rspeech),
    path('map.html', map.map),
    path('index.html',views.views),
]
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
    
# ]
urlpatterns += [
    path('login/',loginViews.LoginView.as_view(), name='login'),
    path('logout/',loginViews.LogoutView.as_view(), name='logout'),

    path('password-reset/', loginViews.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', loginViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', loginViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', loginViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]