from django.db import models
from .train import Train


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
        self._name = value

    @property
    def train(self):
        return self._train

    def accept_train(self, train):
        if type(train) is Train:
            self._train = train
            self.save()
        else:
            print('Wrong type')
