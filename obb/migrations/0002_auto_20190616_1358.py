# Generated by Django 2.2.2 on 2019-06-16 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obb', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ice',
            options={'verbose_name_plural': 'ICEs'},
        ),
        migrations.AlterUniqueTogether(
            name='platform',
            unique_together={('_train',)},
        ),
    ]