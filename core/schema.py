import graphene
from graphene_django import DjangoObjectType

import blog.schema
from blog.models import Category, Post


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'posts']
        
        
class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ['id', 
                  'title', 
                  'category', 
                  'created_at', 
                  'updated_at', 
                  'content', 
                  'author', ]
        
        
# class Query(graphene.ObjectType):
#     all_categories = graphene.List(CategoryType)
#     all_posts = graphene.List(PostType)
#     category_by_slug = graphene.Field(CategoryType,
#                                       slug=graphene.String(required=True))
#     post_by_id = graphene.Field(PostType, 
#                                 id=graphene.Int(required=True))
    
#     def resolve_all_categories(root, info):
#         return Category.objects.all()
    
#     def resolve_all_posts(root, info):
#         return Post.objects.select_related('category').all()
    
#     def resolve_category_by_slug(root, info, slug):
#         try:
#             return Category.objects.get(slug=slug)
#         except Category.DoesNotExist:
#             return None
        
#     def resolve_post_by_id(root, info, id):
#         try:
#             return Post.objects.select_related('category').get(id=id)
#         except Post.DoesNotExist:
#             return None
    
class Query(blog.schema.Query, graphene.ObjectType):
    pass

    
schema = graphene.Schema(query=Query)