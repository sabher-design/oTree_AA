# Generated by Django 2.2.12 on 2024-03-21 10:48

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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app5_p1112_quest_men_group', to='otree.Session')),
            ],
            options={
                'db_table': 'app5_p1112_quest_men_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='app5_p1112_quest_men_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'app5_p1112_quest_men_subsession',
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
                ('aa_rand', otree.db.models.StringField(max_length=10000, null=True)),
                ('ingroup1_info', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True, verbose_name='How much are you willing to help a tournament participant who is female?')),
                ('ingroup2_info', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True, verbose_name='How much are you willing to help a tournament participant who is male?')),
                ('ingroup3_info', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True, verbose_name='How much do you identify yourself with tournament participants who are female?')),
                ('ingroup4_info', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True, verbose_name='How much do you identify yourself with tournament participants who are male?')),
                ('ingroup1_specs', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True, verbose_name='How much are you willing to help a tournament participant who is female?')),
                ('ingroup2_specs', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True, verbose_name='How much are you willing to help a tournament participant who is male?')),
                ('ingroup3_specs', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True, verbose_name='How much do you identify yourself with tournament participants who are female?')),
                ('ingroup4_specs', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True, verbose_name='How much do you identify yourself with tournament participants who are male?')),
                ('smiley1', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='To tournament participant 1 (Woman) ')),
                ('smiley2', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='To tournament participant 2 (Woman) ')),
                ('smiley3', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='To tournament participant 3 (Woman) ')),
                ('smiley4', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='To tournament participant 4 (Man)  ')),
                ('smiley5', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='To tournament participant 5 (Man)  ')),
                ('smiley6', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='To tournament participant 6 (Man)  ')),
                ('aa_favor1', otree.db.models.StringField(choices=[('Favor', 'Favor'), ('Oppose', 'Oppose'), ('No opinion', 'No opinion')], max_length=10000, null=True, verbose_name='Do you generally favor or oppose affirmative action programs for women?')),
                ('aa_favor2', otree.db.models.StringField(choices=[('Favor', 'Favor'), ('Oppose', 'Oppose'), ('No opinion', 'No opinion')], max_length=10000, null=True, verbose_name='Do you generally favor or oppose affirmative action programs for racial minorities?')),
                ('aa_favor3', otree.db.models.StringField(choices=[('Favor', 'Favor'), ('Oppose', 'Oppose'), ('No opinion', 'No opinion')], max_length=10000, null=True, verbose_name='Do you generally favor or oppose affirmative action programs for people with disabilities?')),
                ('risk', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name=' \n        How do you see yourself? \n        Are you generally a person who is fully prepared to take risks or do you try to avoid taking risks? \n        Please tick a box on the scale, where the value 0 means: ‘unwilling to take risks’ and the value 10 means: ‘fully prepared to take risk’.')),
                ('social', otree.db.models.IntegerField(null=True, verbose_name='\n        Imagine the following situation:\n        Today you unexpectedly received 1,000 USD. How much of this amount would you donate to a good cause?')),
                ('gender', otree.db.models.StringField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Diverse', 'Diverse')], max_length=10000, null=True, verbose_name='What is your gender?')),
                ('gender_diverse', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='If you answered Diverse:')),
                ('age', otree.db.models.IntegerField(null=True, verbose_name='What is your age?')),
                ('employment', otree.db.models.StringField(choices=[('Full-time employee', 'Full-time employee'), ('Part-time employee', 'Part-time employee'), ('Retired', 'Retired'), ('Student', 'Student'), ('Self-employed or business owner', 'Self-employed or business owner'), ('Unemployed and looking for work', 'Unemployed and looking for work'), ('Not working and not currently looking for work', 'Not working and not currently looking for work')], max_length=10000, null=True, verbose_name='What is your employment status?')),
                ('socialclass', otree.db.models.StringField(choices=[('Lower Class or Poor', 'Lower Class or Poor'), ('Working Class', 'Working Class'), ('Middle Class', 'Middle Class'), ('Upper-middle Class', 'Upper-middle Class'), ('Upper Class', 'Upper Class')], max_length=10000, null=True, verbose_name='\n        If you had to use one of these five commonly-used names \n        to describe your social class, which one would it be?')),
                ('children', otree.db.models.IntegerField(null=True, verbose_name='How many children do you have?')),
                ('income', otree.db.models.StringField(choices=[('Less than $5,000', 'Less than $5,000'), ('$5,000 to $7,499', '$5,000 to $7,499'), ('$7,500 to $9,999', '$7,500 to $9,999'), ('$10,000 to $12,499', '$10,000 to $12,499'), ('$12,500 to $14,999', '$12,500 to $14,999'), ('$15,000 to $19,999', '$15,000 to $19,999'), ('$20,000 to $24,999', '$20,000 to $24,999'), ('$25,000 to $29,999', '$25,000 to $29,999'), ('$30,000 to $34,999', '$30,000 to $34,999'), ('$35,000to $39,999', '$35,000to $39,999'), ('$40,000 to $49,999', '$40,000 to $49,999'), ('$50,000 to $59,999', '$50,000 to $59,999'), ('$60,000 to $74,999', '$60,000 to $74,999'), ('$75,000 to $99,999', '$75,000 to $99,999'), ('$100,000 to $149,999', '$100,000 to $149,999'), ('$150,000 or more', '$150,000 or more')], max_length=10000, null=True, verbose_name='\n        Which category represents your total combined household income during the past 12 months? \n        This includes money from jobs, net income from business, farm or rent, pensions, dividends, interests, \n        social security payments and any other money income received.')),
                ('household_children', otree.db.models.IntegerField(null=True, verbose_name='How many children does your household have?')),
                ('household_adults', otree.db.models.IntegerField(null=True, verbose_name='How many adults does your household have?')),
                ('ethnicity', otree.db.models.StringField(choices=[('White', 'White'), ('Hispanic', 'Hispanic'), ('Latino or Spanish origin', 'Latino or Spanish origin'), ('Black or African American', 'Black or African American'), ('American Indian', 'American Indian'), ('Alaska Native', 'Alaska Native'), ('Native American', 'Native American'), ('Asian', 'Asian'), ('Pacific Islander', 'Pacific Islander'), ('Other', 'Other')], max_length=10000, null=True, verbose_name='What is your ethnicity or cultural background?')),
                ('ethnicity_other', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='If you selected Other:')),
                ('mother_tongue', otree.db.models.StringField(max_length=10000, null=True, verbose_name='What is your mother tongue(s)?')),
                ('IQ', otree.db.models.StringField(choices=[('No high school diploma', 'No high school diploma'), ('High school diploma or equivalent', 'High school diploma or equivalent'), ('Some college but no degree', 'Some college but no degree'), ('Associate degree in college (2-year college)', 'Associate degree in college (2-year college)'), ("Bachelor's degree (4-year college)", "Bachelor's degree (4-year college)"), ("Master's degree (For example: MA, MS, MEng, MEd, MSW, MBA)", "Master's degree (For example: MA, MS, MEng, MEd, MSW, MBA)"), ('Professional School Degree or Doctorate Degree (For example: MD, DDS,DVM,LLB,JD, PhD, EdD)', 'Professional School Degree or Doctorate Degree (For example: MD, DDS,DVM,LLB,JD, PhD, EdD)')], max_length=10000, null=True, verbose_name='What is the highest level of school you \n        have completed or the highest degree you have received?')),
                ('sexual_orientation', otree.db.models.StringField(choices=[('Heterosexual', 'Heterosexual'), ('Homosexual', 'Homosexual'), ('Other', 'Other'), ('Prefer not to say', 'Prefer not to say')], max_length=10000, null=True, verbose_name='What is your sexual orientation?')),
                ('sexual_orientation_other', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='If you selected Other:')),
                ('political', otree.db.models.StringField(choices=[('Extremely liberal', 'Extremely liberal'), ('Liberal', 'Liberal'), ('Slightly liberal', 'Slightly liberal'), ('Moderate, middle of the road', 'Moderate, middle of the road'), ('Slightly conservative', 'Slightly conservative'), ('Conservative', 'Conservative'), ('Extremely conservative', 'Extremely conservative')], max_length=10000, null=True, verbose_name='We hear a lot of talk these days about ‘liberals’ and ‘conservatives’. \n        Here is a 7-point-scale on which people’s political views are arranged \n        from extremely liberal to extremely conservative. \n        Where would you place yourself on this scale?')),
                ('discrimination', otree.db.models.StringField(choices=[('Yes – very often', 'Yes – very often'), ('Yes – often', 'Yes – often'), ('Yes – sometimes', 'Yes – sometimes'), ('Yes – rarely', 'Yes – rarely'), ('No – never', 'No – never')], max_length=10000, null=True, verbose_name='Have you ever experienced discrimination because of your race, \n        ethnicity, gender, age, religion, physical appearance, \n        sexual orientation, or other characteristics?')),
                ('token_1', otree.db.models.IntegerField(null=True, verbose_name='')),
                ('token_2', otree.db.models.IntegerField(null=True, verbose_name='')),
                ('fairness_AA', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True, verbose_name='')),
                ('fairness_noAA', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True, verbose_name='')),
                ('quiz1', otree.db.models.StringField(choices=[('Barcelona', 'Barcelona'), ('Paris', 'Paris')], max_length=10000, null=True, verbose_name='What is the capital city of France?')),
                ('quiz2', otree.db.models.StringField(choices=[('500kg', '500kg'), ('50kg', '50kg')], max_length=10000, null=True, verbose_name='How much does an average chimpanzee weigh?')),
                ('quiz3', otree.db.models.StringField(choices=[('Jackson Pollock', 'Jackson Pollock'), ('Vincent van Gogh', 'Vincent van Gogh')], max_length=10000, null=True, verbose_name=' "The starry night" is a famous painting by...')),
                ('quiz4', otree.db.models.StringField(choices=[('Italian', 'Italian'), ('French', 'French')], max_length=10000, null=True, verbose_name=' "Verre" means "glass" in which language?')),
                ('quiz5', otree.db.models.StringField(choices=[('Antwerp', 'Antwerp'), ('Rotterdam', 'Rotterdam')], max_length=10000, null=True, verbose_name='Amsterdam is nearer to?')),
                ('quiz6', otree.db.models.StringField(choices=[('Waikiki', 'Waikiki'), ('Honolulu', 'Honolulu')], max_length=10000, null=True, verbose_name='The capital of Hawaii is...')),
                ('quiz7', otree.db.models.StringField(choices=[('The London Eye', 'The London Eye'), ('The Eiffel Tower', 'The Eiffel Tower')], max_length=10000, null=True, verbose_name='Which weighs more?')),
                ('quiz8', otree.db.models.StringField(choices=[('Russian', 'Russian'), ('German', 'German')], max_length=10000, null=True, verbose_name=' "Kieselstein" means "pebble" in which language?')),
                ('quiz9', otree.db.models.StringField(choices=[('Leonardo da Vinci', 'Leonardo da Vinci'), ('Michelangelo', 'Michelangelo')], max_length=10000, null=True, verbose_name=' "The Creation of Adam" is a painting by...')),
                ('quiz10', otree.db.models.StringField(choices=[('Serbian', 'Serbian'), ('Norwegian', 'Norwegian')], max_length=10000, null=True, verbose_name=' "Dronning" means "queen" in which language?')),
                ('your_rank', otree.db.models.IntegerField(null=True)),
                ('attention_check3', otree.db.models.StringField(choices=[('Wine', 'Wine'), ('Beer', 'Beer'), ('Whiskey', 'Whiskey'), ('Carrot juice', 'Carrot juice'), ('Vodka', 'Vodka'), ('Other', 'Other')], max_length=10000, null=True, verbose_name='')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app5_p1112_quest_men.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app5_p1112_quest_men_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app5_p1112_quest_men_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app5_p1112_quest_men.Subsession')),
            ],
            options={
                'db_table': 'app5_p1112_quest_men_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app5_p1112_quest_men.Subsession'),
        ),
    ]
