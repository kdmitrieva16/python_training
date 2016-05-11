from model.contact import Contact
from model.group import Group
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        # init add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field("firstname", contact.firstname)
        self.change_field("middlename", contact.middlename)
        self.change_field("lastname", contact.lastname)
        self.change_field("nickname", contact.nickname)
        self.change_field("title", contact.title)
        self.change_field("company", contact.company)
        self.change_field("address", contact.address)
        self.change_field("home", contact.home_phone)
        self.change_field("mobile", contact.mobile_phone)
        self.change_field("work", contact.work_phone)
        self.change_field("fax", contact.fax)
        self.change_field("email2", contact.email2)
        self.change_field("email3", contact.email3)
        self.change_field("homepage", contact.homepage)
        if contact.bday is not None:
            if not wd.find_element_by_xpath(contact.bday).is_selected():
                wd.find_element_by_xpath(contact.bday).click()
        if contact.bmonth is not None:
            if not wd.find_element_by_xpath(contact.bmonth).is_selected():
                wd.find_element_by_xpath(contact.bmonth).click()
        self.change_field("byear", contact.byear)
        if contact.aday is not None:
            if not wd.find_element_by_xpath(contact.aday).is_selected():
                wd.find_element_by_xpath(contact.aday).click()
        if contact.amonth is not None:
            if not wd.find_element_by_xpath(contact.amonth).is_selected():
                wd.find_element_by_xpath(contact.amonth).click()
        self.change_field("ayear", contact.ayear)
        self.change_field("address2", contact.address2)
        self.change_field("phone2", contact.phone2)
        self.change_field("notes", contact.notes)


    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_first_contact(self):
        self.edit_contact_by_index(0)
        self.contact_cache = None

    def edit_contact_by_index (self, index, new_contact_data):
        wd = self.app.wd
        #init edit
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit contact editing
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #approve deletion
        wd.switch_to_alert().accept()
        self.app.go_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #approve deletion
        wd.switch_to_alert().accept()
        self.app.go_to_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def count(self):
        wd = self.app.wd
        self.app.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache=None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.go_to_home_page()
            self.contact_cache=[]
            for contact_row in wd.find_elements_by_name("entry"):
                cells = contact_row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_phones=cells[5].text
                all_emails=cells[4].text
                self.contact_cache.append(Contact(id=id,firstname=firstname, lastname=lastname,  address=address,
                                                  all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index (self, index):
        wd = self.app.wd
        self.app.go_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index (self, index):
        wd = self.app.wd
        self.app.go_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_id (self, index):
        wd = self.app.wd
        self.app.go_to_home_page()
        row = wd.find_elements_by_name("entry")[id]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobile= wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")


        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       home_phone=homephone, work_phone=workphone, mobile_phone=mobile,
                       phone2=phone2, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobile=re.search("M: (.*)", text).group(1)
        phone2=re.search("P: (.*)", text).group(1)
        return Contact(home_phone=homephone, work_phone=workphone, mobile_phone=mobile, phone2=phone2)

    def select_group_for_add_contact(self):
        wd = self.app.wd
        self.app.go_to_home_page()
        dd_groups=wd.find_element_by_name("to_group")
        for option in dd_groups.find_elements_by_tag_name('option'):
            if option.text=='gggg hjhfsjdhf':
                option.click()


    def add_contact_into_selected_group(self, id):
        wd = self.app.wd
        self.select_group_for_add_contact()
        self.select_contact_by_id(id)
        wd.find_element_by_name("add").click()
        wd.find_element_by_partial_link_text("group page").click()

    def search_contact_by_group (self):
        wd = self.app.wd
        self.app.go_to_home_page()
        dd_groups=wd.find_element_by_xpath('//select[@name="group"]')
        for option in dd_groups.find_elements_by_tag_name('option'):
            if option.text=='gggg hjhfsjdhf':
                option.click()



    def delete_contact_from_selected_group(self, id):
        wd = self.app.wd
        self.search_contact_by_group()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath('/html/body/div/div[4]/form[2]/div[2]/input').click()
        wd.switch_to_alert().accept()



    group_cache=None

    def get_group_list_from_dd(self):
        wd = self.app.wd
        self.app.go_to_home_page()
        dd_groups=wd.find_element_by_name("to_group")
        groups=[]
        for element in dd_groups.find_elements_by_tag_name('option'):
            text = element.get_attribute("label")
            groups.append(Group(name=text))
        return groups


