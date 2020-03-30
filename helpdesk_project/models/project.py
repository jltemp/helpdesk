from odoo import api, fields, models


class ProjectTask(models.Model):

    _inherit = 'project.task'

    ticket_ids = fields.One2many(comodel_name='helpdesk.ticket', inverse_name='task_id', string='Tareas')
    
    tickets_count = fields.Integer(compute='contar_tickets',string='Tcks.')
    

    @api.depends('ticket_ids')
    def contar_tickets(self):
        self.tickets_count  = len(self.ticket_ids)

    def action_view_tickets_miVersion(self):
        action = self.env.ref("helpdesk_project.project_alta_ticket_action").read()[0]
        # action['context']={
        #     'default_task_id' : self.id,
        #     'default_project_id' : self.project_id and self.project_id.id
        # }
        action['res_id'] = 0
        return action

    def action_view_tickets(self):
        action = self.env.ref("helpdesk_project.task_action_ticket_new").read()[0]
        action['context']={
            'default_task_id' : self.id,
            'default_project_id' : self.project_id and self.project_id.id
        }
        return action

    # def action_view_tickets(self):
    #     action = self.env.ref('sale.action_quotations_with_onboarding').read()[0]
    #     action['context'] = {
    #         'search_default_draft': 1,
    #         'search_default_partner_id': self.partner_id.id,
    #         'default_partner_id': self.partner_id.id,
    #         'default_opportunity_id': self.id
    #     }
    #     action['domain'] = [('opportunity_id', '=', self.id), ('state', 'in', ['draft', 'sent'])]
    #     quotations = self.mapped('order_ids').filtered(lambda l: l.state in ('draft', 'sent'))
    #     if len(quotations) == 1:
    #         action['views'] = [(self.env.ref('sale.view_order_form').id, 'form')]
    #         action['res_id'] = quotations.id
    #     return action
    