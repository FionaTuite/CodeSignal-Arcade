from ipaddress import ip_address as ip
def isIPv4Address(inputString):
    try: 
        i = ip(inputString)
    except:
        return False
    return True
