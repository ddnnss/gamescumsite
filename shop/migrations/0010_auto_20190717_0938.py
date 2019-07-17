# Generated by Django 2.1.4 on 2019-07-17 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20190715_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setimage',
            name='set',
        ),
        migrations.RemoveField(
            model_name='set',
            name='name_lower',
        ),
        migrations.RemoveField(
            model_name='set',
            name='spawn_commands',
        ),
        migrations.AddField(
            model_name='items',
            name='set',
            field=models.ManyToManyField(blank=True, null=True, to='shop.Set', verbose_name='В составе сета'),
        ),
        migrations.AddField(
            model_name='subitem',
            name='set',
            field=models.ManyToManyField(blank=True, null=True, to='shop.Set', verbose_name='В составе сета'),
        ),
        migrations.AlterField(
            model_name='baskets',
            name='item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Items'),
        ),
        migrations.DeleteModel(
            name='SetImage',
        ),
    ]