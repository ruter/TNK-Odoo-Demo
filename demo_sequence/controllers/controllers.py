# -*- coding: utf-8 -*-
from odoo import http

# class DemoSequence(http.Controller):
#     @http.route('/demo_sequence/demo_sequence/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo_sequence/demo_sequence/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_sequence.listing', {
#             'root': '/demo_sequence/demo_sequence',
#             'objects': http.request.env['demo_sequence.demo_sequence'].search([]),
#         })

#     @http.route('/demo_sequence/demo_sequence/objects/<model("demo_sequence.demo_sequence"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_sequence.object', {
#             'object': obj
#         })