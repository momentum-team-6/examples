# Generated by Django 3.1.4 on 2020-12-17 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Square',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=1)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('K', 'King'), ('Q', 'Queen'), ('B', 'Bishop'), ('P', 'Pawn'), ('R', 'Rook'), ('KN', 'Knight')], max_length=10)),
                ('rule', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('BL', 'Black'), ('WH', 'White')], max_length=10)),
                ('square', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='game.square')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.type')),
            ],
        ),
    ]
