# Generated by Django 4.0.1 on 2022-01-15 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_sharetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='EtfType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Вид фондов',
                'verbose_name_plural': 'Виды фондов',
                'db_table': 'etf_type',
                'ordering': ('name',),
            },
        ),
    ]