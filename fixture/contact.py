from model.contact import Contact

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

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        #init edit
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        # submit contact editing
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #approve deletion
        wd.switch_to_alert().accept()
        self.app.go_to_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

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
                contact_rows=[]
                for contact_cell in contact_row.find_elements_by_tag_name("td"):
                    contact_rows.append(contact_cell)
                id = contact_row.find_element_by_name("selected[]").get_attribute("value")
                lastname = contact_rows[1].text
                firstname = contact_rows[2].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)

    def get_contact_list2(self):
        wd = self.app.wd
        self.app.go_to_home_page()
        contacts=[]
        for contact_row in wd.find_elements_by_name("entry"):
            id = contact_row.find_element_by_name("selected[]").get_attribute("value")
            lastname = contact_row.find_element_by_xpath('./td[2]').text
            firstname = contact_row.find_element_by_xpath('./td[3]').text
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts











