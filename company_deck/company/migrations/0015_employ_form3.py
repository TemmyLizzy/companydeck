# Generated by Django 3.1.1 on 2020-09-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0014_auto_20200922_0330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employ_Form3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per', models.CharField(max_length=100)),
                ('comment', models.TextField(max_length=500)),
            ],
        ),
    ]
