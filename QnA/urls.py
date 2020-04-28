# from django.conf.urls import url
from QnA.views import *
from django.urls import path

app_name = 'QnA' # 2.0 이후부터는 자신의 이름이 무엇인지 알려주는 코드?
urlpatterns = [
    # /blog/
    # url(r'^$', PostLV.as_view(), name='index'),
    path('', QpostLV.as_view(), name='index'),

    # /blog/post/
    # url(r'^post/$', PostLV.as_view(), name='post_list'),
    path('qna/', QpostLV.as_view(), name='Qpost_list'),
    path('qna/<int:pk>/', QpostDV.as_view(), name='Qpost_detail'),
    path('new/', qpost_new, name='Qpost_new'),
    path('remove/<int:pk>/', delview, name='delete'),
]