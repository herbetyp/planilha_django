# Generated by Django 3.1.3 on 2020-12-21 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_spent_fixed_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='month',
            field=models.IntegerField(default=12, verbose_name='Mês'),
        ),
        migrations.AlterField(
            model_name='spent',
            name='month',
            field=models.IntegerField(default=12, verbose_name='Mês'),
        ),
    ]
