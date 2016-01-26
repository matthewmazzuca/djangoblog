from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import PostForm
from .models import Post

def post_create(request):

	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully created Post")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Something went wrong")

	# below is not robust
	# if request.method == "POST":
	# 	print request.POST.get("content")
	# 	print request.POST.get("title")
		# Posts.objects.Create()


	context = {
		"form" : form,

	}

	return render(request, "post_form.html", context)

def post_detail(request, id):

	# Post.objects.get(id=2)
	instance = get_object_or_404(Post, id=id)

	context = {
		"title": instance.title,
		"instance" : instance,
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
	return render(request, "base.html", context)


def post_update(request, id=None):

	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# success message
		messages.success(request, "Success")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance" : instance,
		"form":form,
	}
	return render(request, "post_form.html", context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")
