from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

orm=ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_into_group(app, db):
    #old_contacts_in_group=orm.get_contacts_in_group(Group(id="9"))
    contacts = db.get_contact_list()
    contact=random.choice(contacts)
    list_group_add_to=app.contact.get_group_list_from_dd()
    group=random.choice(list_group_add_to)
    old_contacts_in_group=orm.get_contacts_in_group_by_name(Group(name=group.name))
    app.contact.select_group_for_add_contact(group.name)
    app.contact.add_contact_into_selected_group(contact.id)
    new_contacts_in_group=orm.get_contacts_in_group_by_name(Group(name=group.name))
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max)==sorted(new_contacts_in_group, key=Contact.id_or_max)

