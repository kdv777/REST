# Generated by Django 3.2.8 on 2023-02-14 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20230211_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_set', to='todos.project'),
        ),
    ]
