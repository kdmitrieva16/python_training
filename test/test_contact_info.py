import re


from random import  randrange


def test_contact_info_on_home_page(app):
    index=randrange(len(app.contact.get_contact_list()))
    contact_from_home_page=app.contact.get_contact_list()[index]
    contact_from_edit_page=app.contact.get_contact_info_from_edit_page(index)
    assert clear(contact_from_home_page.lastname)==clear(contact_from_edit_page.lastname)
    assert clear(contact_from_home_page.firstname)==clear(contact_from_edit_page.firstname)
    assert contact_from_home_page.address.strip()==contact_from_edit_page.address.strip()
    assert contact_from_home_page.all_phones_from_home_page==merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page==merge_emails_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            (map(lambda x:clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone2])))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            (map(lambda x:clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.email, contact.email2, contact.email3])))))