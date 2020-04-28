import pymysql

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
import random
import time

from django.shortcuts import render

from multiprocessing import Process

# Create your views here.

# 월드컵의 진행상황
rcount = 32

conn = ""

next_stage_cnt = 0
# 몇개중 몇개인지 판별
stage_cnt=1


# 데이터베이스 연결
def dbconnection():
    global conn
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='BLOG', charset='utf8')


# 검색어 리스트
def categoryList(tablename):
    if tablename == 'city':
        list_A = ['한국-서울', '미국-워싱턴', '일본-도쿄', '독일-베를린', '영국-런던', '러시아-모스크바', '인도-뉴델리', '브라질-브라질리아', '태국-방콕', '대만-타이베이', '스페인-마드리드', '이탈리아-로마', '핀란드-헬싱키', '헝가리-부다페스트', '체코-프라하', '터키-앙카라',
                  '프랑스-파리', '벨기에-브뤼셀', '그리스-아테네', '네덜란드-암스테르담', '캐나다-오타와', '칠레-산티아고', '필리핀-마닐라', '이스라엘-예루살렘', '네팔-카트만두', '불가리아-소피아', '오스트리아-빈', '스웨덴-스톡홀름', '스위스-베른', '폴란드-바르샤바', '멕시코-멕시코시티', '아르헨티나-부에노스아이레스',] # 세부 항목 이름
        return list_A
    elif tablename == "food":
        list_B = ['짜장면', '짬뽕', '스시', '라면', '케밥', '에그타르트', '볶음밥', '초콜릿', '햄버거', '치킨', '피자', '로브스터', '갈비', '빠에야', '새우튀김', '빵'
            ,'우동', '태국-팟타이', '타코야끼', '베이징 덕', '카레', '삼계탕', '샌드위치', '김밥', '제육볶음', '돈까스', '딤섬', '파스타', '계란말이', '떡볶이', '탕수육', '비빔밥']  # 세부 항목 이름
        return list_B
    elif tablename == "movie":
        list_C = ['스파이더맨 파 프롬 홈', '어벤져스 엔드게임', '아바타', '자전차왕 엄복동', '쥬라기월드', '영화 타이타닉', '영화 스타워즈', '분노의 질주', '영화 겨울왕국', '해리포터와 죽음의 성물'
            , '토이 스토리', '영화 다크 나이트', '영화 알라딘', '영화 조커', '반지의 제왕', '터미네이터', '영화 극한직업', '영화 정글북', '위대한 개츠비', '영화 캐리비안의 해적'
            , '보헤미안 랩소디', '퍼시픽 림 업라이징', '메이즈 러너', '영화 신과함께', '영화 트랜스포머', '영화 바람', '영화 레지던트 이블', '영화 쥬만지 새로운 세계', '영화 엽문', '영화 리얼스틸', '영화 데드풀', '영화 에나벨']  # 세부 항목 이름
        return list_C
    else:
        list_D = ['안유진', '장원영', '헬로비너스 나라', '애프터스쿨 나나', '아이린', '한효주', '수지', '한지민', '전소미', '송혜교', '프리스틴 시연', '걸그룹 여자친구', '걸그룹 러블리즈', '오마이걸 승희', '하지원', '전지현'
            , '방탄소년단', '이병헌', '유재석', '장동건', '원빈', '송중기', '유병재', '강동원', '이준기', '류승범', '조승우', '박보검', '조정석', '류준열', '김수현', '박서준']  # 세부 항목 이름
        return list_D


# 월드컵 데이터베이스 비우기
def image_delete(tablename):
    dbconnection()
    cursor = conn.cursor()
    if tablename == 'city':
        sql = "delete from worldcup_cityimage"
    elif tablename == "food":
        sql = "delete from worldcup_foodimage"
    elif tablename == "movie":
        sql = "delete from worldcup_movieimage"
    else:
        sql = "delete from worldcup_enterimage"
    cursor.execute(sql)
    conn.commit()
    conn.close()

