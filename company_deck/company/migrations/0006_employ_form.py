# Generated by Django 3.1.1 on 2020-09-20 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20200919_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employ_Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=250)),
                ('lname', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('copname', models.CharField(max_length=250)),
                ('job_title', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
            ],
        ),
    ]