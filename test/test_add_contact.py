# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols=string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="")]+[
    Contact(firstname=random_string("firstname",20), middlename=random_string("middlename", 20),
            lastname=random_string("lastname", 20), home_phone=random_string("home",10), work_phone=random_string("work",10),
            mobile_phone=random_string("mobile",10))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x)for x in testdata])

def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts, key=Contact.id_or_max)





