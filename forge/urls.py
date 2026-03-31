from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.render_index, name='index'),
    path('our_space', views.render_index, name='our_space'),
    path('status', views.render_status, name='status'),
    path('news', views.render_news, name='news'),
    path('hours', views.render_hours, name='hours'),
    

    
    #chat is handled in myforge for now
    
    #path('chat', myforge.views.user_chat_join, name='chat'),
    

    
    path('', include("myforge.urls")),
    path('', include("machine_usage.urls")),
    path('', include("user_management.urls")),
    path('', include("apis.urls"))
    ]



urlpatterns += staticfiles_urlpatterns()
