from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    name = fields.Char(string='Name')

    #Uno o varios tickets pueden estar asignados a un proyecto
    project_id = fields.Many2one(
        comodel_name='project.project', 
        string='Proyecto')

    #Uno o varios tickets pueden estar asignados a una tarea'
    task_id = fields.Many2one(
        comodel_name='project.task', 
        string='Tarea')
    
    def action_new_view(self):
        # action = self.env.ref("helpdesk_project.project_alta_ticket_action").read()[0]
        action = self.env.ref("helpdesk_project.task_action_ticket_new").read()[0]
        action['context']={
            'default_task_id' : self.id,
            'default_project_id' : self.project_id and self.project_id.id
        }
        return action
    
    # Si busco la tarea sin indicar el proyecto completar el proyecto de esa tarea
    # (onchange en tarea que complete el projecto)
    # si busco primero el proyecto solo permitir seleccionar tareas de ese proyecto
    # (onchange a project que devuelva un domain)

    # Al buscar una tarea sin poner el proyecto que se obtenga el proyecto 
    @api.onchange('task_id')
    def _onchange_task_id(self):
        if self.task_id and self.task_id.project_id:
            self.project_id = self.task_id.project_id
        else:
            self.project_id = False

    
    # Al buscar un proyecto filtrar (domain) las posibles tareas de ese proyecto
    @api.onchange('project_id')
    def _onchange_project_id(self):
        if self.project_id:
            domain = {'task_id':[('project_id',"=",self.project_id.id)]}
            #domain = [(project_id,"=",self.project_id.id)]
            #domain = {'task_id':[]}
        else:
            domain = {}
        return {'domain' : domain}


