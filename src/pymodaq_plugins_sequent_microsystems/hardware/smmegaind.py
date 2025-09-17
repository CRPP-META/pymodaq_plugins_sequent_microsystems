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
        for channel in range(1, 5):
            megaind.set0_10Out(self.stack, channel, 0)

    def close_connection(self):
        for channel in range(1, 5):
            megaind.set0_10Out(self.stack, channel, 0)
    
    def check_connection(self):
        return megaind.checkStack(self.stack)
    
    def get0_10Out(self, channel):
        return megaind.get0_10Out(self.stack, channel)
    
    def set0_10Out(self, channel, value):
        return megaind.set0_10Out(self.stack, channel, value)
    
    def set0_10Out_rel(self, channel, value):
        V_old = megaind.get0_10Out(self.stack, channel)
        return megaind.set0_10Out(self.stack, channel, V_old + value)

if __name__ == "__main__":
    smmegaind = SMMegaInd(0)

    smmegaind.set0_10Out(1, 0)
    print(smmegaind.get0_10Out(1))