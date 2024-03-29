# Generated by Django 2.2 on 2019-08-23 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20190822_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qq', models.CharField(max_length=32, verbose_name='QQ号')),
                ('mobile', models.CharField(max_length=32, verbose_name='手机号')),
                ('emergency_contract', models.CharField(max_length=32, verbose_name='紧急联系人电话')),
                ('student_status', models.IntegerField(choices=[(1, '申请中'), (2, '在读'), (3, '毕业'), (4, '退学')], default=1, verbose_name='学员状态')),
                ('memo', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
                ('class_list', models.ManyToManyField(blank=True, null=True, to='web.ClassList', verbose_name='已报班级')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.Customer', verbose_name='客户信息')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_type', models.IntegerField(choices=[(1, '报名费'), (2, '学费'), (3, '退学'), (4, '其他')], default=1, verbose_name='费用类型')),
                ('paid_fee', models.IntegerField(default=0, verbose_name='金额')),
                ('apply_date', models.DateTimeField(auto_now_add=True, verbose_name='申请日期')),
                ('confirm_status', models.IntegerField(choices=[(1, '申请中'), (2, '已确认'), (3, '已驳回')], default=1, verbose_name='确认状态')),
                ('confirm_date', models.DateTimeField(blank=True, null=True, verbose_name='确认日期')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('class_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ClassList', verbose_name='申请班级')),
                ('confirm_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirms', to='web.UserInfo', verbose_name='审批人')),
                ('consultant', models.ForeignKey(help_text='谁签的单就选谁', on_delete=django.db.models.deletion.CASCADE, to='web.UserInfo', verbose_name='课程顾问')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Customer', verbose_name='客户')),
            ],
        ),
    ]
