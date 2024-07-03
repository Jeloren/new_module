from odoo import models, fields

class Groups(models.Model):
    _name = "new_module.groups"
    _description = "This is my groups"
    
    group_faculty = fields.Char(string = "Aбревиатура группы")
    group_num = fields.Char(string = "Номер группы")
    creating_date = fields.Date(string = "Дата создания группы")
    
    display_name = fields.Char(compute = "full_name_of_group")
    students_table = fields.One2many('new_module.students', 'f_group')
    
    # f_group_table = fields.Many2one(string = "Группы преподавателей", comodel_name ="new_module.prepods")
    
    prepods_group = fields.One2many('new_module.prepods', 'f_prep_group')
    
    prepods_table = fields.Many2many(string = 'Преподаватели', comodel_name = "new_module.prepods", relation = "new_module_prepods_rel", column1 = "prepod_id", column2 = "group_id")
    
    grades_table = fields.One2many('new_module.student_grades', 'group_id', string='Оценки')

    
    # r_f_prepod_name = fields.Char(string = "Имя преподавателя", related = "f_prepod.first_name")
    # r_f_prepod_mid_name = fields.Char(string = "Отчество преподавателя", related = "f_prepod.middle_name")
    # r_f_prepod_subject = fields.Char(string = "Дисциплина", related = "f_prepod.subject")
    
    # prepods_table = fields.Many2one('new_module.prepods')
    
    def full_name_of_group(self):
        for record in self:
            record.display_name = f"{record.group_faculty}-{record.group_num}"
    
    
    