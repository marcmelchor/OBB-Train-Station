from obb.models import TrainStation, Platform, ICE, TrainSection, Person

# Create a train station
platform = Platform(name='platform 1')
platform.save()
train_station = TrainStation(name='Linz')
train_station.save()
train_station.add_platform(platform)

# Create a train
train_1 = ICE(name='ICE 1')
train_1.save()
platform.accept_train(train_1)
train_section_1 = TrainSection(name='First section')
train_section_1.save()
train_section_2 = TrainSection(name='Second section')
train_section_2.save()
train_section_3 = TrainSection(name='Third section')
train_section_3.save()
train_1.dock_section(train_section_1)
train_1.dock_section(train_section_2)
train_1.dock_section(train_section_3)
train_1.print_sections()

# Create persons
person_1 = Person(first_name='Franz', last_name='Mair')
person_2 = Person(first_name='Michael', last_name='Schuh')
person_3 = Person(first_name='Herbert', last_name='Sailer')
person_4 = Person(first_name='Michaela', last_name='Mader')
train_section_1.get_on_train(person_1)
train_section_1.get_on_train(person_2)
train_section_2.get_on_train(person_3)
train_section_3.get_on_train(person_4)
train_section_2.get_off_train(person_3)

# Query passengers
train_1.show_current_passengers()
train_1.count_passengers()