# Generated by Django 2.1.4 on 2018-12-19 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTemplates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, null=True)),
                ('image', models.ImageField(default=None, null=True, upload_to='events/')),
                ('info', models.TextField(default='')),
                ('reward', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'Шаблон мероприятия',
                'verbose_name_plural': 'Шаблоны мероприятий',
            },
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Мероприятие', 'verbose_name_plural': 'Мероприятия'},
        ),
        migrations.RemoveField(
            model_name='event',
            name='name',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='event',
            name='template',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.EventTemplates'),
        ),
    ]