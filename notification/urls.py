"""notification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
# from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from notificationApp import views
from notificationApp.views import contactView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    # esta linea es para si no pones el login html dentro de registration
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # esta linea es para cuando pones el login html dentro de registration
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    path('accounts/', views.accountProfile, name='accounts'),
    path('accounts/red', views.classificationIncidentsInRed, name='red'),
    path('accounts/security', views.classificationIncidentsInSecurity, name='security'),
    path('accounts/yes', views.revisedIncidentsYes, name='yes'),
    path('accounts/no', views.revisedIncidentsNo, name='no'),
    path('accounts/search', views.search, name='search'),
    path('contact/', contactView.as_view(), name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)