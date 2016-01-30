#try
# -*- coding: utf-8 -*-
"""from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Document
from .forms import DocumentForm
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('blog.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'blog/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
"""
# end try

from django.http import *
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Post
from .forms import PostForm, CommentForm
import os

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

@login_required
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request, 'blog/post_draft_list.html', {'posts':posts})

@login_required(login_url='/login/')
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)

@login_required(login_url='/login/')
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def under_maintain(request):
	return render(request, 'blog/under_maintain.html',{})

@login_required(login_url='/login/')
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.created_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

@login_required(login_url='/login/')
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)

	if request.method == "POST":		
		form = PostForm(request.POST, request.FILES,instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.created_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

#try login
def login_user(request):
    logout(request)
    username = password = ''

    next = ""

    if request.GET:  
        next = request.GET['next']
		
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            
            if user.is_active:
                login(request, user)
                if next == "":
                    return redirect('blog.views.post_list')
                else:
                    return HttpResponseRedirect(next)
    return render_to_response('registration/login.html', {'next':next}, context_instance=RequestContext(request))


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
#        form = CommentForm()
#    return render(request, 'blog/add_comment_to_post.html', {'form': form})
      return redirect('blog.views.post_detail', pk=post.pk)
"""
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = Post(wallpaper = request.FILES['wallpaper'])
			post.title = request.POST['title']
			post.text	 = request.POST['text']
			post.author = request.user
			post.created_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})
"""

"""
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	data = {'title':post.title, 'text':post.text, 'wallpaper': SimpleUploadedFile('docker.png', 'image')}

	if request.method == "POST":		
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post.title = request.POST['title']
			post.text	 = request.POST['text']
			post.wallpaper = request.FILES['wallpaper']
			post.author = request.user
			post.created_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(data)
	return render(request, 'blog/post_edit.html', {'form': form})
"""


