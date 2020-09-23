from django.conf import settings
from django.db import models
from django.utils import timezone

class VanessaModule(models.Model):
    verbose_name = "Модуль вопросов и ответов Ванессы"
    verbose_name_plural = "Модули вопросов и ответов Ванессы"
    
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    # 'Дата создания модуля'
    module_type = models.CharField('Тип', max_length=1)
    # 'Тип модуля'
    module_number = models.IntegerField('Номер', default=0)
    # 'Уровень модуля'
    module_used = models.BooleanField('Используется', default=True)
    # 'Модуль используется Ванессой'
    #previous_module = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    # ,  related_name='Предшествующий модуль'
    # previous_module = models.IntegerField('Предшествующий модуль', null=True)
    vanessa_question = models.CharField('Вопрос Ванессы', max_length=200)
    Vanessa_answer_word = models.BooleanField('Использовать слова пользователя в ответе', default=False)
    vanessa_answer = models.CharField('Ответ Ванессы', max_length=200, blank=True)
    # web_interface = models.CharField('Интерфейс', max_length=200, default='Интерфейс', blank=True)
    url_address = models.URLField('url ответа', max_length=200, blank=True, null=True)
               
    # def ABC_Modules_save(self):
    #     self.created_date = timezone.now()
    #     self.save()
        

class UserAnswerWord(models.Model):
    verbose_name = "Ключевое слово в ответе пользователя"
    verbose_name_plural = "Ключевые слова в ответе пользователя"
    
    created_date = models.DateTimeField('Дата', default=timezone.now)
    module_code = models.ForeignKey('VanessaModule', on_delete=models.PROTECT, default=1)
    keyword = models.CharField(' Ключевое слово', max_length=30, blank=True)
    keyword_weight = models.FloatField('Вес(важность) слова', blank=True, null=True)
    next_module_number = models.IntegerField('Номер следующего модуля', default=0)
    vanessa_answer = models.CharField('Ответ Ванессы', max_length=200, blank=True)
    url_address = models.URLField('url ответа', max_length=200, blank=True, null=True)

    # def User_Answers_save(self):
    #     self.created_date = timezone.now()
    #     self.save()

    # def module_guestion_field(self):
    #     verbose_name = "Модуль вопросов и ответов Ванессы"
    #     return ABC_Modules.vanessa_question
        
    # def module_type_field(self):
    #     return ABC_Modules.module_type

    # def module_level_field(self):
    #     return ABC_Modules.module_level    

            
    
