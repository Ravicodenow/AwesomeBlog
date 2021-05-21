

from django.urls import path
#from . import  views
from .views import HomeView, ArticleDetailView, AddPostView,  UpdatePostView, DeletePostView, AddCommentView
urlpatterns = [
    #path('',views.home, name="home"),
    path('', HomeView.as_view(), name ="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>',  UpdatePostView.as_view(), name='update_post'),
    path('article/edit/<int:pk>/remove',  DeletePostView.as_view(), name='delete_post'),
    path('article/<int:pk>/comment/',  AddCommentView.as_view(), name='add_comment'),
   
]
