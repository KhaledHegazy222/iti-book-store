# Generated by Django 4.2.5 on 2023-09-21 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('Available', 'Available'), ('Taken', 'Taken')], max_length=10)),
                ('return_date', models.DateField()),
                ('price', models.FloatField()),
                ('borrowing_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.buser')),
            ],
        ),
    ]