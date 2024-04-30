# Generated by Django 5.0.4 on 2024-04-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aweme_id', models.CharField(max_length=100, unique=True)),
                ('aweme_type', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=500)),
                ('create_time', models.BigIntegerField()),
                ('user_id', models.CharField(max_length=100)),
                ('sec_uid', models.CharField(max_length=100)),
                ('short_user_id', models.CharField(max_length=100)),
                ('user_unique_id', models.CharField(max_length=100)),
                ('user_signature', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=200)),
                ('liked_count', models.CharField(max_length=100)),
                ('collected_count', models.CharField(max_length=100)),
                ('comment_count', models.CharField(max_length=100)),
                ('share_count', models.CharField(max_length=100)),
                ('ip_location', models.CharField(max_length=100)),
                ('last_modify_ts', models.BigIntegerField()),
                ('cover', models.CharField(max_length=200)),
                ('aweme_url', models.CharField(max_length=200)),
            ],
        ),
    ]