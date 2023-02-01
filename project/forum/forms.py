from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment


# Create your forms here.

class NewUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user
	
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text', 'author', 'is_published')
		widgets = {
			'title': forms.TextInput(attrs={'placeholder': 'заголовок', 'class': 'text-center'}),
			'text': forms.TextInput(attrs={'placeholder': 'текст', 'class': 'text-center'}),
			'author': forms.HiddenInput(attrs={'class': 'form-control'}),
			'is_published': forms.HiddenInput(attrs={'class': 'form-control'})
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('text', 'author', 'post', 'is_published')
		widgets = {
			'text': forms.TextInput(attrs={'placeholder': 'текст', 'class': 'text-center'}),
            'author': forms.HiddenInput(attrs={'class': 'form-control'}),
            'post': forms.HiddenInput(attrs={'class': 'form-control'}),
			'is_published': forms.HiddenInput(attrs={'class': 'form-control'})
		}