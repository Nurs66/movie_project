from django.urls import path
from .views import MovieViews, MovieDetailView, AddReview

urlpatterns = [
    path('', MovieViews.as_view(), name='movie_list'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
]
