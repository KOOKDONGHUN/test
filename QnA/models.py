from __future__ import unicode_literals # 파이선 2.x 버전에서도 지원이 가능 하게 해준다 우리는 3.0
from django.db import models # 데이터베이스 연동
from django.utils.encoding import python_2_unicode_compatible # 아레와 같은말

from django.urls import reverse  # url 패턴생성? 해주는 장고에 있는 내장함수

# Create your models here.

# Create your models here.

@python_2_unicode_compatible
class Qpost(models.Model): #models의 model을 상속 받겠다
    #ㅍㅣㄹ드명---
    title = models.CharField('TITLE',max_length=50)

    slug = models.SlugField('SLUG',unique=True,allow_unicode=True,
                            help_text='one word for title alias') #타이틀의 별칭을 한단어로


    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date',auto_now_add=True) #현재시간을 추가
    modify_date = models.DateTimeField('Modify Date',auto_now=True) #수정된시간? #변경날짜


    class Meta:#테이블 자체의 정보
        verbose_name = 'Qpost' #테이블 별칭 단수별칭?
        verbose_name_plural = 'Qposts' #테이블 별칭 복수별칭?
        db_table = 'QnA_post' #데이터 베이스에 저장되는 테이블명     # 테이블 명이 된다?
        ordering = ('-modify_date',)# 모델 객체 출력시 변경날짜를 기준으로 -(내림차순) 정렬한다

    def __str__(self):
        return self.title


    # 기본 url # 정의된 객체의 url 리턴
    def get_absolute_url(self):
        return reverse('QnA:Qpost_detail', args=(self.id,)) # reverse 블로그에 대한 url을 출력?
                                                            # slug약어 사용가능?

    def get_previous_post(self):
        return self.get_previous_by_modify_date() #수정된 날짜를 기준으로 이전

    # 현재 포스트를 기준으로 다음 포스트 반환
    def get_next_post(self):
        return self.get_next_by_modify_date()