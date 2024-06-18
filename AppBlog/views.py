from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from .filter import BlogFilter
from rest_framework.pagination import PageNumberPagination
#---------------------getAllArticle---------------------#
@api_view(["GET"])
def getAllArticle(request):
    try:
    #query 
        article=Blog.objects.all().order_by("-create")
        
    #filter
        articleFilter=BlogFilter(request.GET,queryset=article)
    #paginate
        resPage=4
        paginator=PageNumberPagination()
        paginator.page_size=resPage
        articlePaginate=paginator.paginate_queryset(articleFilter.qs,request)

    except Blog.DoesNotExist:
        return Response(status=status.TTP_404_NOT_FOUND)
    #serializer
    serializer=BlogSerializer(articleFilter.qs,many=True)
  
    
   
   
    
    #Response
    return Response({
        "article":serializer.data,
      
        
        
    })
#-----------------------------------------------------------#
@api_view(["GET"])
def getRecentPosts(request):
    try:
        #query 
        article=Blog.objects.all().order_by("-create")[0:3]
        
    except Blog.DoesNotExist:
        return Response(status=status.TTP_404_NOT_FOUND)
    #serializer
    serializer=BlogSerializer(article,many=True)
    
    
    #Response
    return Response({
        "article":serializer.data,
        
         
        
    })
#---------------------getArticle_by_slug---------------------#
@api_view(["GET","POST"])
def getArticle_by_slug(request,slug):
    try:
    #query 
        article=get_object_or_404(Blog,slug=slug)
        #--------------------comment------------------#
        comments=article.comments.filter(active=True)
        data=request.data
        if request.method=="POST":
            comment=Comment.objects.create(
                name=data["name"],
                Email=data["Email"],
                content=data["content"],
                active=data["active"],
                post=article,
            )
            return Response({
               "details":"CommentAdd"
            })
    #serializer:
        #blog
        serializerblog=BlogSerializer(article,many=False)
        #comment
        serializercomment=CommentSerializer(comments,many=True)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #Response
    return Response({
        "article":serializerblog.data,
        "comment":serializercomment.data
    })
#--------------------- getAllCategory---------------------#
@api_view(["GET"])
def getAllCategory(request):
    try:
    #query
      category=Category.objects.all()
    #serializer
      serializer=CategorySerializer(category,many=True)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #Response
    return Response({
        "category":serializer.data
    })
#---------------------getArticle_by_category---------------------#
@api_view(["GET"])
def getArticle_by_category(request,name):
    try:
    #query
      category=Category.objects.get(name=name)
      article=Blog.objects.filter(category=category)
     

    #serializer
      serializer=BlogSerializer(article,many=True)
    
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #Response
    return Response({
        "article":serializer.data,
       
    })









