# Generated by Django 2.2.7 on 2020-02-03 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField()),
                ('requested_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_book', to='books.BookDetails')),
                ('requested_trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_trade', to='books.BookDetails')),
            ],
            options={
                'db_table': 'request_table',
            },
        ),
    ]