import frappe
from frappe.utils.password import get_decrypted_password
from http import HTTPStatus
import dashscope
from dashscope import Generation
import json

@frappe.whitelist()
def chat():
    pass

@frappe.whitelist()
def recoginize_vehicle(text):
#    prompt = '''你是json技术专家，请把下面的物流运输聊天记录中的车辆、司机及押运员信息文本整理成规范的json格式。json的格式如下
#{'vehicle': '车牌号','guahao': '挂车号','qty': '吨数','driver': '司机姓名','cell_number': '司机手机号','pid': '司机身份证号','yayun': '押运员姓名','yayun_pid': '押运员身份证号','yayun_cell_number': '押运员手机号',}
#不允许出现除了以上字段之外的信息，如果没有对应字段信息，这使用空字符串。qty字段必须是数字。只返回正确的json数据，不要其他文本。'''
#    prompt += text
#    print(prompt)
#    secret_info = frappe.get_doc('Ali Security', 'dashscope')
#    #the key is stored in a single doctype Dashscope Security
#    dashscope.api_key = get_decrypted_password('Ali Security', secret_info.name, "api_key")
#    response = dashscope.Generation.call(
#        model='qwen-max',
#        prompt="你是json技术专家，请把下面的物流运输聊天记录中的车辆、司机及押运员信息文本整理成规范的json格式。json的格式如下\n{\"vehicle\": \"车牌号\",\"guahao\": \"挂车号\",\"qty\": \"吨数\",\"driver\": \"司机姓名\",\"cell_number\": \"司机手机号\",\"pid\": \"司机身份证号\",\"yayun\": \"押运员姓名\",\"yayun_pid\": \"押运员身份证号\",\"yayun_cell_number\": \"押运员手机号\",}\n不允许出现除了以上字段之外的信息，如果没有对应字段信息，这使用空字符串。只返回正确的json数据，不要其他文本。\n车号：辽H23717\n挂车：辽HL736挂\n装32吨\n司机 肖兵\n电话18741299456\n身份证210321197012165013",
#        seed=1234,
#        top_p=0.59,
#        result_format='message',
#        enable_search=False,
#        max_tokens=1500,
#        temperature=0.0,
#        repetition_penalty=1.0
#        )
#    if response.status_code == HTTPStatus.OK:
#        #output need utf-8 decoding
#        print(response.output.choices[0].message.content)
#        #using the json.loads method to convert the string to a dictionary and return
#        # Initial JSON string from the API
#        # Parse the initial JSON string
#        embedded_json_string = response.output.choices[0].message.content
#        cleaned_json_string = embedded_json_string.replace('```json', '').replace('```', '').strip()
#
#        # Parse the cleaned JSON string into a dictionary
#        embedded_json = json.loads(cleaned_json_string)
#
#        # Output the result
#        print(embedded_json)
#        return embedded_json
#    else:
#        return response.message
    return {'vehicle': '辽H23717','guahao': '辽HL736挂','qty': '32','driver': '肖兵','cell_number': '18741299456','pid': '210321197012165013','yayun': '','yayun_pid': '','yayun_cell_number': '',}


