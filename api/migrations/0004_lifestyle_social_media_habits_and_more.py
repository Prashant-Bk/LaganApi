# Generated by Django 5.1.4 on 2024-12-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_partnerpreference_is_living_in_foreign_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifestyle',
            name='social_media_habits',
            field=models.CharField(choices=[('usual', 'Usual'), ('addicted', 'Addicted'), ('avoidant', 'Avoidant'), ('none', 'None')], default='usual', help_text='Describe your social media usage habits.', max_length=20, verbose_name='Social Media Habits'),
        ),
        migrations.AlterField(
            model_name='interests',
            name='favorite_books_genres',
            field=models.TextField(blank=True, null=True, verbose_name='Favorite Books Generes'),
        ),
    ]
