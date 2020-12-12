# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:41:29 2020

@author: jenpr
"""

"""printing game text more slowly"""


    
def slowdown(stg):
    import sys
    import time
    """stg = string; x = float, optional, c= letters"""
    for c in stg + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1/30)
    return ""
            
if __name__ == "__main__":
  slowdown("This is a test of slowprint")