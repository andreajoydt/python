from bll.contacts_bll import retrieve_contacts

def display_contacts():
    for record in retrieve_contacts("db").get("contacts", []):
        print(f"{record.get("name", "")} \t\t {record.get("contact_no")}")
