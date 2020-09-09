from django.db import models
from django.utils import timezone
# Create your models here.


class Member(models.Model):
    PLACE_CHOICE = (
        ('HOME', '在宅'),
        ('MEJIRO', '目白台'),
        ('OOTE', '大手町'),
        ('DAYOFF','休暇'),
    )

    STATUS_CHOICE = (
        ('WORK', '勤務中'),
        ('LEAVE', '離席中'),
        ('LUNCH', '食事中'),
    )

    name = models.CharField(
        verbose_name='名前',
        max_length=200,
    )

    place = models.CharField(
        verbose_name='勤務場所',
        choices=PLACE_CHOICE,
        max_length=10,
        default='目白台',
    )

    status = models.CharField(
        verbose_name='勤務ステータス',
        choices=STATUS_CHOICE,
        max_length=10,
        default='勤務中',
    )

    #********************************************
    status_work = models.BooleanField(
        default=False,
    )

    status_home = models.BooleanField(
        default=False,
    )

    status_meeting = models.BooleanField(
        default=False,
    )

    status_lunch = models.BooleanField(
        default=False,
    )

    last_update_time = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.name
