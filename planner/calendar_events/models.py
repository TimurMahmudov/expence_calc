import datetime

from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name="Название")
    time = models.DateTimeField(verbose_name="Дата и время проведения",
                                help_text="Выберите время проведения",
                                null=True,
                                blank=True)
    description = models.TextField(null=True,
                                   blank=True,
                                   verbose_name="Описание",
                                   help_text="Добавьте описание к событию")

    def __str__(self):
        return self.title

    def get_countdown(self):
        current_day = datetime.datetime.now()
        appointed_time = self.time
        diff = appointed_time - current_day
        if diff.days < 0:
            return "Ивент окончен"
        result = str(datetime.timedelta(seconds=diff.seconds))
        return result

    get_countdown.short_description = "Осталось времени"

    def get_description(self):
        return f"{self.description[:20]}..."

    class Meta:
        ordering = ("time",)
        verbose_name = "Событие"
        verbose_name_plural = "События"
