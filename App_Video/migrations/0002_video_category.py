# Generated by Django 4.1.7 on 2023-03-13 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.CharField(choices=[('Quran', 'Quran'), ('Hadith', 'Hadith'), ('Fiqh', 'Fiqh'), ('Heart Softener', 'Heart Softener'), ('Biography', 'Biography'), ('Debate', 'Debate'), ('Dawah', 'Dawah')], default='Others', max_length=21),
        ),
    ]
