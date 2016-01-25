from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post

def post_create(request):

	return HttpResponse("<h1>Create</h1>")

def post_detail(request, id):

	# Post.objects.get(id=2)
	instance = get_object_or_404(Post, id=id)

	context = {
		"title": instance.title,
		"obj" : instance.content,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset = Post.objects.all()
	if request.user.is_authenticated():
	# return HttpResponse("<h1>List</h1>")
		context = {
			"objectlist" : queryset,
			"title": "List"
		}
	else:
		context = {
			"title": "List but not auth"
		}
	return render(request, "index.html", context)


def post_update(request):

	return HttpResponse("<h1>Update</h1>")

def post_delete(request):

	return HttpResponse("<h1>Delete</h1>")