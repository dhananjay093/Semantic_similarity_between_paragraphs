# -*- coding: utf-8 -*-

"""
Created on Tue Apr 16 23:03:47 2024

@author: dhana
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    text1: str
    text2: str 
   