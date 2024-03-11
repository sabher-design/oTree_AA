from os import environ

SESSION_CONFIGS = [
    dict(
       name='AAPref',
       display_name="AAPref",
       num_demo_participants=6,
       ###Testing:
       #app_sequence=['app1_p1234_intro_TP', 'app3_p5678_TP', 'app5_p1112_quest_TP']
       ###INFO, SPEC, SPECG:
       ###app_sequence=['app1_p1234_intro', 'app3_p5678']
       ###app_sequence=[ 'app1_p1234_intro','word_encryption_trial', 'app3_p5678','word_encryption', 'app5_p1112_quest']
       ###Tournament participants:
       #app_sequence=[ 'app1_p1234_intro_TP', 'word_encryption_trial_TP', 'app3_p5678_TP','word_encryption_round1','word_encryption_round2','word_encryption_round3',
        #              'word_encryption_round4','word_encryption_round5','word_encryption_round6', 'app5_p1112_quest_TP']
        app_sequence=['app1_p1234_intro_TP', 'app3_p5678_TP_men']
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '*8&1rr(yg4#^$*-z7zm#+_w-9y5wcg#mxpi-t!_$k+slk=(ii9'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']