"""Vespa contacts.

Usage:
  vespa_contacts.py list
  vespa_contacts.py add <name>
  vespa_contacts.py find <name>
  vespa_contacts.py (-h | --help)

Examples:
  vespa_contacts.py list

Options:
  -h, --help

"""
from docopt import docopt

CONTACTS = {
  "gaia": {"loc": "the netherlands"},
  "akki": {"loc": "mauritius"},
  "eva": {"loc": "ireland"},
  "thomas": {"loc": "france"},
  "helene": {"loc": "france"},
  "andrea": {"loc": "the hague"},
  "sebastien": {"loc": "reunion"}
}


def add_contact(name):
    """Add contact to the vespa"""
    CONTACTS[name] = dict()
    list_contacts()
    
def find_contact(name):
    """Return contact location"""
    contact_info = CONTACTS.get(name, {})
    if not contact_info:
      return "contact not found"
    else:
      contact_loc = contact_info.get('loc', 'location not provided')
      return contact_loc

def list_contacts():
    """List contacts"""
    for name in CONTACTS.keys():
        print(f"- {name}")


if __name__ == "__main__":
    arguments = docopt(__doc__)
    if arguments.get('list'):
        list_contacts()
    elif arguments.get('add'):
        add_contact(arguments['<name>'])
    elif arguments.get('find'):
        print(find_contact(arguments['<name>']))
        
