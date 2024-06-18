from django.urls import path

from .import views

urlpatterns = [
    path("article/",views.getAllArticle),
    path("article/<slug:slug>",views.getArticle_by_slug),
    
    path("post/",views.getRecentPosts),
    

    path("category/",views.getAllCategory),
    path("category/<str:name>",views.getArticle_by_category),
   
]
