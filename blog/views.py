from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse

from .models import Post
from .forms import CommentsForm, EmailPostForm

# Create your views here.


def view_posts(request):
    blog_list = Post.objects.all().filter(published=True).order_by('-published_date')
    context = {
        'posts': blog_list
    }

    return render(request, 'blog/blog_list.html', context)



def post_detail(request, post_id):
    posts = get_object_or_404(Post, id=post_id)
    post_related = posts.tags.similar_objects()
    form = CommentsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
           form.instance.user = request.user
           form.instance.post = posts
           form.save()
           return redirect(reverse('blog:post_detail', args=[posts.id]))
        #    return redirect('post_detail', post_id=post_id)


    context = {
        'post': posts,
        'form': form,
        'related_post':post_related
    }

    return render(request, 'blog/blog_detail.html', context)



# def post_share(request, post_id):
#     post = get_object_or_404(Post, id=post_id, published=True)
#     sent = False
#     if request.method == 'POST':
#         form = EmailPostForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             #--- send mail
#             post_url = request.build_absolute_uri(post.get_absolute_url())
#             subject = f"{cd['name']} recommends you read " \
#                 f"{post.title}"
#             message = f"Read {post.title} at {post url}\n\n" \
#                 f"{cd['name']}\'s comments: {cd['comments']}"
#             send_mail(subject, message, 'blogging@village.ng', [cd['to']])
#             sent = True

#     else:
#         form = EmailPostForm()
#     return render(request, 'blog/share.html', {'post': post, 'form': form, 'sent': sent})

