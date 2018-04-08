from django.conf.urls import url
from . import views
        
#0861201000

app_name = 'institution'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^add/$',views.add_institution,name='add'),
    url(r'^(?P<pk>[0-9]+)/detail/$',views.DetailInstitutionView.as_view(),name='detail'),
    url(r'^(?P<pk>[0-9]+)/view/$',views.RetrieveInstitutionView.as_view(),name='view'),
    url(r'^(?P<pk>[0-9]+)/edit/$',views.EditInstitutionView.as_view(),name='edit'),
    url(r'^(?P<institution_id>[0-9]+)/update/$',views.update_institution,name='update'),
    url(r'^(?P<institution_id>[0-9]+)/delete/$',views.delete_institution,name='delete'),
]
