from django.contrib import admin

# Register your models here.
from .models import VanessaModule
from .models import UserAnswerWord

# admin.site.register(ABC_Modules)

# admin.site.register(User_Answers)

class UserAnswerWordInline(admin.TabularInline):
    # таблиця ключових слів відповіді користувача
    # буде в одній формі з модулем, що редагується
    
    # class User_AnswersInline(admin.TabularInline):
    # class User_AnswersInline(admin.StackedInline):
    # StackedInline - всі поля одного записув стовпчик
    # TabularInline - всі поля одного запису в лінію 
    
    model = UserAnswerWord
    # кількість ключових слів підпорядкованої таблиці відповідей користувача, 
    # що відображаються на адмін-екрані під полями редагування запису ABC-модулю
    extra = 3 

class VanessaModuleAdmin(admin.ModelAdmin):
    inlines = [UserAnswerWordInline]
    list_display = ('module_type', 'module_number', 'module_used', 'vanessa_question','url_address')
    # колонки таблиці - 'created_date', вилучено 
    search_fields = ('vanessa_question',)
    list_display_links = ('module_type', 'url_address')
    # поля для переходу до форми редагування'created_date',
    list_editable = ('module_number', 'module_used', 'vanessa_question')
    # поля, що редагуються безпосередньо в таблиці ,'url_address'
    list_filter = ['module_type', 'module_used']
    # фільтрація модулів, 'module_level'
  
    


# class User_Answers_Admin(admin.ModelAdmin):
    # list_display = ('module_guestion_field', 'created_date', 'keyword','keyword_weight')
    # search_fields = ('keyword','keyword_weight')
  
    # list_display_links = ('created_date', 'keyword','keyword_weight')
    # list_ select related('module_code',)


# admin.site.register(User_Answers, User_Answers_Admin)
admin.site.register(VanessaModule, VanessaModuleAdmin)
