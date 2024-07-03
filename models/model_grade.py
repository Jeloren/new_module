from odoo import _, fields, models, api

class Grades(models.Model):
    _name = "new_module.student_grades"
    _description = "This is my grades"
    
    grade = fields.Char(string="Оценка")
    display_name = fields.Char(compute="_compute_display_name", store=True)
    date = fields.Date(string='Дата')
    
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.grade
