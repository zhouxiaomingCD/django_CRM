# Generated by Django 2.2 on 2019-08-21 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
        ('web', '0002_auto_20190820_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, verbose_name='部门名称')),
            ],
        ),
        migrations.AlterField(
            model_name='school',
            name='title',
            field=models.CharField(max_length=32, verbose_name='校区名称'),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('email', models.CharField(max_length=32, verbose_name='邮箱')),
                ('nickname', models.CharField(max_length=16, verbose_name='姓名')),
                ('phone', models.CharField(max_length=32, verbose_name='手机号')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Department', verbose_name='部门')),
                ('roles', models.ManyToManyField(blank=True, to='rbac.Role', verbose_name='拥有的所有角色')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
