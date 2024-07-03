from odoo import models, fields

class Subject(models.Model):
    
    _name="new_module.subject"
    _description="This is my subjects"
    
    name = fields.Char(string='Предмет', required=True)
    teacher_ids = fields.Many2many(comodel_name='new_module.prepods', string='Преподаватель', relation = "new_module_tachers_rel")
    
   
   
    
    
    