# Generated by Django 4.0.1 on 2022-01-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Отрасль',
                'verbose_name_plural': 'Отрасли',
                'db_table': 'branch',
                'ordering': ('name',),
            },
        ),
    ]