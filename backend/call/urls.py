from django.urls import include, path

from backend.call import views as v

app_name = 'call'

call_patterns = [
    path('', v.CallListView.as_view(), name='call_list'),
]


urlpatterns = [
    path('call/', include(call_patterns)),
]
