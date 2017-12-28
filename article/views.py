from django.shortcuts import render
from django.shortcuts import redirect
from article.models import Article as articlemodel
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.


# def home(req):
#     post_list = articlemodel.objects.all().reverse()
#     print(post_list)
#     return render(req,'home.html',{'post_list' : post_list})

def home(req):
    posts = articlemodel.objects.all()
    paginator = Paginator(posts,2)
    page = req.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.page(paginator.num_pages)
    return render(req,'home.html',{'post_list' : post_list})


def detail(req,id):
    try:
        post = articlemodel.objects.get(id=str(id))
    except articlemodel.DoesNotExist:
        raise Http404
    return render(req,'article_content.html',{'post' : post})

def searchtag(req,tag):
    try:
        post_list = articlemodel.objects.filter(tag = tag).reverse()
        print(post_list)
    except articlemodel.DoesNotExist:
        raise Http404
    return render(req,'tag.html',{'post_list' : post_list})

def blog_search(req):
    if 's' in req.GET:
        print('s')
        s = req.GET['s']
        print(s)
        if not s :
            return render(req,'home.html')
        else:
            post_list = articlemodel.objects.filter(title__icontains=s)
            if len(post_list) == 0 :
                return render(req,'search.html',{'post_list':post_list,'error':True})
            else:
                return render(req,'search.html',{'post_list':post_list,'error':False})


    return redirect('/')


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return articlemodel.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self,item):
        return item.date_time

    def item_description(self, item):
        return item.content

