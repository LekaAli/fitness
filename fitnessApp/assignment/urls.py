from django.conf.urls import url
from . import views

app_name = 'assignment'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^add/',views.add_assignment,name='add'),
    url(r'^(?P<pk>[0-9]+)/view/$',views.RetrieveAssignentView.as_view(),name='view'),
    url(r'^(?P<pk>[0-9]+)/edit/$',views.EditAssignentView.as_view(),name='edit'),
    url(r'^(?P<pk>[0-9]+)/detail/$',views.DetailAssignmentView.as_view(),name='detail'),
    url(r'^(?P<assignment_id>[0-9]+)/update/$',views.update_assignment,name='update'),
    url(r'(?P<pk>[0-9]+)/delete/$',views.delete_assignment,name='delete'),
]
