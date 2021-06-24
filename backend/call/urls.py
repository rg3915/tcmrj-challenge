from django.urls import include, path

from backend.call import views as v

app_name = 'call'

call_patterns = [
    path('', v.CallListView.as_view(), name='call_list'),
    path('<int:pk>/', v.CallDetailView.as_view(), name='call_detail'),
    path('create/', v.CallCreateView.as_view(), name='call_create'),
    path('<int:pk>/update/', v.CallUpdateView.as_view(), name='call_update'),
    path('<int:pk>/delete/', v.CallDeleteView.as_view(), name='call_delete'),
    path('management/', v.call_management, name='call_management'),
]

category_patterns = [
    path('', v.CategoryListView.as_view(), name='category_list'),
    path('<int:pk>/', v.CategoryDetailView.as_view(), name='category_detail'),
    path('create/', v.CategoryCreateView.as_view(), name='category_create'),
    path('<int:pk>/update/', v.CategoryUpdateView.as_view(), name='category_update'),  # noqa E501
    path('<int:pk>/delete/', v.CategoryDeleteView.as_view(), name='category_delete'),  # noqa E501
]

subcategory_patterns = [
    path('', v.SubcategoryListView.as_view(), name='subcategory_list'),
    path('<int:pk>/', v.SubcategoryDetailView.as_view(), name='subcategory_detail'),
    path('create/', v.SubcategoryCreateView.as_view(), name='subcategory_create'),
    path('<int:pk>/update/', v.SubcategoryUpdateView.as_view(), name='subcategory_update'),  # noqa E501
    path('<int:pk>/delete/', v.SubcategoryDeleteView.as_view(), name='subcategory_delete'),  # noqa E501
]


urlpatterns = [
    path('call/', include(call_patterns)),
    path('category/', include(category_patterns)),
    path('subcategory/', include(subcategory_patterns)),
]
