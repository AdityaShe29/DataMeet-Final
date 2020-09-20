# Generated by Django 3.0.6 on 2020-09-20 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0009_auto_20200920_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotionqueries',
            name='confusion',
            field=models.DecimalField(decimal_places=7, default=0, max_digits=11),
        ),
        migrations.AlterField(
            model_name='emotionqueries',
            name='happy',
            field=models.DecimalField(decimal_places=7, default=0, max_digits=11),
        ),
        migrations.AlterField(
            model_name='emotionqueries',
            name='sad',
            field=models.DecimalField(decimal_places=7, default=0, max_digits=11),
        ),
        migrations.AlterField(
            model_name='emotionqueries',
            name='surprised',
            field=models.DecimalField(decimal_places=7, default=0, max_digits=11),
        ),
    ]
