from worldcup.views import *
from django.urls import path


app_name = 'worldcup' # 2.0 이후부터는 자신의 이름이 무엇인지 알려주는 코드
urlpatterns = [
    path('',goHome),

    path('<str:tablename>/', imageLV, name='worldcupindex'),
    path('load/<str:tablename>/', imageLoad, name='imageload'),
    path('load/<str:tablename>/<str:name1>/', imageLoad, name='leftimage'),
    path('load/<str:tablename>/<str:name2>/', imageLoad, name='rightimage'),
    path('load/<str:tablename>/<str:name>/',imageLoad, name='winimageload')
]