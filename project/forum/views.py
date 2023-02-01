from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import NewUserForm, PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views.generic import View
import time
import datetime
from .token import token
from .telegram_send import send_telegram
from django.shortcuts import get_object_or_404
import os

# Create your views here.

ban_words = ('архипиздрит басран бздение бздеть бздех бзднуть бздун бздунья '
			 'бздюха бикса блежник блудилище бляд блябу блябуду блядун блядунья '
			 'блядь блядюга взьебка волосянка взьебывать взьебывать выблядок '
			 'выблядыш выебать выеть выпердеть высраться выссаться говенка '
			 'говенный говешка говназия говнецо говно говноед говночист говнюк '
			 'говнюха говнядина говняк говняный говнять гондон дермо долбоеб дрисня '
			 'дрист дристать дристануть дристун дристуха дрочена дрочила дрочилка дрочить '
			 'дрочка ебало ебальник ебануть ебаный ебарь ебатория ебать ебаться ебец '
			 'ебливый ебля ебнуть ебнуться ебня ебун елда елдак елдачить заговнять '
			 'задристать задрока заеба заебанец заебать заебаться заебываться заеть '
			 'залупа залупаться залупить залупиться замудохаться засерун засеря засерать засирать '
			 'засранец засрун захуячить злоебучий изговнять изговняться кляпыжиться курва '
			 'курвенок курвин курвяжник курвяжница курвяжный манда мандавошка мандей мандеть '
			 'мандища мандюк минет минетчик минетчица мокрохвостка мокрощелка мудак муде мудеть '
			 'мудила мудистый мудня мудоеб мудозвон муйня набздеть наговнять надристать надрочить '
			 'наебать наебнуться наебывать нассать нахезать нахуйник насцать обдристаться '
			 'обдристаться обосранец обосрать обосцать обосцаться обсирать опизде отпиздячить '
			 'отпороть отъеть охуевательский охуевать охуевающий охуеть охуительный охуячивать '
			 'охуячить педрик пердеж пердение пердеть пердильник перднуть пердун пердунец пердунина '
			 'пердунья пердуха пердь передок пернуть пидор пизда пиздануть пизденка пиздеть пиздить пиздища '
			 'пиздобратия пиздоватый пиздорванец пиздорванка пиздострадатель пиздун пиздюга пиздюк '
			 'пиздячить писять питишка плеха подговнять подъебнуться поебать поеть попысать посрать '
			 'поставить поцоватый презерватив проблядь проебать промандеть промудеть пропиздеть '
			 'пропиздячить пысать разъеба разъебай распиздай распиздеться распиздяй распроеть растыка '
			 'сговнять секель серун серька сика сикать сикель сирать сирывать скурвиться скуреха скурея '
			 'скуряга скуряжничать спиздить срака сраный сранье срать срун ссака ссаки ссать старпер '
			 'струк суходрочка сцавинье сцака сцаки сцание сцать сциха сцуль сцыха сыкун титечка '
			 'титечный титка титочка титька трипер триппер уеть усраться усцаться фик фуй хезать '
			 'хер херня херовина херовый хитрожопый хлюха хуевина хуевый хуек хуепромышленник '
			 'хуерик хуесос хуище хуй хуйня хуйрик хуякать хуякнуть целка шлюха лох дебил дурак'
			 'сука ублюдок тварь блять ебать хуй пизда')

# users_online = {
# 
# }

# def delete_online(request):
# 	users_online[f'{request.user.username}'] = datetime.datetime.now()
# 	for user in users_online.keys():
# 		if int(str(datetime.datetime.now()).split(' ')[1].split(':')[1]) - 5 == int(str(users_online[user]).split(' ')[1].split(':')[1]):
# 			users_online.pop(user)

def index(request):
	template = 'forum/index.html'
	posts = Post.objects.order_by('-pub_date')
	# delete_online(request)
	context = {
	    'posts': posts
	}
	return render(request, template, context)

