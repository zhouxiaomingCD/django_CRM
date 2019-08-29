# Generated by Django 2.2 on 2019-08-21 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20190821_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveIntegerField(verbose_name='班级(期)')),
                ('price', models.PositiveIntegerField(verbose_name='学费')),
                ('start_date', models.DateField(verbose_name='开班日期')),
                ('graduate_date', models.DateField(blank=True, null=True, verbose_name='结业日期')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='说明')),
                ('class_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='web.UserInfo', verbose_name='班主任')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Course', verbose_name='课程名称')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.School', verbose_name='校区')),
                ('tech_teachers', models.ManyToManyField(blank=True, related_name='teach_classes', to='web.UserInfo', verbose_name='任课老师')),
            ],
        ),
    ]