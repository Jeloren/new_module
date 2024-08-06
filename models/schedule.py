from odoo import models, fields, api 

class Schedule(models.Model):
    
    _name="new_module.schedule"
    _description="This is my Schedule"
    
    
    f_group = fields.Many2one(string = 'Группа', comodel_name = "new_module.groups") 
    
    week_day = fields.Selection([
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday')
    ], string='Day of Week', required=True)
    
     
    f_subj = fields.Many2one(comodel_name = "new_module.subject", string = "Предмет")
    
    schedule_lines = fields.One2many(
        comodel_name="new_module.schedule_line", 
        inverse_name="schedule_id", 
        string="Schedule Lines"
    )
    
    @api.onchange('week_day', 'f_group')
    def _onchange_schedule(self):
        if self.f_group and self.week_day:
            schedule_line_obj = self.env['new_module.schedule_line']
            lines = schedule_line_obj.search([
                ('group_id', '=', self.f_group.id),
                ('week_day', '=', self.week_day)
            ])
            self.schedule_lines = lines
        else:
            self.schedule_lines = [(5, 0, 0)] 
    
    
    
    
    
    