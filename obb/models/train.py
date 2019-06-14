from django.db import models
from .train_section import TrainSection


class Train(models.Model):
    _train_section = models.ManyToManyField(TrainSection, blank=True)

    def __str__(self):
        return str(self.pk)

    def __unicode__(self):
        return '/%i/' % self.pk

    @property
    def train_section(self):
        return self._train_section

    @train_section.setter
    def train_section(self, value):
        if type(value) is TrainSection:
            self._train_section.add(value)
            value.order = self._train_section.all().count() - 1
            value.save()

    def dock_section(self, train_section):
        if type(train_section) is TrainSection:
            self._train_section.add(train_section)
            train_section.order = self._train_section.all().count() - 1
            train_section.save()
        else:
            print('Wrong type')

    def print_sections(self):
        sections_list = self._train_section.all().order_by('order')
        for section in sections_list:
            print(section.name)

    def show_current_passengers(self):
        sections = self._train_section.all()
        for section in sections:
            for person in section.person.all():
                print(person.first_name + ' ' + person.last_name)

    def count_passengers(self):
        sections = self.train_section.all()
        count = 0
        for section in sections:
            count += section.person.all().count()
        print(count)
