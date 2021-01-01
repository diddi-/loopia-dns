import configparser
import os

import click
from pathlib import Path

from loopiadns.loopia_api import LoopiaAPI
from loopiadns.rpc.record import Record
from loopiadns.rpc.record_type import RecordType


def get_api(domain=None):
    config = configparser.ConfigParser()
    config.read(os.path.join(Path.home(), ".loopia-credentials"))
    username = config.get("loopia", "username")
    password = config.get("loopia", "password")
    return LoopiaAPI(username, password, domain)


@click.group()
def main():
    """ Manage DNS entries with Loopia API. """


@main.group()
def get():
    """ Get DNS data """
    pass


@get.command("domains")
def get_domains():
    api = get_api()
    for d in api.get_domains():
        click.echo(d["domain"])


@get.command("subdomains")
@click.argument("domain")
def get_subdomains(domain):
    api = get_api(domain)
    result = {}
    for s in api.get_subdomains():
        result[s] = []
        for r in api.get_records(s):
            result[s].append(f"\t{r['type']} {r['rdata']} (ttl: {r['ttl']})")

    for k, v in result.items():
        click.echo(k)
        for r in v:
            click.echo(r)


@main.group()
def create():
    """ Create new DNS entries """
    pass


@create.command("subdomain")
@click.argument("domain")
@click.argument("subdomain")
@click.option("-t", "--type", "record_type", help="Type of record (A, CNAME, etc.)")
@click.option("-v", "--value", "value", help="Value of the record")
@click.option("--ttl", "ttl", default=60, help="TTL of the record")
def create_subdomain(domain, subdomain, record_type, value, ttl):
    api = get_api(domain)
    api.add_subdomain(subdomain)
    if record_type and value:
        record = Record(RecordType[record_type], value, ttl=ttl)
        api.add_record(subdomain, record)


@main.group()
def delete():
    """ Delete DNS entries """
    pass


@delete.command("subdomain")
@click.argument("domain")
@click.argument("subdomain")
def delete_subdomain(domain, subname):
    api = get_api(domain)
    api.remove_subdomain(subname)
