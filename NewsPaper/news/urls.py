from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostEdit, PostDelete, PostSearch

urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostEdit.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('create/', PostCreate.as_view(), name='articles_create'),
   path('<int:pk>/edit/', PostEdit.as_view(), name='articles_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
   path('search', PostSearch.as_view(), name='search')
]