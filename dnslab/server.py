import socket
from typing import Dict
from os.path import abspath, dirname, join

from onl.device import UDPDevice
from onl.sim import Environment

from dns_packet import DNSPacket


class DNSServer(UDPDevice):
    def __init__(self, env: Environment, debug: bool = False):
        super().__init__()
        self.env = env
        # map url to ip address
        self.url_ip: Dict[str, str] = dict()
        with open(join(dirname(abspath(__file__)), "ipconf.txt"), "r", encoding="utf-8") as f:
            for line in f:
                ip, name = line.split(" ")
                self.url_ip[name.strip("\n")] = ip
        # public DNS server address
        self.name_server = ("223.5.5.5", 53)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("", 1088))
        self.server_socket.setblocking(True)
        self.trans = {}
        self.debug = debug

    def recv_callback(self, data: bytes):
        """
        TODO: 处理DNS请求，data参数为DNS请求数据包对应的字节流
        1. 解析data得到构建应答数据包所需要的字段
        2. 根据请求中的domain name进行相应的处理:
            2.1 如果domain name在self.url_ip中，构建对应的应答数据包，发送给客户端
            2.2 如果domain name不再self.url_ip中，将DNS请求发送给public DNS server
        """
        pass
