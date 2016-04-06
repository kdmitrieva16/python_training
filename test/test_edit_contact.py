# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="new", lastname="contact")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0]=contact
    assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_first_contact(app):
#    app.contact.edit_first_contact(Contact(firstname="edited", middlename="edited", lastname="Wendice", nickname="edited", title="edited", company="edited", address="edited dg dgd.d hdhfh",
 #                                    home_phone="333333", mobile_phone="44444444444", work_phone="44545456678", fax="hhfjjjfjfjfjfj", email2="fjfjghjhjjf@ddfdfdf.fg",
  #                                   email3="gdfgfdfhfhfgh", homepage="ffsfsdgddfgdfgdfgdgghj", address2="wewwrweetehfghgf", phone2="hghfhfhfhhfjuiuidf",
   #                                  notes="sdfdgdfhdfhdfhfhjghjhgh", bday= "//div[@id='content']/form/select[1]//option[18]", bmonth="//div[@id='content']/form/select[2]//option[12]", byear= "1971",
    #                                 aday="//div[@id='content']/form/select[3]//option[11]",
     #                                amonth="//div[@id='content']/form/select[4]//option[3]", ayear="1999"))
