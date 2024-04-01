# Generated by Django 5.0 on 2024-03-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrecipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('electronics', 'Electronics'), ('clothing', 'Clothing'), ('books', 'Books')], max_length=50)),
            ],
        ),
    ]
