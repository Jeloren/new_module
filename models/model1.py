# -*- coding:utf-8 -*-

from odoo import _, fields, models


class Students(models.Model):
    _name="new_module.students"
    _description="This is my students"
    
    first_name = fields.Char(string = "Имя")
    last_name = fields.Char(string = "Фамилия")
    middle_name = fields.Char(string = "Отчество")
    age = fields.Integer(string = "Возраст", default = 18)
    birth_day = fields.Date(string = "Дата рождения")
   
    f_group = fields.Many2one(string = 'Группа студента', comodel_name = "new_module.groups")
    
    # grades_table = fields.One2many('new_module.student_grades', 'student_id', string='Оценки')
    
    display_name = fields.Char(compute = "Method")
   
    def Method(self):
        for record in self:
            record.display_name = f"{record.first_name} {record.last_name}"
            

