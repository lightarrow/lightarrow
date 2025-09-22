#!/bin/python3
"""
Author: Ronald Johnson
Date: 9-22-2025
License: GPLv3
link: https://www.gnu.org/licenses/quick-guide-gplv3.html
This code takes CVSS version 3.x vectors and computes them.
The vectors are then matched against host data to determine weight and priority.
The risk will be calculated once the host data has been calculated.
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
        self.no_auth = 0.85

class UserInteractionMetric:
    def __init__(self,no_interaction, required_interaction):
        self.no_interaction = 0.85
        self.required_interaction = 0.62


class ConfidentialityImpactMetric:
    def __init__(self,low, high):
        self.no_impact = 0.00
        self.low = 0.22
        self.high = 0.56

class AvailabilityImpactMetric:
    def __init__(self,low, high):
        self.no_impact = 0.00
        self.low = 0.22
        self.high = 0.56

class Scope:
    def __init__(self,unchanged, changed):
        self.changed = False
        self.unchanged = False

class InterpretVector:
    def __init__(self, vector, cvss_split):
        self.vector = vector
        self.cvss_split = None

class KnownExploitedVulnerability:
    def __init__(self,low, high):
        self.exploited = False

if __name__=='__main__':

    countVector = 0
    vector_limit = 20
    while countVector < vector_limit:

        try:
            my_vector = InterpretVector("CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:H/A:L", None)
        except:
            print(f'Except Error')
            break
        finally:
            print(f'Vector results: {my_vector.vector}')
            countVector += 1
