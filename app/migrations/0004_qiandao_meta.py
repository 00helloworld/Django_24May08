# Generated by Django 5.0.4 on 2024-04-27 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_jsjy_nr_alter_kecheng_sm'),
    ]

    operations = [
        migrations.CreateModel(
            name='qiandao_meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kc', models.CharField(max_length=40)),
                ('code', models.CharField(max_length=40)),
                ('rq', models.CharField(max_length=40)),
                ('qdsj', models.CharField(max_length=40)),
            ],
        ),
    ]
