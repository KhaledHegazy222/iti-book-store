# Generated by Django 4.2.5 on 2023-09-21 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowing_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.buser'),
        ),
    ]
