# Generated by Django 3.0.6 on 2020-09-20 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0006_auto_20200919_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='teacher_name',
            field=models.CharField(default='None', max_length=41),
        ),
    ]
