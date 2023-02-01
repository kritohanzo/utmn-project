from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

# Create your models here.

User = get_user_model()

class Post(models.Model):
	title = models.CharField(max_length=42, verbose_name='Заголовок')
	text = models.TextField(max_length=420, verbose_name='Текст')
	pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
	is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
	is_deleted = models.BooleanField(default=False, verbose_name='Удалено')

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'

class Comment(models.Model):
	text = models.TextField(max_length=420, verbose_name='Текст')
	pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author', verbose_name='Автор')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post', verbose_name='Пост')
	is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
	is_deleted = models.BooleanField(default=False, verbose_name='Удалено')
	
	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'

        