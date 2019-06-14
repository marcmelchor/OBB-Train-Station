from django.db import models
from .person import Person


class TrainSection(models.Model):
    _name = models.CharField(max_length=100)
    _order = models.IntegerField(default=-1)
    _person = models.ManyToManyField(Person, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '/%s/' % self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value='default'):
        self._name = value[: 100]

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value

    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, value):
        if type(value) is Person:
            self._person.add(value)

    def get_on_train(self, person):
        if type(person) is Person:
            self._person.add(person)
            print(person.first_name + ' ' + person.last_name + ' is on the train now')
        else:
            print('Wrong type')

    def get_off_train(self, person):
        if type(person) is Person:
            self._person.remove(person)
            print(person.first_name + ' ' + person.last_name + ' has left the train')
        else:
            print('Wrong type')
