# Generated by Django 2.0 on 2017-12-25 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171225_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_word', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_key', models.CharField(default='', max_length=255)),
                ('key_word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.KeyWord')),
            ],
        ),
    ]
