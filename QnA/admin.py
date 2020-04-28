from django.contrib import admin
from QnA.models import Qpost


# Register your models here.

class QpostAdmin(admin.ModelAdmin):
    list_display = ('title','modify_date')
    list_filter = ('modify_date', )
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}#, 'description': ('content',)} #slug 사이트명을 짧게 약어로 써준다


admin.site.register(Qpost, QpostAdmin)