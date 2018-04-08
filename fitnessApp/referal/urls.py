from django.conf.urls import url
from . import views

app_name = 'referal'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^add/$',views.add_referal,name='add'),
    url(r'^(?P<pk>[0-9]+)/detail/$',views.detail_referal.as_view(),name='detail'),
    url(r'^edit/$',views.edit_referal,name='edit'),
    url(r'^update/$',views.update_referal,name='update'),
    url(r'^check/$',views.check_referal,name='check'),
    url(r'^accept/$',views.accept_referal,name='accept'),
    url(r'^cancel/$',views.cancel_referal,name='cancel'),
]