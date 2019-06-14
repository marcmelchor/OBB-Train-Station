from django.db import models


class Person(models.Model):
    _first_name = models.CharField(max_length=100)
    _last_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'People'

    def __str__(self):
        return self._first_name

    def __unicode__(self):
        return '/%s/' % self._first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value='default'):
        self._first_name = value[: 100]

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value='default'):
        self._last_name = value[: 100]
