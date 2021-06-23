from django.urls import include, path

from backend.call import views as v

app_name = 'call'

call_patterns = [
    path('', v.CallListView.as_view(), name='call_list'),
    path('<int:pk>/', v.CallDetailView.as_view(), name='call_detail'),
    path('create/', v.CallCreateView.as_view(), name='call_create'),
    path('<int:pk>/update/', v.CallUpdateView.as_view(), name='call_update'),
]

category_patterns = [
    path('', v.CategoryListView.as_view(), name='category_list'),
    path('<int:pk>/', v.CategoryDetailView.as_view(), name='category_detail'),
    path('create/', v.CategoryCreateView.as_view(), name='category_create'),
    path('<int:pk>/update/', v.CategoryUpdateView.as_view(), name='category_update'),
    path('<int:pk>/delete/', v.CategoryDeleteView.as_view(), name='category_delete'),
]


urlpatterns = [
    path('call/', include(call_patterns)),
    path('category/', include(category_patterns)),
]