def stopped_posts(request):
	template = 'forum/stopped_posts.html'
	posts = Post.objects.order_by('-pub_date')
	context = {
        'posts': posts
    }
	return render(request, template, context)

def deleted_posts(request):
	template = 'forum/deleted_posts.html'
	posts = Post.objects.order_by('-pub_date')
	context = {
        'posts': posts
    }
	return render(request, template, context)

def stopped_comments(request):
	template = 'forum/stopped_comments.html'
	comments = Comment.objects.order_by('-pub_date')
	context = {
        'comments': comments
    }
	return render(request, template, context)

def deleted_comments(request):
	template = 'forum/deleted_comments.html'
	comments = Comment.objects.order_by('-pub_date')
	context = {
        'comments': comments
    }
	return render(request, template, context)

def accept_post(request, pk):
	if request.user.is_superuser: 
		post = Post.objects.get(pk=pk)
		post.is_published = True
		post.save()
		return redirect('forum:post_detail_url', pk=pk)
	else:
		messages.error(request, "Данная возможность предусмотрена только администраторам.")
		return redirect('forum:index')

def delete_post(request, pk):
	if request.user.is_superuser: 
		post = Post.objects.get(pk=pk)
		post.is_deleted = True
		post.save()
		return redirect('forum:post_detail_url', pk=pk)
	else:
		messages.error(request, "Данная возможность предусмотрена только администраторам.")
		return redirect('forum:index')

def restore_post(request, pk):
	if request.user.is_superuser: 
		post = Post.objects.get(pk=pk)
		post.is_deleted = False
		post.save()
		return redirect('forum:post_detail_url', pk=pk)
	else:
		messages.error(request, "Данная возможность предусмотрена только администраторам.")
		return redirect('forum:index')

def on_moderate_post(request, pk):
	if request.user.is_superuser: 
		post = Post.objects.get(pk=pk)
		post.is_published = False
		post.save()
		return redirect('forum:post_detail_url', pk=pk)
	else:
		messages.error(request, "Данная возможность предусмотрена только администраторам.")
		return redirect('forum:index')

def accept_comment(request, pk):
	if request.user.is_superuser: 
		comment = Comment.objects.get(pk=pk)
		comment.is_published = True
		comment.save()
		return redirect('forum:post_detail_url', pk=comment.post.pk)
	else:
		messages.error(request, "Данная возможность предусмотрена только администраторам.")
		return redirect('forum:index')

def delete_comment(request, pk):
	if request.user.is_superuser: 
		comment = Comment.objects.get(pk=pk)
		comment.is_deleted = True
		comment.save()
		return redirect('forum:post_detail_url', pk=comment.post.pk)
	else:
		messages.error(request, "Данная возможность предусмотрена только администраторам.")
		return redirect('forum:index')

def restore_comment(request, pk):
	if request.user.is_superuser: 
		comment = Comment.objects.get(pk=pk)
		comment.is_deleted = False
		comment.save()
		return redirect('forum:post_detail_url', pk=comment.post.pk)
	else:
		messages.error(request, "Данная возможность предусмотрена только администраторам.")
		return redirect('forum:index')

def on_moderate_comment(request, pk):
	if request.user.is_superuser: 
		comment = Comment.objects.get(pk=pk)
		comment.is_published = False
		comment.save()
		return redirect('forum:post_detail_url', pk=comment.post.pk)
	else:
		messages.error(request, "Данная возможность предусмотрена только администраторам.")
		return redirect('forum:index')


