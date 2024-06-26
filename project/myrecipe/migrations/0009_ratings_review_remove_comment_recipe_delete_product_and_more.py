# Generated by Django 5.0 on 2024-03-31 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrecipe', '0008_comment_delete_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=250)),
                ('rating', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myrecipe.fooddetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myrecipe.logindetails')),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='recipe',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='ratings',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myrecipe.review'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
