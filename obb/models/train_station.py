from django.db import models
from .platform import Platform


class TrainStation(models.Model):
    _name = models.CharField(max_length=100)
    _platform = models.ManyToManyField(Platform, blank=True)

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

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        if type(value) is Platform:
            self._platform.add(value)

    def add_platform(self, platform):
        if type(platform) is Platform:
            self._platform.add(platform)
        else:
            print('Wrong type')
