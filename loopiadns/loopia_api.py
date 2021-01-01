import logging
from xmlrpc import client

from loopiadns.rpc.exceptions import LoopiaAPIException
from loopiadns.rpc.record import Record


class LoopiaAPI:
    def __init__(self, username: str, password: str, domain: str = None):
        self.__loopia_api = "https://api.loopia.se/RPCSERV"
        self.__username = username
        self.__password = password
        self.__domain = domain
        self.__client = client.ServerProxy(self.__loopia_api, encoding="utf-8")
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

    def get_domains(self):
        return self.__client.getDomains(self.__username, self.__password)

    def add_record(self, name: str, record: Record):
        if name not in self.get_subdomains():
            self.add_subdomain(name)

        logging.info(f"Adding zone record: {name}.{self.__domain} {record.type} {record.data}")
        status = self.__client.addZoneRecord(self.__username, self.__password, self.__domain,
                                             name, record.as_dict())
        if status != "OK":
            logging.error(f"{status}")
            raise LoopiaAPIException(status)
        logging.info("OK")

    def add_subdomain(self, name: str):
        logging.info(f"Creating subdomain {name}.{self.__domain}")
        status = self.__client.addSubdomain(self.__username, self.__password, self.__domain, name)
        if status != "OK":
            logging.error(f"{status}")
            raise LoopiaAPIException(status)

        logging.info("OK")

    def get_subdomains(self):
        return self.__client.getSubdomains(self.__username, self.__password, self.__domain)

    def get_records(self, name: str):
        return self.__client.getZoneRecords(self.__username, self.__password, self.__domain, name)

    def remove_subdomain(self, name: str):
        logging.info(f"Removing subdomain {name}.{self.__domain}")
        status = self.__client.removeSubdomain(self.__username, self.__password, self.__domain,
                                               name)
        if status != "OK":
            logging.error(f"{status}")
            raise LoopiaAPIException(status)
        logging.info("OK")
