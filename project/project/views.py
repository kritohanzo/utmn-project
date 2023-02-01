from django.shortcuts import render

def page_not_found_view(request, exception):
	template = 'project/404.html'
	return render(request, template, status=404)

def robots(request):
	return render(request, 'project/robots.txt', content_type="text/plain")

def sitemap(request):
	return render(request, 'project/sitemap.xml', content_type="text/plain")