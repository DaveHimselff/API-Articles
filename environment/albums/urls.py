from django.urls import path
from .views import (
   TagListCreateView, TagUpdateView, TagDeleteView, CategoryListCreateView, CategoryUpdateView, CategoryDeleteView,
   ArticleListCreateView, ArticleUpdateView, ArticleDeleteView 
)
 
urlpatterns = [
    #tag
     path('articles/tags/', TagListCreateView.as_view(), name = 'tag-list-create'),
     path('articles/tags/<int:id>/', TagUpdateView.as_view(), name='tag-update'),
     path('delete/articles/tags/<int:id>/', TagDeleteView.as_view(), name='tag-delete'),


     #Category
     path('articles/category/',CategoryListCreateView.as_view(), name='category-list-create'),
     path('articles/category/<int:id>/', CategoryUpdateView.as_view(), name='category-update'),
     path('delete/articles/category/<int:id>/', CategoryDeleteView.as_view(), name='category-delete'),
      

     #Articles
     path('articles/',ArticleListCreateView.as_view(), name='Article-list-create'),
     path('articles/<int:id>/',ArticleUpdateView.as_view(), name='Article-update'),
     path('delete/articles/<int:id>/', ArticleDeleteView.as_view(), name='Article-delete')

   
]