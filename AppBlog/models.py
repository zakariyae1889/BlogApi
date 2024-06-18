from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify



class  Category (models.Model):
    name=models.CharField(max_length=255)
    create=models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Blog(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField(max_length=10000)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='blogs')
    
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blogs")
    slug=models.SlugField(null=True,blank=True,unique=True)
    create=models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now_add=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
            super(Blog,self).save(*args, **kwargs)

    def __str__(self):
        return self.title
class Comment(models.Model):

    name=models.CharField(max_length=255)
    Email=models.EmailField(max_length=255,blank=True,null=True ,unique=True)
    content=models.TextField(max_length=10000)
    active=models.BooleanField(default=False)
    post=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments")
    create=models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.post.title

    

    

   
    

   

    

   
   
    

