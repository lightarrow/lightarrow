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
from logging import log


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
    impact_sub_score = 0
    my_vector = "CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:H/A:L"
    vector_two = "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"
    vector_four = "CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:L/SI:L/SA:L"
    vector_dictionary = {}
    count_vector = 0
    vector_limit = 1
    while count_vector < vector_limit:
        try:
            for i in my_vector.split(sep='/'):
                j = i.split(sep=':')
                vector_dictionary[j[0]] = j[1]
            count_vector += 1

        except Exception as e:
            log('Reason:', e)
            print('Reason:', e)
            break
        finally:
            print(f'Vector results: {vector_dictionary}')

