from django.conf.urls import url, include

'''
this import is sort of special because 
I have imported 'views' as 'auth_views'
and these are different from standard 
'views.py' file which is an essential 
django project/app structure
--- 
from django.contrib.auth import views as auth_views

this will allow us create pages automatically
    - LOGIN
    - LOGOUT 
    
starting from django 1.11 we do not have to set up special
view in views.py for 'login/logout' purpose which is awesome!
---
'''
from django.contrib.auth import views as auth_views
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

app_name = "accounts"

urlpatterns = [

    url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'signup/$', views.SignUpToOurJKPortal.as_view(), name='signup'),
    url(r'documents/$', views.list_document, name='list_document'),
    url(r'^documents/(?P<pk>\d+)/remove/$', views.DocumentDeleteView.as_view(), name='remove_document'),
    url(r'^(?P<pk>\d+)/remove$', views.ProcessedDocumentDeleteView.as_view(), name='remove_processed_file'),
    url(r'select_process/$', views.SelectProcessView, name='select_process'),
    url(r'collect_templates/$', views.collect_templates, name='collect_templates'),
    url(r'generate_table/$', views.generate_table, name='generate_table')

]





