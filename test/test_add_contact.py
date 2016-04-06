# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact =Contact(firstname="Tony", middlename="nnnn", lastname="Wendice", nickname="mmm", title="mhfgj", company="gfhfghfgs", address="dfgdg dg dgd.d hdhfh",
                                     home_phone="111111111", mobile_phone="22222222222", work_phone="44545456575", fax="hhfjjjfjfjfjfj", email2="fjfjghjhjjf@ddfdfdf.fg",
                                     email3="gdfgfdfhfhfgh", homepage="ffsfsdgddfgdfgdfgdgghj", address2="wewwrweetehfghgf", phone2="hghfhfhfhhfjuiuidf",
                                     notes="sdfdgdfhdfhdfhfhjghjhgh", bday= "//div[@id='content']/form/select[1]//option[18]", bmonth="//div[@id='content']/form/select[2]//option[12]", byear= "1971",
                                     aday="//div[@id='content']/form/select[3]//option[11]",
                                     amonth="//div[@id='content']/form/select[4]//option[3]", ayear="1999")
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts, key=Contact.id_or_max)





