# Generated by Django 2.2.12 on 2024-03-19 13:33

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app3_p5678_tp_men_group', to='otree.Session')),
            ],
            options={
                'db_table': 'app3_p5678_TP_men_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='app3_p5678_tp_men_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'app3_p5678_TP_men_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('treatment', otree.db.models.StringField(max_length=10000, null=True)),
                ('ctrq1_1', otree.db.models.StringField(choices=[('2 and 3', '2 and 3'), ('3 and 6', '3 and 6'), ('4 and 6', '4 and 6')], max_length=10000, null=True, verbose_name='Question 1: Assuming that the special rule does not apply, who are the two winners?')),
                ('ctrq1_2', otree.db.models.StringField(choices=[('2 and 3', '2 and 3'), ('3 and 6', '3 and 6'), ('4 and 6', '4 and 6')], max_length=10000, null=True, verbose_name='Question 2: Assuming that the special rule applies, who are the two winners?')),
                ('ctrq2_1', otree.db.models.StringField(choices=[('3 and 4', '3 and 4'), ('1 and 6', '1 and 6'), ('5 and 6', '5 and 6')], max_length=10000, null=True, verbose_name='Question 3: Assuming that the special rule does not apply, who are the two winners?')),
                ('ctrq2_2', otree.db.models.StringField(choices=[('3 and 4', '3 and 4'), ('1 and 6', '1 and 6'), ('5 and 6', '5 and 6')], max_length=10000, null=True, verbose_name='Question 4: Assuming that the special rule applies, who are the two winners?')),
                ('aa_choice', otree.db.models.StringField(choices=[('Apply the special rule', 'Apply the special rule'), ('Do not apply the special rule', 'Do not apply the special rule')], max_length=10000, null=True, verbose_name='')),
                ('belief1_tp', otree.db.models.StringField(choices=[('Less likely', 'Less likely'), ('Equally likely', 'Equally likely'), ('More likely', 'More likely')], max_length=10000, null=True, verbose_name='')),
                ('belief2_tp', otree.db.models.IntegerField(null=True, verbose_name='')),
                ('belief3_tp', otree.db.models.IntegerField(null=True, verbose_name='')),
                ('attention_check1', otree.db.models.StringField(max_length=10000, null=True, verbose_name='Question: What is your favorite city?')),
                ('attention_check2', otree.db.models.StringField(choices=[('Less likely', 'Less likely'), ('Equally likely', 'Equally likely'), ('More likely', 'More likely')], max_length=10000, null=True, verbose_name='')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app3_p5678_TP_men.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app3_p5678_tp_men_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app3_p5678_tp_men_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app3_p5678_TP_men.Subsession')),
            ],
            options={
                'db_table': 'app3_p5678_TP_men_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app3_p5678_TP_men.Subsession'),
        ),
    ]
