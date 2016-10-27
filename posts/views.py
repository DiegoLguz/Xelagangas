from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView


def post_login(request):
    return render(request,"index.html")


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request,"post_form.html",context)

def post_detail(request,id=None):
    instance = get_object_or_404(Post,id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request,"post_detail.html",context)

def post_list(request):
    queryset_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list, 5) 
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:    
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    if request.user.is_authenticated():
        context = {
            "object_list": queryset,
            "title": "XelaGangas"
        }
    else:
        context = {
            "title": "Inicie sesion para ver la lista de articulos"
        }
    return render(request,"post_list.html",context)



def post_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request,"post_form.html",context)

def post_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect("list")