from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    
    class Meta:
        ordering = ('pk',)
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = "category"
        verbose_name_plural = "categories"
        
    def __str__(self) -> str:
        return self.name

    

class Post(models.Model):
    category = models.ForeignKey(Category, 
                                 on_delete=models.CASCADE,
                                 related_name='posts'
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at',)
        indexes = [
            models.Index(fields=['-created_at'])
        ]
