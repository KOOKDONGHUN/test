from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView
from QnA.models import Qpost
from QnA.form import QpostForm
import pymysql



# Create your views here.


# ListView
class QpostLV(ListView):
    model = Qpost  #테이블을 사용한다??
    template_name = 'QnA/QnA.html'
    context_object_name = 'Qposts'
    paginate_by = 10 # 페이지당 보여지는 개수

# DetailView
class QpostDV(DetailView):
    model = Qpost
    template_name = 'QnA/QnA_detail.html'

# def Qpost_create(request):
#         if request.method == 'POST'
#             new_article =

def qpost_new(request):
    if request.method == 'POST':
        form = QpostForm(request.POST)
        if form.is_valid():
            Qpost = form.save(commit=False)
            Qpost.author = request.user
            Qpost.save()
            return redirect( 'QnA:Qpost_detail', pk=Qpost.pk)
    else:
        form = QpostForm
    return render(request, 'QnA/QnA_create.html', {'form': form})
def dbconnection():
    global conn
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='BLOG', charset='utf8')

def delview(request, pk):
    dbconnection()
    cursor = conn.cursor()
    sql = "DELETE from QnA_post where id=%s"
    cursor.execute(sql, pk)
    conn.commit()
    conn.close()
    return redirect('QnA:index')