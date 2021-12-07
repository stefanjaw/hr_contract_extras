# -*- coding: utf-8 -*-
# from odoo import http


# class HrContractExtras(http.Controller):
#     @http.route('/hr_contract_extras/hr_contract_extras/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_contract_extras/hr_contract_extras/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_contract_extras.listing', {
#             'root': '/hr_contract_extras/hr_contract_extras',
#             'objects': http.request.env['hr_contract_extras.hr_contract_extras'].search([]),
#         })

#     @http.route('/hr_contract_extras/hr_contract_extras/objects/<model("hr_contract_extras.hr_contract_extras"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_contract_extras.object', {
#             'object': obj
#         })
