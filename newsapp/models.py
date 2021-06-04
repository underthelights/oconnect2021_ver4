from datetime import datetime, timezone, timedelta

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class News(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='news', null=True)
    title = models.CharField(verbose_name='TITLE', max_length=70, null=True)
    image = models.ImageField(upload_to='news/', null=True)
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True, null=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True, null=True)

    @property
    def show_date(self):
        time = datetime.now(tz=timezone.utc) - self.modify_dt

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.modify_dt.date()
            return str(time.days) + '일 전'
        else:
            return False


