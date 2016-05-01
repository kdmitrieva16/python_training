# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app, db, json_contacts):
    contact=json_contacts
    old_contacts = db.get_contact_list()
    app.contact.add_new(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts, key=Contact.id_or_max)





