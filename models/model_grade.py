from odoo import _, fields, models


class Grades(models.Model):
    _name="new_module.student_grades"
    _description="This is my grades"
    
    student_id = fields.Many2one('new_module.students', string='Студент', required=True)
    group_id = fields.Many2one('new_module.groups', string='Группа', required=True)
    subject_id = fields.Many2one('new_module.subjects', string='Предмет', required=True)
    grade = fields.Integer(string='Оценка', required=True)
    teacher_id = fields.Many2one('new_module.prepods', string='Преподаватель', required=True)
    date = fields.Date(string='Дата', required=True)