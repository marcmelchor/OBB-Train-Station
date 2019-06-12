from django.db import models
from .train import Train


class Railjets(Train, models.Model):
    _name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Railjets'

    def __str__(self):
        return self._name

    def __unicode__(self):
        return '/%s/' % self._name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value[: 100]

    @staticmethod
    def close_windows():
        print('windows closed')
