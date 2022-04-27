from django.db import models

# Create your models here.
class Teachers(models.Model):
    username = models.CharField(verbose_name='ФИ', max_length=100)
    position = models.CharField(verbose_name='Должность', max_length=60)
    subject = models.ForeignKey('Subjects', verbose_name='Дисциплина', on_delete=models.CASCADE)
    cabinet = models.IntegerField(verbose_name='Кабинет')
    salary = models.DecimalField(verbose_name='Зарплата', max_digits=8, decimal_places=2)
    
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        
    def __str__(self):
        return self.username


class Subjects(models.Model):
    title = models.CharField(verbose_name='Дисциплина', max_length=60)
    tcode = models.IntegerField(verbose_name='Учебный код')
    
    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'
        
    def __str__(self):
        return self.title
    