# 크롤링작업 및 DB에 데이터 삽입
def image_in(tablename, img_search, inum):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('disable-gpu')
    chrome_options.add_argument('lang=ko_KR')

    url = "https://www.google.com/search?q=" + img_search[inum] + "&source=lnms&tbm=isch"
    browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    # print("쓰레드 번호",inum,"이미지 아이넘 : ",img_search[inum])
    browser.implicitly_wait(3)
    browser.get(url)
    # time.sleep(3)
    # 해당하는 확장자 외 값은 가지고 오지 않음.
    while True:
    # for r in range(10):
    #     r = random.randint(0,10)
        r=0
        x = browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')[r]
        img = json.loads(x.get_atribute('innerHTML'))["ou"]

        if img.endswith('.jpg') or img.endswith('.jpeg') or img.endswith('.png') == True:
            print("쓰레드 번호 : ",inum," 성공! "," r = ",r)
            break
        else:
            print("쓰레드 번호 : ",inum,'재실행'," r = ",r)

    dbconnection()
    cursor = conn.cursor()
    img_name = img_search[inum]
    if tablename == 'city':
        sql = "insert into worldcup_cityimage values (%s,%s,%s,%s,%s)"
    elif tablename == "food":
        sql = "insert into worldcup_foodimage values (%s,%s,%s,%s,%s)"
    elif tablename == "movie":
        sql = "insert into worldcup_movieimage values (%s,%s,%s,%s,%s)"
    else:
        sql = "insert into worldcup_enterimage values (%s,%s,%s,%s,%s)"
    cursor.execute(sql, (0, img, rcount, img_name, 0))
    conn.commit()
    conn.close()
    browser.close()

# 크롤링 프로세스 생성 및 실행
def crawling_Process(tablename):
    for i in range(rcount):

        cmd_process = 'pr'+str(i)+ '= Process(target=image_in, args=(tablename, categoryList(tablename), i))'
        exec(cmd_process)

    for i in range(rcount):
        cmd_start = 'pr'+str(i)+'.start()'
        exec(cmd_start)

    for i in range(rcount):
        cmd_join = 'pr'+str(i)+'.join()'
        exec(cmd_join)





