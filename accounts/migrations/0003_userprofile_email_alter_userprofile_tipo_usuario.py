# Generated by Django 5.1.3 on 2024-11-15 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_especialidad_delete_especialidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tipo_usuario',
            field=models.CharField(choices=[('paciente', 'Paciente'), ('profesional', 'Profesional')], max_length=19),
        ),
    ]