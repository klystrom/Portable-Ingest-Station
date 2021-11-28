import socket

def check_network_connection(): 
    try:
        addr1 = socket.gethostbyname('google.com')
    except:
        addr1 = "NOPE."

    try:
        addr2 = socket.gethostbyname('hawktalonnextcloud.ddns.net')
    except:
        addr2 = "NOPE."

    if (addr1 == "NOPE.") or (addr2 == "NOPE."):
        return False
    else:
        print("Google is at " + addr1)
        print("NextCloud is at " + addr2)
        return True


if __name__== "__main__":
    check_network_connection()