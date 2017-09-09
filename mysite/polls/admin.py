from django.contrib import admin

from .models import Choice, Question

admin.site.site_header = "Polls Administrator"


class ChoiceInline(admin.TabularInline):
    model = Choice  # Choice对象在Question的管理界面中编辑。
    extra = 3  # 默认提供额外3个Choice的空间。


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
