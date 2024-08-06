from odoo import models, fields

class Groups(models.Model):
    _name = "new_module.groups"
    _description = "This is my groups"
    
    group_faculty = fields.Char(string = "Aбревиатура группы")
    group_num = fields.Char(string = "Номер группы")
    creating_date = fields.Date(string = "Дата создания группы")
    
    display_name = fields.Char(compute = "full_name_of_group")
    students_table = fields.One2many('new_module.students', 'f_group')
    

    
    prepods_group = fields.One2many('new_module.prepods', 'f_prep_group')
    
    prepods_table = fields.Many2many(string = 'Преподаватели', comodel_name = "new_module.prepods", relation = "new_module_prepods_rel", column1 = "prepod_id", column2 = "group_id")
    
   
    def full_name_of_group(self):
        for record in self:
            record.display_name = f"{record.group_faculty}-{record.group_num}"
    
    
    