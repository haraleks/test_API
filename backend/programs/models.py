# Create your models here.
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class MyUser(AbstractUser):

    report_id = models.BigIntegerField(blank=True, null=True, unique=True)


class Program(models.Model):
    name = models.CharField('Название программы', max_length=155, blank=False, null=False)
    is_active = models.BooleanField('Статус программы', null=False, default=False)
    ages = models.ManyToManyField(
                        'Age',
                        through='ProgramAgeRelationsTable',
                        related_name='programs',
                        blank=False
                    )
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)
    deleted_at = models.DateTimeField('Удален', null=True, default=None, blank=True)

    class Meta:
        verbose_name = 'Список Программ'
        verbose_name_plural = 'Список Программ'
        unique_together = [['created_at', 'id']]
        get_latest_by = ['-created_at', '-updated_at']
        select_on_save = True

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.deleted_at = datetime.now()


class Age(models.Model):
    from_age = models.IntegerField(
        'От какого возраста',
        validators=[MinValueValidator(1)],
        blank=False,
        null=False,
        default=1
    )
    to_age = models.IntegerField(
        'До какого возраста',
        validators=[MaxValueValidator(100)],
        blank=False,
        null=False,
        default=99
    )
    name = models.CharField('Имя возростной категории', blank=False, null=False, max_length=155)
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)
    deleted_at = models.DateTimeField('Удален', null=True, default=None, blank=True)

    class Meta:
        verbose_name = 'Возростная категория'
        verbose_name_plural = 'Возрастные категории'
        select_on_save = True
        get_latest_by = ['-created_at', '-updated_at']
        unique_together = [['from_age', 'to_age'], ['created_at', 'id']]

    def clean(self):
        if self.to_age < self.from_age:
            raise ValidationError(
                f'From ({self.from_age}) should be more '
                f'To ({self.to_age}'
            )

    def __str__(self):
        return self.name


# Модель для реализации связи MtoM для Program и Age
class ProgramAgeRelationsTable(models.Model):
    program_id = models.ForeignKey(Program, related_name='program_id', on_delete=models.SET_NULL, null=True)
    age_id = models.ForeignKey(Age, related_name='age_id', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)
    deleted_at = models.DateTimeField('Удален', null=True, default=None, blank=True)

    question_plus_variants_cnt = models.IntegerField(null=False, default=0)
    text_missing_words_cnt = models.IntegerField(null=False, default=0)
    image_plus_text_cnt = models.IntegerField(null=False, default=0)
    image_plus_variants_cnt = models.IntegerField(null=False, default=0)
    audio_plus_variants_cnt = models.IntegerField(null=False, default=0)
    video_plus_variants_cnt = models.IntegerField(null=False, default=0)
    build_sentence_cnt = models.IntegerField(null=False, default=0)

    class Meta:
        indexes = [
            models.Index(fields=['program_id', 'age_id']),
        ]
