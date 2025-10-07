from bll.contacts_bll import ContactsBll

class Contacts:
    def __init__(self, source="json"):
        self.contacts_bll = ContactsBll(source)

    def display_contacts(self):
        for record in self.contacts_bll.search_contacts().get("contacts", []):
            print(f"{record.get("name", "")} \t\t {record.get("contact_no")}")