from django.urls import path
from . import views


app_name="articles"
urlpatterns = [
    path('',views.index,name='index'),
    path('create/<int:movie_pk>/',views.create,name='create'),
    path('<int:article_pk>/',views.detail,name='detail'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/comments/', views.create_comment, name='create_comment'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:article_pk>/like/', views.like, name='like'),

]
