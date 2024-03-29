# Generated by Django 4.0.2 on 2022-02-08 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('identificacion', models.BigIntegerField(primary_key=True, serialize=False)),
                ('apellidos', models.CharField(max_length=100)),
                ('nombres', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('identificacion', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pagaduria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.BigIntegerField()),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_tarjeta', models.BigIntegerField()),
                ('clave', models.CharField(max_length=4)),
                ('cuota', models.BigIntegerField(blank=True, null=True)),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarjeta.banco')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarjeta.cliente')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarjeta.empresa')),
                ('pagaduria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarjeta.pagaduria')),
            ],
        ),
    ]
