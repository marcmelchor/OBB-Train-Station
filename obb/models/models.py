from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return(self.first_name)

    def __unicode__(self):
        return '/%s/' % self.first_name


class TrainSection(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=-1)
    person = models.ManyToManyField(Person, blank=True)


    def __str__(self):
        return(self.name)

    def __unicode__(self):
        return '/%s/' % self.name

    def get_on_train(self, Person):
        self.person.add(Person)
        print(Person.first_name + ' ' + Person.last_name + ' is on the train now')

    def get_off_train(self, Person):
        self.person.remove(Person)
        print(Person.first_name + ' ' + Person.last_name + ' has left the train')


class Train(models.Model):
    train_section = models.ManyToManyField(TrainSection, blank=True)

    def __str__(self):
        return(str(self.id))

    def __unicode__(self):
        return '/%i/' % self.id

    def dock_section(self, TrainSection):
        self.train_section.add(TrainSection)
        TrainSection.order = self.train_section.all().count() - 1
        TrainSection.save()

    def print_sections(self):
        sections_list = self.train_section.all().order_by('order')
        for section in sections_list:
            print(section.name)

    def show_current_passengers(self):
        sections = self.train_section.all()
        for section in sections:
            for person in section.person.all():
                print(person.first_name + ' ' + person.last_name)

    def count_passengers(self):
        sections = self.train_section.all()
        count = 0
        for section in sections:
            count += section.person.all().count()
        print(count)
        


class Railjets(Train, models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return(self.name)

    def __unicode__(self):
        return '/%s/' % self.name

    def close_windows(self):
        print('windows closed')


class ICE(Train, models.Model):
    name = models.CharField(max_length=100)
    train = models.ManyToManyField('self', related_name='dependent_on', blank=True)
    
    def __str__(self):
        return(self.name)

    def __unicode__(self):
        return '/%s/' % self.name

    def dock_train(self, ICE):
        self.train.add(ICE)


class Platform(models.Model):
    name = models.CharField(max_length=100)
    train = models.ForeignKey(Train, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return(self.name)

    def __unicode__(self):
        return '/%s/' % self.name

    def accept_train(self, Train):
        self.train = Train
        self.save()

class TrainStation(models.Model):
    name = models.CharField(max_length=100)
    platform = models.ManyToManyField(Platform, blank=True)

    def __str__(self):
        return(self.name)

    def __unicode__(self):
        return '/%s/' % self.name

    def add_platform(self, Platform):
        self.platform.add(Platform)
