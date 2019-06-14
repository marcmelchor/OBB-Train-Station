from django.db import models
from .train import Train
from .ice import ICE
from .railjets import Railjets


class Platform(models.Model):
    _name = models.CharField(max_length=100)
    _train = models.ForeignKey(Train, on_delete=models.CASCADE, blank=True, null=True)

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
    def train(self):
        return self._train

    @train.setter
    def train(self, value):
        if type(value) is Train or type(value) is ICE or type(value) is Railjets:
            self._train = value
            self.save()

    def accept_train(self, train):
        if type(train) is Train or type(train) is ICE or type(train) is Railjets:
            self._train = train
            self.save()
        else:
            print('Wrong type')
