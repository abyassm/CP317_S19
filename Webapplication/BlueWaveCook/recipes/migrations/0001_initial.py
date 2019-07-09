# Generated by Django 2.2.1 on 2019-07-09 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('calories', models.IntegerField()),
                ('image', models.ImageField(upload_to='recipes/static/images')),
                ('ingredients', models.CharField(max_length=1000)),
                ('instructions', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appetizer',
            fields=[
                ('recipe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recipes.Recipe')),
            ],
            bases=('recipes.recipe',),
        ),
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('recipe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recipes.Recipe')),
            ],
            bases=('recipes.recipe',),
        ),
        migrations.CreateModel(
            name='Meat',
            fields=[
                ('recipe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recipes.Recipe')),
            ],
            bases=('recipes.recipe',),
        ),
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('recipe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recipes.Recipe')),
            ],
            bases=('recipes.recipe',),
        ),
    ]
