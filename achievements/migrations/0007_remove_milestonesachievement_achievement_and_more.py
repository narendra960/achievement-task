# Generated by Django 5.1.3 on 2024-11-06 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0006_alter_milestones_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='milestonesachievement',
            name='achievement',
        ),
        migrations.DeleteModel(
            name='AchievementStep',
        ),
        migrations.DeleteModel(
            name='MilestonesAchievement',
        ),
    ]
