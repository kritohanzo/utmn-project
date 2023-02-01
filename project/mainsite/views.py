from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'mainsite/index.html'
    return render(request, template)

def about_me(request):
    template = 'mainsite/about_me.html'
    return render(request, template)

def about_my_cat(request):
    template = 'mainsite/about_my_cat.html'
    return render(request, template)

def about_my_university(request):
    template = 'mainsite/about_my_university.html'
    return render(request, template)

def about_my_friend(request):
    template = 'mainsite/about_my_friend.html'
    return render(request, template)

def calendar(request):
    template = 'mainsite/calendar.html'
    return render(request, template)