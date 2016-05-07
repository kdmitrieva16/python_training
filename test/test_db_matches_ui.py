from model.group import Group
from model.contact import Contact
import re
from timeit import timeit

def test_group_list(app, db):
    ui_list=app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list=map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max)==sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_list=app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(),lastname=contact.lastname.strip(), address=contact.address.strip(), all_phones=contact.all_phones,
                       all_emails=contact.all_emails)
    db_list=map(clean, db.get_contact_list_like_on_home_page())
    assert sorted(ui_list, key=Contact.id_or_max)==sorted(db_list, key=Contact.id_or_max)


def test_contact_list1(app, db):
    ui_list=app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(),lastname=contact.lastname.strip(), address=contact.address.strip(), all_phones=merge_phones_like_on_home_page(contact),
                       all_emails=merge_emails_like_on_home_page(contact))
    db_list=map(clean, db.get_contact_list1())
    assert sorted(ui_list, key=Contact.id_or_max)==sorted(db_list, key=Contact.id_or_max)


def clear_phones(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            (map(lambda x:clear_phones(x),
                                 filter(lambda x: x is not None,
                                        [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone2])))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            (map(lambda x:clear_phones(x),
                                 filter(lambda x: x is not None,
                                        [contact.email, contact.email2, contact.email3])))))