#!/bin/python3
"""
Author: Ronald Johnson
Date: 9-22-2025
License: GPLv3
link: https://www.gnu.org/licenses/quick-guide-gplv3.html
This code takes CVSS vectors and computes them.
The vectors are then matched against host data to determine weight and priority.
The risk will be calculated once the host data has been calculated.
The map will be graphed nodes of different colors indicating a progressive path to a goal with a suggested implementation of a vulnerability per host.
"""
import logging
import random
from logging import log
from ipaddress import ip_network


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
        
class HostCalculation:
    def __init__(self):
        self.local_total_vulnerability = 0
        self.adjacent_host_vulnerability = 0
        self.ring_fence = 0
        self.neighbors_away_from_public = 0
        self.business_critical = 0
        self.asset_loss_cost = 0
        self.asset_loss_probability = 0
        self.asset_recovery_speed = 0
        self.asset_data_hours_lost_when_recovered = 0
        self.node_hardness = 0

class AttackChainMembers:
    def __init__(self):
        self.hosts = {}
        self.ip_chain = {}
        self.vulnerability_correlations = {}
        self.cost_to_implement_attack = 0
        self.price_to_implement_attack = 0
        self.hours_to_perform_breach = 0
        self.attack_team_members = {}
        self.attack_chain_delivered_to_red_team = True
        self.blue_team_prepared_for_exercise = True
        self.host_cartography_complete = True
        self.exercise_status = 'augmetics active, bionics online, psy-booster 100%, mind impulse unit link active.'

if __name__=='__main__':
    #create 126 host IP network
    test_net = list(ip_network('192.168.1.0/25').hosts())
    # build up a random Base Score Metric for each host.
    # Exploitability Metrics
    av = ['P', 'L', 'A', 'N']
    ac = ['H', 'L']
    pr = ['H', 'L', 'N']
    ui = ['R', 'N']
    # scope
    ms = ['U', 'C']
    # confidentiality impact metrics
    mc = ['N', 'L', 'H']
    # integrity impact metrics
    mi = ['N', 'L', 'H']
    # availability impact metrics
    ma = ['N', 'L', 'H']
    vector_one = "CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:H/A:L"
    vector_dictionary = {}
    node_path = {}
    alternate_node_paths = {}
    hosts_collection = {}
    count_vector = 0
    vector_limit = 10000
    while count_vector < vector_limit:
        try:
            for host in test_net:
                AV = 'AV:' + random.choice(av)
                AC = 'AC:' + random.choice(ac)
                PR = 'PR:' + random.choice(pr)
                UI = 'UI:' + random.choice(ui)
                MS = 'MS:' + random.choice(ms)
                MC = 'MC:' + random.choice(mc)
                MI = 'MI:' + random.choice(mi)
                MA = 'MA:' + random.choice(ma)
                hosts_collection[host] = [AV, AC, PR, UI, MS, MC, MI, MA]

            for i in vector_one.split(sep='/'):
                j = i.split(sep=':')
                vector_dictionary[j[0]] = j[1]


        except Exception as e:
            logging.info(e)
            print('Reason:', e)
            break
        finally:
            print(f'Vector results: {vector_dictionary}')


    def

