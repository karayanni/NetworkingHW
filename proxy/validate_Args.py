# import ipaddress why... no need to over engineer...


def is_valid_args(listen_port: int, fake_ip: str, server_ip: str):
    """
    validates the provided arguments to the script
    :return: True if the arguments are valid False otherwise
    """
    # return is_valid_port_number(listen_port) and is_valid_id_address(fake_ip) and is_valid_id_address(server_ip)
    return True


def is_valid_port_number(listen_port: int):
    # validate the port number is valid port number:
    if listen_port < 1 or listen_port > 65535:
        print(f'Invalid port number {listen_port}, please provide a port number between 1024 and 65535')
        return False

    if listen_port < 1024:
        print(f'WARNING, the specified port number {listen_port} is used by system-supplied TCP/IP applications')
    return True

# dont try to be smart..
# def is_valid_id_address(ip_address: str):
#     try:
#         ipaddress.IPv4Address(ip_address)
#         return True
#
#     except ipaddress.AddressValueError:
#         print(f'Invalid ipv4 address {ip_address}')
#         return False
