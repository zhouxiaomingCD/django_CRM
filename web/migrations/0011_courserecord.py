# Generated by Django 2.2 on 2019-08-23 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_student_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_num', models.IntegerField(verbose_name='节次')),
                ('date', models.DateField(auto_now_add=True, verbose_name='上课日期')),
                ('class_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ClassList', verbose_name='班级')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserInfo', verbose_name='讲师')),
            ],
        ),
    ]
