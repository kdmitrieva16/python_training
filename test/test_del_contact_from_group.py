from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

orm=ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_del_contact_from_group(app, db):
    list_group_add_to=app.contact.get_group_list_from_dd()
    group=random.choice(list_group_add_to)
    old_contacts_in_group=orm.get_contacts_in_group_by_name(Group(name=group.name))
    if len(old_contacts_in_group) == 0:
        contacts = db.get_contact_list()
        contact0=random.choice(contacts)
        app.contact.add_contact_into_selected_group(contact0.id)
    #old_contacts_in_group=orm.get_contacts_in_group(Group(id="9"))
    app.contact.search_contact_by_group(group.name)
    contact=random.choice(old_contacts_in_group)
    app.contact.delete_contact_from_selected_group(contact.id)
    new_contacts_in_group = orm.get_contacts_in_group_by_name(Group(name=group.name))
    old_contacts_in_group.remove(contact)
    assert old_contacts_in_group == new_contacts_in_group
