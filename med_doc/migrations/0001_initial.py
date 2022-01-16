# Generated by Django 3.2.9 on 2022-01-09 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateTimeField(verbose_name='Data wizyty')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Dodatkowe informacje')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='Podsumowanie')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created', to=settings.AUTH_USER_MODEL)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.patient')),
            ],
        ),
    ]
