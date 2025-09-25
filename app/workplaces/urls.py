from django.urls import path

from ..workplaces import views


urlpatterns = [
    path('', views.WorkplacesView.as_view(), name='workplaces'),
    path('create/', views.WorkplaceCreateView.as_view(), name='workplace_create'),
    path('<uuid:pk>/', views.WorkplaceView.as_view(), name='workplace'),
    path('<uuid:pk>/update/', views.WorkplaceUpdateView.as_view(), name='workplace_update'),
    path('<uuid:pk>/delete/', views.WorkplaceDeleteView.as_view(), name='workplace_delete'),
]
