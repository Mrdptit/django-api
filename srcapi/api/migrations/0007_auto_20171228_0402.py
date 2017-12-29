# Generated by Django 2.0 on 2017-12-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(default='https://www.google.com.vn/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjXmYPb6KvYAhXLto8KHVlVDC8QjRwIBw&url=http%3A%2F%2Fwww.yxineff.com%2Fen%2Ffilmmakers%2Fnguyen-thuy-tien%2F&psig=AOvVaw010B5-zNbkVHktKfy_JPy0&ust=1514519967983392', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='cover',
            field=models.CharField(default='https://www.google.com.vn/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwinz97z6KvYAhUfSI8KHVL7CsgQjRwIBw&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DQX4j_zHAlw8&psig=AOvVaw2alZ9a3n7ICEn89KdwdkAk&ust=1514520024404108', max_length=255),
        ),
    ]
