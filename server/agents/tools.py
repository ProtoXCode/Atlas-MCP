import socket

import requests
import netifaces
from fastapi import APIRouter

router = APIRouter()


def get_router_vendor(mac_prefix: str) -> str:
    try:
        url = f'https://api.macvendors.com/{mac_prefix}'
        return requests.get(url, timeout=2).text
    except Exception as e:
        return f'Unknown - {e}'


@router.get('/network_info', summary='Get network info', tags=['MCP Tools'])
async def get_network_info() -> dict:
    """
    Retrieves local network information including IP address,
    default gateway, router MAC address and vendor (if possible).
    """
    info = {}

    hostname = socket.gethostname()
    info['local_ip'] = socket.gethostbyname(hostname)
    gateway = netifaces.gateways()
    default = gateway.get('default', {})

    if netifaces.AF_INET in default:
        gw_ip, iface = default[netifaces.AF_INET]
        info['gateway_ip'] = gw_ip
        info['interface'] = iface

        try:
            from getmac import get_mac_address
            mac = get_mac_address(ip=gw_ip)
            info['router_mac'] = mac
            if mac:
                mac_prefix = ':'.join(mac.split(':')[:6]).upper()
                info['router_vendor'] = get_router_vendor(mac_prefix)
        except Exception as e:
            print(f'Failed to get mac address: {e}')

    return info
