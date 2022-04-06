from rpyc import connect, Service
from rpyc.utils.server import ThreadedServer
from socket import gethostname, gethostbyname

from constCS import *
from utils import levenshtein


class StringOps(Service):
    def exposed_concat(self, first_string: str, second_string: str) -> str:
        """Concatenate two strings"""
        return first_string+second_string


    def exposed_levenshtein(self, first_string: str, second_string: str) -> float:
        """Calculates the levenshtein distance between two strings"""
        return levenshtein(first_string, second_string)


    def exposed_equal(self, first_string: str, second_string: str) -> bool:
        """Check if two strings are equal or not"""
        return True if first_string==second_string else False


def main() -> None:
    conn = connect(NAME_SERVER_HOST, NAME_SERVER_PORT)

    host_name = gethostname()
    ip_address = gethostbyname(host_name)

    conn.root.register(
        MAIN_SERVER_NAME,
        ip_address,
        MAIN_SERVER_PORT
    )

    server = ThreadedServer(
        StringOps,
        port=MAIN_SERVER_PORT
    )

    server.start()

if __name__ == "__main__":
    main()