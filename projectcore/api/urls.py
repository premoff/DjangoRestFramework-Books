from django.urls import path
from .views import Booklist,additem,updateitem,deleteitem,RegisterUser#,listitem
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('',listitem,name='listitem'),
    path('register/',RegisterUser.as_view()),
    path('',Booklist.as_view(),name='booklist'),
    path('additem/',additem,name='additem'),
    path('updateitem/<str:pk>/',updateitem,name='updateitem'),
    path('delete/<str:pk>/',deleteitem,name='deleteitem'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
