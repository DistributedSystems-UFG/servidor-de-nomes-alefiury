from collections import defaultdict

from rpyc import Service
from rpyc.utils.server import ThreadedServer

from constCS import *


class NameServer(Service):
    lookup_table = defaultdict(list)

    def exposed_register(self, name: str, ip_address: str, port: int) -> None:
        if name not in dict.keys(self.lookup_table):
            self.lookup_table[name].append((ip_address, port))
        else:
            print(f"Name: {name} already exists... ")

        print(self.lookup_table)

    def exposed_lookup(self, name: str) -> tuple:
        if name in self.lookup_table.keys():
            return self.lookup_table[name][0]
        else:
            print(f"Name: {name} does not exist... ")


def main() -> None:
    server = ThreadedServer(
        NameServer,
        port=NAME_SERVER_PORT
    )
    server.start()


if __name__ == "__main__":
    main()