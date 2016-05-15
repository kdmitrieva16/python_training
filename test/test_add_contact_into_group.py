from model.contact import Contact
from model.group import Group
import random


def test_add_contact_into_group(app, db, orm):
    contacts = db.get_contact_list()
    contact=random.choice(contacts)
    list_group_add_to=db.get_group_list()
    group=random.choice(list_group_add_to)
    old_contacts_in_group=orm.get_contacts_in_group_by_name(Group(name=group.name))
    app.contact.select_group_for_add_contact(group.name)
    app.contact.add_contact_into_selected_group(contact.id)
    new_contacts_in_group=orm.get_contacts_in_group_by_name(Group(name=group.name))
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max)==sorted(new_contacts_in_group, key=Contact.id_or_max)

