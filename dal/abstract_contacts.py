from dal.contacts_dal import ContactsJsonDao
from dal.contacts_db_dal import ContactsDbDao

class ContactsABC:

    def retrieve_contacts(self):
        pass

    def search_contacts(self, keyword):
        pass

class ContactsFactory:

    def create_instance(self, source) -> ContactsABC:
        obj_map = {
            "db": ContactsDbDao(),
            "json": ContactsJsonDao()
        }
        obj = obj_map.get(source, None)

        if obj == None:
            Exception("Invalid Source")
        else:
            return obj()