from odoo import models, fields, api 

class ScheduleLine(models.Model):
    _name = "new_module.schedule_line"
    _description = "Schedule Line"
    
    schedule_id = fields.Many2one(
        comodel_name="new_module.schedule", 
        string="Schedule",
        ondelete='cascade'
    )
    
    group_id = fields.Many2one(
        comodel_name="new_module.groups", 
        string="Группа",
        required=True,
        ondelete='cascade'
    )
    
    week_day = fields.Selection([
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday')
    ], string='Day of Week', required=True)
    
    subject_id = fields.Many2one(
        comodel_name="new_module.subject", 
        string="Предмет",
        required=True
    )
    
    time_start = fields.Float(string="Start Time", required=True)
    time_end = fields.Float(string="End Time", required=True)