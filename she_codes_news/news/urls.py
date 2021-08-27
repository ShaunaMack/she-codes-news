from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # /news/
    path('<int:pk>/', views.StoryView.as_view(), name='story'), # /news/3
    path('stories/', views.StoryListView.as_view(), name='stories'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'), # /news/add-story
    path('<int:pk>/edit/', views.StoryUpdateView.as_view(), name='editStory'), # /news/1/edit
    path('<int:pk>/delete/', views.StoryDeleteView.as_view(), name='deleteStory'),
]
 