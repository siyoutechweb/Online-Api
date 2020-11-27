"""Online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from shopApp import views as v1
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.show_home_client),
    path('main2',v1.show_main2),
    # path('main3',v1.product_list3),
    path('cart/', include('cart.urls', namespace='cart')),
    path('shopApp/', include('shopApp.urls', namespace='shopApp')),
    # path('login/',v1.show_login),
    path('account/', include('account.urls')),
    path('social-auth/',include('social_django.urls', namespace='social')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('comments/', include('django_comments.urls')),
    path('home_client/',v1.show_home_client),
    path('contact/',v1.show_contact),
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/', include('shopApp.api.urls', namespace='api')),
    #path('api/auth/', include('djoser.urls.authtoken')),
    path('api/rest/', include('rest_registration.api.urls')),


    path('api/account/', include('account.api.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
