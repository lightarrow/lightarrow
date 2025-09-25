import random
from ipaddress import ip_network
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

hosts_collection.keys()
hosts_collection.values()