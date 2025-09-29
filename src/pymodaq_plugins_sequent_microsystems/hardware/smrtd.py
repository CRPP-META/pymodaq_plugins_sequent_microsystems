# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:18:11 2025

@author: Bastien Bégon
"""

import librtd

class SMRtd:
    """
    Sequent Microsystems RTD 8-channel Hat wrapper class
    """
    def __init__(self, stack):
        self.open_connection(stack)

    def open_connection(self, stack):
        self.stack = stack
        librtd.get(stack, 1)  # Only channel 1 (no need to check everything)
    
    def close_connection(self):
        pass
    
    def check_connection(self):
        librtd.get(self.stack, 1)

    def get_res(self, channel):
        return librtd.getRes(self.stack, channel)
    
    def get_temp(self, channel):
        return librtd.get(self.stack, channel)
    


if __name__ == "__main__":
    smrtd = SMRtd(stack=0)

    temp = smrtd.get_temp(5)
    print(temp)