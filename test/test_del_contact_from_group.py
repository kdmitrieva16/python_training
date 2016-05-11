from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

orm=ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_del_contact_from_group(app, db):
    if len(orm.get_contacts_in_group(Group(id="9"))) == 0:
        contacts = db.get_contact_list()
        contact0=random.choice(contacts)
        app.contact.add_contact_into_selected_group(contact0.id)
    old_contacts_in_group=orm.get_contacts_in_group(Group(id="9"))
    contact=random.choice(old_contacts_in_group)
    app.contact.delete_contact_from_selected_group(contact.id)
    new_contacts_in_group = orm.get_contacts_in_group(Group(id="9"))
    old_contacts_in_group.remove(contact)
    assert old_contacts_in_group == new_contacts_in_group
