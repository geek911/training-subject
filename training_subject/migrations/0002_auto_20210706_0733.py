# Generated by Django 3.2.4 on 2021-07-06 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_subject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationquestionnaire',
            name='other_previous_work',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Specify your most recent work'),
        ),
        migrations.AlterField(
            model_name='educationquestionnaire',
            name='other_type_of_work',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Other type of work'),
        ),
    ]
