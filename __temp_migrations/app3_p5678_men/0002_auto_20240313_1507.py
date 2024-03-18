# Generated by Django 2.2.12 on 2024-03-13 14:07

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('app3_p5678_men', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='belief4_specs',
            field=otree.db.models.StringField(choices=[('With the special rule, both groups have about the same chance', 'With the special rule, both groups have about the same chance'), ('With the special rule, the men have a higher chance of winning than women', 'With the special rule, the men have a higher chance of winning than women'), ('With the special rule, the women have a higher chance of winning than men', 'With the special rule, the women have a higher chance of winning than men')], max_length=10000, null=True, verbose_name=''),
        ),
    ]