from django.conf.urls import url
import system.views
# SET THE NAMESPACE!
app_name = 'system'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',system.views.register,name='register'),
    url(r'^user_login/$',system.views.user_login,name='user_login'),
]