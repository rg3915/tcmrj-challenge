from django.urls import include, path

from backend.call import views as v

app_name = 'call'

call_patterns = [
    path('', v.CallListView.as_view(), name='call_list'),
    # path('<int:pk>/', v.call_detail, name='call_detail'),
    # path('create/', v.CallCreateView.as_view(), name='call_create'),
    path('<int:pk>/update/', v.CallUpdateView.as_view(), name='call_update'),
]


urlpatterns = [
    path('call/', include(call_patterns)),
]
