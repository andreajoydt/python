from dal.db_dal import DbDaoABC
from dal.abstract_contacts import ContactsABC

class ContactsDbDao(DbDaoABC, ContactsABC): 

    def retrieve_contacts(self):
        sql = "SELECT name, contact_no FROM contacts"
        
        result = {
            "contacts": []
        }
        
        for row in self.execute_select(sql):
            result.get("contacts").append({
                "name": row[0],
                "contact_no": row[1]
            })

        return result

    def search_contacts(self, keyword):
        raise Exception("Not implemented")