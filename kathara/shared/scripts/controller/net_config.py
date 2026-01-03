# |=======================|
# | NETWORK CONFIGURATION |
# |=======================|

NET_CONFIG = {
        'subnets': [
            {'network': '10.0.0.0/24', 'port': 1, 'gw': '10.0.0.254', 'trusted': True, 'server': True, 'hpot': False},
            {'network': '10.0.1.0/24', 'port': 2, 'gw': '10.0.1.254', 'trusted': True, 'server': False, 'hpot': False},
            {'network': '10.0.2.0/24', 'port': 3, 'gw': '10.0.2.254', 'trusted': False, 'server': False, 'hpot': False},
            {'network': '11.0.0.0/24', 'port': 4, 'gw': '11.0.0.254', 'trusted': True, 'server': False, 'hpot': True}
        ],
        'virtual_mac': '00:00:de:ad:be:ef',
}

ASSETS_URL = ['admin']
SERVICE_PORT = 8080