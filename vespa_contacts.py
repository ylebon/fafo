"""Vespa contacts.

Usage:
  vespa_contacts.py list
  vespa_contacts.py (-h | --help)

Examples:
  vespa_contacts.py list

Options:
  -h, --help

"""
from docopt import docopt


def list_contacts():
    """List contacts"""
    contacts = ["gaia", "akki", "eva", "thomas", "helene", "andrea", "..."]
    for contact in contacts:
        print(f"- {contact}")


if __name__ == "__main__":
    arguments = docopt(__doc__)
    if arguments.get('list'):
        list_contacts()
