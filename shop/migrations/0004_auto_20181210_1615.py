# Generated by Django 2.1.4 on 2018-12-10 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20181210_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Categories'),
        ),
        migrations.AlterField(
            model_name='items',
            name='info',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]