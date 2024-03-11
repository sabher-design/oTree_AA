from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class p5_INFOGreen(Page):
      def is_displayed(self):
        if self.player.treatment == 'INFO' and self.player.color == 'Green':
             return True
        else:
             return False

class p5_INFOBlue(Page):
      def is_displayed(self):
        if self.player.treatment == 'INFO' and self.player.color == 'Blue':
             return True
        else:
             return False            

class p5_SPEC(Page):
    def is_displayed(self):
        if self.player.treatment == 'SPEC':
             return True
        else:
             return False

class p5_SPECG(Page):
    def is_displayed(self):
        if self.player.treatment == 'SPECG':
             return True
        else:
             return False

class p6a_INFO(Page):
      def is_displayed(self):
        if self.player.treatment == 'INFO':
             return True
        else:
             return False

class p6a_SPECnSPECG(Page):
    def is_displayed(self):
        if self.player.treatment == 'SPEC' or self.player.treatment == 'SPECG':
             return True
        else:
             return False

class p6b1(Page):
     form_model = 'player'
     form_fields = ['ctrq1_1','ctrq1_2']

class p6b2_1(Page):
     def is_displayed(self):
        if self.player.ctrq1_1== '3 and 6' and self.player.ctrq1_2 == '3 and 6':
             return True
        else:
             return False

class p6b2_2(Page):
    def is_displayed(self):
        if self.player.ctrq1_1 == '3 and 6' and self.player.ctrq1_2 != '3 and 6':
             return True
        else:
             return False

class p6b2_3(Page):
    def is_displayed(self):
        if self.player.ctrq1_1 != '3 and 6' and self.player.ctrq1_2 == '3 and 6':
             return True
        else:
             return False
class p6b2_4(Page):
    def is_displayed(self):
        if self.player.ctrq1_1 != '3 and 6' and self.player.ctrq1_2 != '3 and 6':
             return True
        else:
             return False

class p6b3(Page):
     form_model = 'player'
     form_fields = ['ctrq2_1','ctrq2_2']

class p6b4_1(Page):
     def is_displayed(self):
        if self.player.ctrq2_1 == '5 and 6' and self.player.ctrq2_2 == '1 and 6':
             return True
        else:
             return False

class p6b4_2(Page):
    def is_displayed(self):
        if self.player.ctrq2_1 == '5 and 6' and self.player.ctrq2_2 != '1 and 6':
             return True
        else:
             return False

class p6b4_3(Page):
    def is_displayed(self):
        if self.player.ctrq2_1 != '5 and 6' and self.player.ctrq2_2 == '1 and 6':
             return True
        else:
             return False
class p6b4_4(Page):
    def is_displayed(self):
        if self.player.ctrq2_1 != '5 and 6' and self.player.ctrq2_2 != '1 and 6':
             return True
        else:
             return False

class p7(Page):
     form_model = 'player'
     form_fields = ['aa_choice']

class p8_INFO(Page):
     form_model = 'player'
     form_fields = ['belief1_info', 'belief2_info', 'belief3_info', 'attention_check2']

     def is_displayed(self):
        if self.player.treatment == 'INFO':
             return True
        else:
             return False
  

class p8a_SPECG(Page):
     form_model = 'player'
     form_fields = ['belief1_specs', 'belief2_specs', 'belief3_specg', 'belief4_specs', 'attention_check2']

     def is_displayed(self):
        if self.player.treatment == 'SPECG':
             return True
        else:
             return False

class p8a_SPEC(Page):
     form_model = 'player'
     form_fields = ['belief1_specs', 'belief2_specs', 'belief3_g_spec', 'belief3_b_spec','belief4_specs', 'attention_check2']

     def is_displayed(self):
        if self.player.treatment == 'SPEC':
             return True
        else:
             return False
     
class p8b_SPECnSPECG(Page):
     form_model = 'player'
     form_fields = ['belief5_specs', 'belief6_specs', 'belief7_specs', 'belief8_specs']

     def is_displayed(self):
        if self.player.treatment == 'SPEC' or self.player.treatment == 'SPECG':
             return True
        else:
             return False
     
class p8c_SPECnSPECG(Page):
     form_model = 'player'
     form_fields = ['belief9_specs', 'belief10_specs', 'belief11_specs', 'belief12_specs']

     def is_displayed(self):
        if self.player.treatment == 'SPEC' or self.player.treatment == 'SPECG':
             return True
        else:
             return False


class attention_check1(Page):
    form_model = 'player'
    form_fields = ['attention_check1']


page_sequence = [p5_INFOGreen, p5_INFOBlue, p5_SPEC, p5_SPECG, p6a_INFO, p6a_SPECnSPECG, attention_check1, 
p6b1, p6b2_1, p6b2_2, p6b2_3, p6b2_4, p6b3, p6b4_1, p6b4_2, p6b4_3, p6b4_4, p7, p8_INFO, p8a_SPEC, 
p8a_SPECG, p8b_SPECnSPECG, p8c_SPECnSPECG]

#page_sequence = [p8_INFO, p8a_SPEC, p8a_SPECG]