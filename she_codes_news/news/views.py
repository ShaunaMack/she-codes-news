from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by("-pub_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:4]
        context['all_stories'] = NewsStory.objects.all().order_by("-pub_date")
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    # use the name we called the path in urlpatterns to get the url path
    success_url = reverse_lazy('news:index')

    # overriding form_valid which is on generic.CreateView
    def form_valid(self, form):
        #set author to user logged in
        form.instance.author = self.request.user
        return super().form_valid(form)

class StoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NewsStory
    fields = ['title', 'pub_date', 'content', 'image_url']
    template_name = 'news/editStory.html'
    success_url = reverse_lazy('news:index')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class StoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class StoryListView(generic.ListView, LoginRequiredMixin, UserPassesTestMixin,):
    model = NewsStory
    template_name = 'news/stories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_stories'] = NewsStory.objects.all().filter(author=self.request.user).order_by("-pub_date")
        return context

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
