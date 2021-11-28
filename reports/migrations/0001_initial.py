# Generated by Django 3.1.4 on 2021-11-28 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mailboxes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('overall', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('messages_counter', models.IntegerField()),
                ('mailbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailboxes.mailboxmodel')),
            ],
            options={
                'unique_together': {('name', 'mailbox')},
            },
        ),
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('sender', models.CharField(max_length=255)),
                ('to_recipients', models.CharField(max_length=255)),
                ('received_at', models.DateTimeField()),
                ('body', models.TextField()),
                ('folder', models.CharField(max_length=255)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='reports.reportmodel')),
            ],
        ),
        migrations.CreateModel(
            name='MessageEvaluationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spam_score', models.IntegerField()),
                ('spam_description', models.TextField()),
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='spam_evaluation', to='reports.messagemodel')),
            ],
        ),
    ]
