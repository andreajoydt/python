from bll.contacts_bll import ContactBll
from fastapi import APIRouter
from domain.contact import Contact
from util.logger import Logger, enable_logging

router = APIRouter(tags=["Contacts API"])
contact_bll = ContactBll("json")
logger = Logger().get_logger()

@router.get("/contacts")
@enable_logging
def display_contacts()->list[Contact]:
    return contact_bll.retrieve_contacts().get("contacts", [])

@router.get("/contacts/search")
def search_contacts(keyword:str)->list[Contact]:
    logger.info(f"Begin search contacts for [{keyword}]")
    return contact_bll.search_contacts(keyword).get("contacts", [])

# @router.get("/contacts/search/{keyword}")
# def search_contacts(keyword:str)->list[Contact]:
#     return contact_bll.search_contacts(keyword).get("contacts", [])
