# Generated by Django 4.2 on 2023-05-04 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='이메일 주소')),
                ('password', models.CharField(max_length=256, verbose_name='비밀번호')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('join_date', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('gender', models.CharField(choices=[('F', '여성'), ('M', '남성'), ('None', '공개하지 않음')], max_length=10, verbose_name='성별')),
                ('introduction', models.TextField(blank=True, default='', verbose_name='자기소개')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
