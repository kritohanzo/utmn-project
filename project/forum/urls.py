from django.urls import path
from . import views
from .views import PostCreate, PostDetail

app_name = 'forum'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail_url'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name="logout"),
    path('stopped_posts/', views.stopped_posts, name="stopped_posts"),
    path('deleted_posts/', views.deleted_posts, name="deleted_posts"),
    path('post/<int:pk>/accept/', views.accept_post, name="accept_post"),
    path('post/<int:pk>/delete/', views.delete_post, name="delete_post"),
    path('post/<int:pk>/restore/', views.restore_post, name="restore_post"),
    path('post/<int:pk>/on_moderate/', views.on_moderate_post, name="on_moderate_post"),
    path('stopped_comments/', views.stopped_comments, name="stopped_comments"),
    path('deleted_comments/', views.deleted_comments, name="deleted_comments"),
    path('comment/<int:pk>/accept/', views.accept_comment, name="accept_comment"),
    path('comment/<int:pk>/delete/', views.delete_comment, name="delete_comment"),
    path('comment/<int:pk>/restore/', views.restore_comment, name="restore_comment"),
    path('comment/<int:pk>/on_moderate/', views.on_moderate_comment, name="on_moderate_comment"),

]