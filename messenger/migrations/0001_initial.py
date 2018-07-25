# Generated by Django 2.0.5 on 2018-07-23 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromuser', models.IntegerField(default=0)),
                ('touser', models.IntegerField(default=0)),
                ('chattext', models.TextField(default=' ', verbose_name='ChatBox')),
            ],
        ),
    ]