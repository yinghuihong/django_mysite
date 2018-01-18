from django.contrib import admin

from .models import Choice, Question


# Register your models here.


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice  # Choice作为内联model
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [  # 字段排序
        (None, {'fields': ['question_text']}),  # 第一个参数为字段的Title
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]  # 设置内联对象
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 展示字段
    list_filter = ['pub_date']  # 会展示日期过滤组件
    search_fields = ['question_text']  # 会展示搜索组件


admin.site.register(Question, QuestionAdmin)
