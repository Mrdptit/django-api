# Generated by Django 2.0 on 2017-12-29 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(default='', max_length=255, unique=True)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('first_name', models.CharField(default='', max_length=255)),
                ('token', models.CharField(default='', max_length=255)),
                ('facebook_id', models.CharField(default='', max_length=255)),
                ('avatar', models.CharField(default='https://www.google.com.vn/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjXmYPb6KvYAhXLto8KHVlVDC8QjRwIBw&url=http%3A%2F%2Fwww.yxineff.com%2Fen%2Ffilmmakers%2Fnguyen-thuy-tien%2F&psig=AOvVaw010B5-zNbkVHktKfy_JPy0&ust=1514519967983392', max_length=255)),
                ('cover', models.CharField(default='https://www.google.com.vn/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwinz97z6KvYAhUfSI8KHVL7CsgQjRwIBw&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DQX4j_zHAlw8&psig=AOvVaw2alZ9a3n7ICEn89KdwdkAk&ust=1514520024404108', max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('verifyUser', models.BooleanField(default=False)),
                ('verify_key', models.CharField(default='', max_length=40)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KeyWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(default='', max_length=255)),
                ('key_word', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Value_Charater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_word', models.CharField(default='', max_length=255)),
                ('value_key', models.CharField(default='', max_length=255)),
                ('u_id', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
