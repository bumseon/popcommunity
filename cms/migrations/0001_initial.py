# Generated by Django 2.1.2 on 2018-11-06 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='제목')),
                ('publisher', models.CharField(blank=True, max_length=100, verbose_name='작성자')),
                ('modify_date', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('clicks', models.IntegerField(blank=True, default=0, verbose_name='조회수')),
                ('up', models.IntegerField(blank=True, default=0, verbose_name='추천')),
                ('content', models.TextField(blank=True, verbose_name='내용')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replyname', models.CharField(blank=True, max_length=100, verbose_name='작성자')),
                ('comment', models.TextField(blank=True, verbose_name='댓글')),
                ('replymodify_date', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impressions', to='cms.Book', verbose_name='도서')),
            ],
        ),
    ]