class PostDetail(View):
	def get(self, request, pk):
		post = get_object_or_404(Post, pk__iexact=pk)
		comments = post.comment_post.all()
		form = CommentForm()
		return render(request, 'forum/post_detail.html', context={'post': post, 'comments': comments, 'form': form})
	def post(self, request, pk):
		if not request.user.id:
			return redirect('forum:login')
		post = Post.objects.get(pk__iexact=pk)
		comments = post.comment_post.all()
		for word in str(request.POST['text']).lower().split(' '):
			if word in ban_words.split(' '):
				request.POST._mutable = True
				request.POST['is_published'] = False
				request.POST._mutable = False
		request.POST._mutable = True
		request.POST['author'] = str(request.user.id)
		request.POST['post'] = str(post.pk)
		request.POST._mutable = False
		bound_form = CommentForm(request.POST)
		if bound_form.is_valid():
			new_comment = bound_form.save()
			if new_comment.is_published == True:
				text_for_tg = f'В посте #{new_comment.post.pk} новый комментарий\nАвтор: {new_comment.author}\nТекст комментария: {new_comment.text}\nСсылка на пост: kritohanzo.ru/forum/post/{new_comment.post.pk}'
			else:	
				text_for_tg = f'В посте #{new_comment.post.pk} новый комментарий\nАвтор: {new_comment.author}\nТекст комментария: {new_comment.text}\n\nТРЕБУЕТСЯ МОДЕРАЦИЯ!!!\n\nСсылка на пост: kritohanzo.ru/forum/post/{new_comment.post.pk}'
			send_telegram(text_for_tg)
			return redirect('forum:post_detail_url', pk=pk)
		return render(request, 'forum/post_detail.html', context={'form': bound_form, 'comments': comments, 'post':post})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		nick = str(form)
		nick = nick.split('value="')
		nick = nick[1]
		nick = nick.split('"')
		nick = nick[0]
		if len(nick) > 16:
			messages.error(request, "Максимальная длина ника - 16 символов.")
			return redirect("forum:register")
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Регистрация успешна." )
			text_for_tg = f'На форуме зарегистрировался новый пользователь\nНик: {user.username}'
			send_telegram(text_for_tg)
			return redirect("forum:index")
		messages.error(request, "Регистрация не успешна. Вы ввели не правильные данные. Убедитесь, что в вашем пароле есть как минимум 1 цифра и он не общедоступный.")
		return redirect("forum:register")
	form = NewUserForm()
	return render (request=request, template_name="forum/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Вы вошли в аккаунт {username}.")
				return redirect("forum:index")
			else:
				messages.error(request,"Неверный логин или пароль.")
		else:
			messages.error(request,"Неверный логин или пароль.")
	form = AuthenticationForm()
	return render(request=request, template_name="forum/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, f"Вы успешно вышли с аккаунта.") 
	return redirect("forum:index")

class PostCreate(View):
	def get(self, request):
		if request.user.id:
			form = PostForm()
			return render(request, 'forum/create_post.html', context={'form': form})
		return redirect('forum:login')

	def post(self, request):
		for word in str(request.POST['title']).lower().split(' '):
			if word in ban_words.split(' '):
				request.POST._mutable = True
				request.POST['is_published'] = False
				request.POST._mutable = False
		for word in str(request.POST['text']).lower().split(' '):
			if word in ban_words.split(' '):
				request.POST._mutable = True
				request.POST['is_published'] = False
				request.POST._mutable = False
		request.POST._mutable = True
		request.POST['author'] = str(request.user.id)
		request.POST._mutable = False
		bound_form = PostForm(request.POST)
		if bound_form.is_valid():
			new_post = bound_form.save()
			if new_post.is_published == False:
				text_for_tg = f'На форуме создали новый пост #{new_post.pk}\nЗаголовок поста: {new_post.title}\nТекст поста: {new_post.text}\nАвтор: {new_post.author}\n\nТРЕБУЕТСЯ МОДЕРАЦИЯ!!!\n\nСсылка на пост: kritohanzo.ru/forum/post/{new_post.pk}'
			else:
				text_for_tg = f'На форуме создали новый пост #{new_post.pk}\nЗаголовок поста: {new_post.title}\nТекст поста: {new_post.text}\nАвтор: {new_post.author}\nСсылка на пост: kritohanzo.ru/forum/post/{new_post.pk}'
			send_telegram(text_for_tg)
			return redirect('forum:post_detail_url', pk=new_post.pk)
		return render(request, 'forum/create_post.html', context={'form': bound_form})