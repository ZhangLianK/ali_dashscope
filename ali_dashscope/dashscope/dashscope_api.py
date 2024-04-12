import dashscope
import frappe
import frappe.utils
from frappe.utils.password import get_decrypted_password

@frappe.whitelist(allow_guest=True)
def chat():
    return "Chatting with Dashscope"

secret_info = frappe.get_doc('Ali Security', 'dashscope')
#the key is stored in a single doctype Dashscope Security
dashscope.api_key = get_decrypted_password('Ali Security', secret_info.name, "api_key")
print(dashscope.api_key)