# DB에 저장된 이미지 URL이 들어있는 값을 불러와서 템플릿에 반환
def imageLoad(request, name1='', tablename=''):
    global stage_cnt
    global rcount
    global next_stage_cnt

    if next_stage_cnt >= 1:
        stage_cnt += 1

    if name1 != "":
        imageWinUpdate(request, rcount, name1, tablename)
        if int(rcount / 2) < stage_cnt:
            rcount = int(rcount / 2)
            stage_cnt = 1

    dbconnection()
    if rcount > 1:
        for i in range(2):
            cursor1 = conn.cursor()
            cursor2 = conn.cursor()

            if tablename == 'city':
                sql_select_image = "select image from worldcup_cityimage where `rank`=%s and choice=0"
                sql_select_name = "select `name` from worldcup_cityimage where `rank`=%s and choice=0"
                title = '도시'
            elif tablename == 'food':
                sql_select_image = "select image from worldcup_foodimage where `rank`=%s and choice=0"
                sql_select_name = "select `name` from worldcup_foodimage where `rank`=%s and choice=0"
                title = '음식'
            elif tablename == 'movie':
                sql_select_image = "select image from worldcup_movieimage where `rank`=%s and choice=0"
                sql_select_name = "select `name` from worldcup_movieimage where `rank`=%s and choice=0"
                title = '영화'
            else:
                sql_select_image = "select image from worldcup_enterimage where `rank`=%s and choice=0"
                sql_select_name = "select `name` from worldcup_enterimage where `rank`=%s and choice=0"
                title = '연예인'

            cursor1.execute(sql_select_image, rcount)
            cursor2.execute(sql_select_name, rcount)

            image_list = cursor1.fetchall()
            name_list = cursor2.fetchall()

            randrange = len(image_list)

            # 리스트가 들어 있는 변수 생성
            image_list2 = []
            name_list2 = []

            # 튜플로 온 데이터를 리스트로 변환
            for j in range(randrange):
                image_list2.append(image_list[j][0])

            for j in range(randrange):
                name_list2.append(name_list[j][0])

            randnum = random.randint(1, randrange)
            randnum -= 1

            if i == 0:
                name1 = name_list2[randnum]
                data1 = image_list2[randnum]

                # data1의 name
                choice_image_name = name_list2[randnum]

                cursor3 = conn.cursor()
                if tablename == 'city':
                    sql_choice_update = "update worldcup_cityimage set choice=1 where name=%s"
                elif tablename == 'food':
                    sql_choice_update = "update worldcup_foodimage set choice=1 where name=%s"
                elif tablename == 'movie':
                    sql_choice_update = "update worldcup_movieimage set choice=1 where name=%s"
                else:
                    sql_choice_update = "update worldcup_enterimage set choice=1 where name=%s"
                cursor3.execute(sql_choice_update, choice_image_name)

                conn.commit()

            else:
                name2 = name_list2[randnum]
                data2 = image_list2[randnum]

                # data1의 name
                choice_image_name = name_list2[randnum]

                cursor3 = conn.cursor()
                if tablename == 'city':
                    sql_choice_update = "update worldcup_cityimage set choice=1 where name=%s"
                elif tablename == 'food':
                    sql_choice_update = "update worldcup_foodimage set choice=1 where name=%s"
                elif tablename == 'movie':
                    sql_choice_update = "update worldcup_movieimage set choice=1 where name=%s"
                else:
                    sql_choice_update = "update worldcup_enterimage set choice=1 where name=%s"
                cursor3.execute(sql_choice_update, choice_image_name)

                conn.commit()
    else:
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()

        if tablename == 'city':
            sql_image = "select image from worldcup_cityimage order by `rank`"
            sql_name = "select `name` from worldcup_cityimage order by `rank`"
            title = '도시'
        elif tablename == 'food':
            sql_image = "select image from worldcup_foodimage order by `rank`"
            sql_name = "select `name` from worldcup_foodimage order by `rank`"
            title = '음식'
        elif tablename == 'movie':
            sql_image = "select image from worldcup_movieimage order by `rank`"
            sql_name = "select `name` from worldcup_movieimage order by `rank`"
            title = '영화'
        else:
            sql_image = "select image from worldcup_enterimage order by `rank`"
            sql_name = "select `name` from worldcup_enterimage order by `rank`"
            title = '연예인'

        cursor1.execute(sql_image)
        cursor2.execute(sql_name)

        datalist = []
        namelist = []

        datatuple = cursor1.fetchall()
        nametuple = cursor2.fetchall()

        for i in range(len(datatuple)):
            datalist.append(datatuple[i][0])
            namelist.append(nametuple[i][0])

        conn.commit()
        # 다시하기 실행을 위해 rcount 초기화
        rcount = 32
        next_stage_cnt = 0
        stage_cnt = 1
        return render(request, 'worldcup_result.html', {'name': name1, 'tablename': tablename,
                                                             'alldata':datalist, 'allname': namelist, 'title': title})
    next_stage_cnt += 1
    conn.close()

    return render(request, 'worldcup_main.html', {'name1': name1, 'name2': name2, 'datas1': data1, 'datas2': data2, 'tablename': tablename
                                                    , 'rcount': rcount, 'half': int(rcount/2), 'st': stage_cnt, 'title': title})


# 사진이 선택됬을 때
def imageWinUpdate(request, rcount, name1, tablename):
    dbconnection()
    cursor = conn.cursor()
    rcount = int(rcount / 2)

    if tablename == 'city':
        sql_update = "update worldcup_cityimage set `rank`=%s, choice=0 where name=%s"
    elif tablename == 'food':
        sql_update = "update worldcup_foodimage set `rank`=%s, choice=0 where name=%s"
    elif tablename == 'movie':
        sql_update = "update worldcup_movieimage set `rank`=%s, choice=0 where name=%s"
    else:
        sql_update = "update worldcup_enterimage set `rank`=%s, choice=0 where name=%s"
    cursor.execute(sql_update, (rcount, name1))
    conn.commit()
    conn.close()


# /worldcup/
def goHome(request):

    return render(request, 'home.html')


# 처음 메뉴바에서 이상형월드컵 눌렀을때 실행
def imageLV(request, tablename):
    image_delete(tablename)
    crawling_Process(tablename)

    return render(request, 'worldcup_start.html', {'tablename': tablename})