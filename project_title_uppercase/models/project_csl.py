# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProjectCsl(models.Model):
    _inherit = 'project.project'

    @api.onchange('name')
    def _onchange_name_uppercase(self):
        """Convert project title to uppercase on change"""
        if self.name:
            self.name = self.name.upper()

    @api.model_create_multi
    def create(self, vals_list):
        """Convert project title to uppercase on create"""
        for vals in vals_list:
            if vals.get('name'):
                vals['name'] = vals['name'].upper()
        return super(ProjectCsl, self).create(vals_list)

    def write(self, vals):
        """Convert project title to uppercase on write"""
        if vals.get('name'):
            vals['name'] = vals['name'].upper()
        return super(ProjectCsl, self).write(vals)
