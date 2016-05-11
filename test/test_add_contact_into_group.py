from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

orm=ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_into_group(app, db):
    old_contacts_in_group=orm.get_contacts_in_group(Group(id="9"))
    contacts = db.get_contact_list()
    contact=random.choice(contacts)
    app.contact.add_contact_into_selected_group(contact.id)
    new_contacts_in_group=orm.get_contacts_in_group(Group(id="9"))
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max)==sorted(new_contacts_in_group, key=Contact.id_or_max)

