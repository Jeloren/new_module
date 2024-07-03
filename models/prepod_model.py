from odoo import models, fields

class Prepods(models.Model):
    
    _name="new_module.prepods"
    _description="This is my teaсhers"
    
    first_name = fields.Char(string = "Имя")
    last_name = fields.Char(string = "Фамилия")
    middle_name = fields.Char(string = "Отчество")
    
    subject = fields.Char(string = "Дисциплина")
    
    display_name = fields.Char(compute = "Method")
   
    f_group = fields.Many2many(string = 'Группа', comodel_name = "new_module.groups", relation = "new_module_groups_rel", column1 = "prepod_id", column2 = "group_id" )
   
    f_prep_group = fields.Many2one(string = 'Преподаватели группы', comodel_name = "new_module.groups")
    
    grades_given = fields.One2many('new_module.student_grades', 'teacher_id', string='Оценки')
   
    subject_ids = fields.Many2many(comodel_name = 'new_module.subjects', string="Предметы", relation = "new_module_subject_rel")  
    
    def Method(self):
        for record in self:
            record.display_name = f"{record.first_name} {record.middle_name}, {record.subject}"
   
    
    
    