from odoo import models, fields

class Journal(models.Model):
    
    _name="new_module.journal"
    _description="This is my journal"
    
    f_student = fields.Many2one(comodel_name = "new_module.students", string = "Студент")
     
    f_subj = fields.Many2one(comodel_name = "new_module.subject", string = "Предмет")
    
    f_grade = fields.Many2one(comodel_name = "new_module.student_grades", string = "Оценка")
    
    display_name = fields.Char(string = "")
    
    
    
    
    