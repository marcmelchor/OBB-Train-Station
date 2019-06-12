from django.db import models
from .train import Train


class ICE(Train, models.Model):
    _name = models.CharField(max_length=100)
    _dock_train = models.ManyToManyField('self', related_name='dependent_on', blank=True)

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
    def doc_train(self):
        return self._dock_train

    def dock_train(self, ice):
        if type(ice) is ICE:
            self._dock_train.add(ice)
        else:
            print('Wrong type')
