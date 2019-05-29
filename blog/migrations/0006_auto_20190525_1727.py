# Generated by Django 2.2.1 on 2019-05-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190525_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='post',
            field=models.ForeignKey(on_delete='CASCADE', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
