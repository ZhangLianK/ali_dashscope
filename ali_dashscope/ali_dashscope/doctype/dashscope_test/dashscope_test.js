// Copyright (c) 2024, Alvin and contributors
// For license information, please see license.txt

frappe.ui.form.on('Dashscope Test', {
	// refresh: function(frm) {

	// }
	call: function(frm) {
		frappe.call({
			method: "ali_dashscope.ali_dashscope.dashscope.dashscope.chat",
			callback: function(r) {
				frm.set_value("result", r.message.text);
			}
		});
	}
});
