# Generated by Django 4.2.7 on 2023-11-27 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Portfel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CeleOszczednosciowe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cel', models.CharField(max_length=100)),
                ('kwotaUzbierana', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kwotaCel', models.DecimalField(decimal_places=2, max_digits=10)),
                ('IDPorfela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portfel.portfel')),
            ],
        ),
    ]
