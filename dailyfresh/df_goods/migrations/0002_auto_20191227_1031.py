# Generated by Django 2.0 on 2019-12-27 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='gkucun',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gintro',
            field=models.CharField(max_length=200),
        ),
    ]