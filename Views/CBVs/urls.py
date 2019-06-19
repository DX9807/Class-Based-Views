from django.urls import path
from .import views

app_name='CBVs'

urlpatterns=[
      path('',views.PostsListView.as_view(),name='list'),
      path('<int:pk>/',views.PostsDetailView.as_view(),name='detail'),
      path('update/<int:pk>/',views.PostsUpdateView.as_view(),name='update'),
      path('create/',views.PostsCreateView.as_view(),name='create'),
      path('delete/<int:pk>/',views.PostsDeleteView.as_view(),name='delete'),
]
