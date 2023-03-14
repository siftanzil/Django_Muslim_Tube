# Generated by Django 4.1.7 on 2023-03-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Video', '0004_category_alter_video_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.CharField(choices=[('Quran', 'Quran'), ('Hadith', 'Hadith'), ('Fiqh', 'Fiqh'), ('Heart Softener', 'Heart Softener'), ('Biography', 'Biography'), ('Debate', 'Debate'), ('Dawah', 'Dawah')], default='Islamic', max_length=255),
        ),
    ]
