# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 18:19:19 2025

@author: Bastien Bégon
"""

import megaind

class SMMegaInd:
    """
    Sequent Microsystems Industrial Automation Hat wrapper class
    """
    def __init__(self, stack):
        self.open_connection(stack)

    def open_connection(self, stack):
        self.stack = stack
        self.set_all_to_0()
        
    def close_connection(self):
        self.set_all_to_0()
    
    def set_all_to_0(self):
        # Set all analog outputs to O
        for channel in range(1, 5):
            megaind.set0_10Out(self.stack, channel, 0)

        # Set all open-drain outputs to 0 → todo
        # Set 4-20mA outputs to 0 → todo
    
    def check_connection(self):
        return megaind.checkStack(self.stack)
    
    # 0-10 V Analog Outputs
    def get_0_10_out(self, channel):
        return megaind.get0_10Out(self.stack, channel)
    
    def set_0_10_out(self, channel, value):
        return megaind.set0_10Out(self.stack, channel, value)
    
    def set_0_10_out_rel(self, channel, value):
        previous_value = megaind.get0_10Out(self.stack, channel)
        return megaind.set0_10Out(self.stack, channel, previous_value + value)
    
    # 0-10 V Analaog Inputs
    def get_0_10_in(self, channel):
        return megaind.get0_10In(self.stack, channel)
    
    # Open Drain Outputs
    def set_od(self, channel, value):
        return megaind.setOd(self.stack, channel, value)

    def get_od(self, channel):
        return megaind.getOd(self.stack, channel)
    
    def set_od_pwm(self, channel, value):
        return megaind.setOdPWM(self.stack, channel, value)
    
    def get_od_pwm(self, channel):
        return megaind.getOdPWM(self.stack, channel)
    
    def set_od_pwm_rel(self, channel, value):
        previous_value = megaind.getOdPWM(self.stack, channel)
        return megaind.setOdPWM(self.stack, channel, previous_value + value)


if __name__ == "__main__":
    smmegaind = SMMegaInd(0)

    smmegaind.set0_10Out(1, 0)
    print(smmegaind.get0_10Out(1))