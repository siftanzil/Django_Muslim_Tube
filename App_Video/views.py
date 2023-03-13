from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from App_Video.models import Video, Comment, Like
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Video.forms import CommentForm
import uuid

# Create your views here.


class UploadVideo(LoginRequiredMixin, CreateView):
    model = Video
    template_name = 'App_Video/upload_video.html'
    fields = ('video_title', 'video_link', 'video',
              'video_thumb', 'video_description', 'category')

    def form_valid(self, form):
        form_obj = form.save(commit=False)
        form_obj.uploader = self.request.user
        title = form_obj.video_title
        form_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        form_obj.save()
        return HttpResponseRedirect(reverse('index'))


class VideoList(ListView):
    context_object_name = 'videos'
    model = Video
    template_name = 'App_Video/video_list.html'


class CategoryList(ListView):
    context_object_name = 'videos'
    model = Video
    template_name = 'App_Video/category_list.html'


class MyVideos(LoginRequiredMixin, TemplateView):
    template_name = 'App_Video/my_videos.html'


@login_required
def play_video(request, slug):
    video = Video.objects.get(slug=slug)
    comment_form = CommentForm()
    already_liked = Like.objects.filter(video=video, user=request.user)
    if already_liked:
        liked = True
    else:
        liked = False
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.video = video
            comment.save()
            return HttpResponseRedirect(reverse('App_Video:play_video', kwargs={'slug': slug}))
    return render(request, 'App_Video/play_video.html', context={'video': video, 'comment_form': comment_form, 'liked': liked, })


@login_required
def liked(request, pk):
    video = Video.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(video=video, user=user)
    if not already_liked:
        liked_post = Like(video=video, user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('App_Video:play_video', kwargs={'slug': video.slug}))


@login_required
def unliked(request, pk):
    video = Video.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(video=video, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Video:play_video', kwargs={'slug': video.slug}))


class UpdateVideo(LoginRequiredMixin, UpdateView):
    model = Video
    fields = ('video_title', 'video_link', 'video',
              'video_thumb', 'video_description', 'category')
    template_name = 'App_Video/update_video.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Video:play_video', kwargs={'slug': self.object.slug})
