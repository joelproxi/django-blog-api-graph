
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from blog.models import Category, Post


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'posts',]
        interfaces = (relay.Node,)
        
        
class PostNode(DjangoObjectType):
    class Meta:
        model = Post
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith', ],
            'author': ['exact'],
            'category': ['exact'],
            'category__name': ['exact', 'icontains']
        }
        interfaces = (relay.Node,)
      

class Query(ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)
    
    post = relay.Node.Field(PostNode)
    all_posts = DjangoFilterConnectionField(PostNode)
    