# Generated by Django 5.0.4 on 2024-04-27 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_jiaoshi_jsjy_jsxx_kecheng_qiandao_sjd_sksj_xingqi_xuesheng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsjy',
            name='nr',
            field=models.CharField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='kecheng',
            name='sm',
            field=models.CharField(max_length=400),
        ),
    ]