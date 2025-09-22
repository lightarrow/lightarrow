#!/bin/python3
"""
Author: Ronald Johnson
Date: 9-22-2025
License: GPLv3
link: https://www.gnu.org/licenses/quick-guide-gplv3.html
"""
class AttackVector:
    def __init__(self,physical, local, adjacent, network):
        self.physical = 0.20
        self.local = 0.55
        self.adjacent = 0.62
        self.network = 0.85

class AttackComplexity:
    def __init__(self,low, high):
        self.high = 0.44
        self.low = 0.77

class PrivilegesRequired:
    def __init__(self,low, high):
        self.low = 0.62
        self.high = 0.27
        self.none = 0.85



if __name__=='__main__':