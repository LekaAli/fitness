"""fitnessApp URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from . import views
# from patient import urls as patient
# from institution import urls as institution
# from referal import urls as referal
# from serviceprovider import urls as serviceprovider
# from availability import urls as availability
# from assignment import urls as assignment

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    # url(r'^patient/',include(patient),name='patient'),
    # url(r'^institution/',include(institution),name='institution'),
    # url(r'^referal/',include(referal),name='referal'),
    # url(r'^serviceprovider/',include(serviceprovider),name='serviceprovider'),
    # url(r'^availability/',include(availability),name='availability'),
    # url(r'^assignment/',include(assignment),name='assignment'),
]
