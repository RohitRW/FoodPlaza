from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodapp', '0003_auto_20190821_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('AdminId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('AdminPass', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'FP_Admin',
            },
        ),
    ]
