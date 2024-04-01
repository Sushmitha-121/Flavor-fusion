# Generated by Django 5.0 on 2024-03-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fooddetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Recipe_Name', models.CharField(max_length=100)),
                ('Ingredients', models.TextField()),
                ('Cooking_process', models.TextField()),
                ('about_recipe', models.TextField()),
                ('origin', models.TextField()),
                ('servings', models.IntegerField()),
                ('Cooking_time', models.CharField(max_length=100)),
                ('author_Name', models.CharField(max_length=100)),
                ('Category', models.CharField(choices=[('Healthy_food', 'Healthy Food'), ('Chicken', 'Chicken'), ('Egg', 'Egg'), ('Veg_Recipe', 'Veg Recipe')], default='Healthy_food', max_length=50)),
                ('Recipe_image', models.ImageField(upload_to='static/recipe_img')),
            ],
        ),
        migrations.CreateModel(
            name='logindetails',
            fields=[
                ('user', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]
