# Generated by Django 4.0.1 on 2022-01-12 19:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_countrygroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Наименование')),
                ('flag', models.FileField(upload_to='country_flags/', validators=[django.core.validators.FileExtensionValidator(['svg'])], verbose_name='Флаг')),
                ('country_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='assets.countrygroup', verbose_name='Группа стран')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
                'db_table': 'country',
                'ordering': ('name',),
            },
        ),
    ]
