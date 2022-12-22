"""Vespa contacts.

Usage:
  vespa_contacts.py list
  vespa_contacts.py add <name>
  vespa_contacts.py (-h | --help)

Examples:
  vespa_contacts.py list

Options:
  -h, --help

"""
from docopt import docopt

CONTACTS = ["gaia", "akki", "eva", "thomas", "helene", "andrea"]


def add_contact(name):
    """Add contact to the vespa"""
    CONTACTS.append(name)
    list_contacts()


def list_contacts():
    """List contacts"""
    for contact in CONTACTS:
        print(f"- {contact}")


if __name__ == "__main__":
    arguments = docopt(__doc__)
    if arguments.get('list'):
        list_contacts()
    elif arguments.get('add'):
        add_contact(arguments['<name>'])
