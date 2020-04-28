# from django.conf.urls import url
from notice.views import *
from django.urls import path

app_name = 'notice' # 2.0 이후부터는 자신의 이름이 무엇인지 알려주는 코드?
urlpatterns = [
    # /blog/
    # url(r'^$', PostLV.as_view(), name='index'),
    path('', PostLV.as_view(), name='index'),

    # /blog/post/
    # url(r'^post/$', PostLV.as_view(), name='post_list'),
    path('post/', PostLV.as_view(), name='post_list'),
    path('post/<slug>/', PostDV.as_view(), name='post_detail'),
]