# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.http import request


class Notify(models.Model):
    _name = 'new_module.notify'
    _description = 'notify'

    enable_welcome_message = fields.Boolean(string='Enable Welcome Message', default=True)

    @api.model
    def show_welcome_message(self):
        for record in self:
            if not record.enable_welcome_message:
                continue
            user = self.env.user
            action = {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Добро пожаловать!',
                    'message': f'{user.name}, добро пожаловать в систему!',
                    'sticky': False,
                    'next': {'type': 'ir.actions.act_window_close'},
                }
            }
            return action

        
    
    
