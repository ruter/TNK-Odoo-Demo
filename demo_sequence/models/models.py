# -*- coding: utf-8 -*-

import fcntl
import logging
import datetime

from odoo import models, fields, api
from odoo.modules.module import get_module_resource


_logger = logging.getLogger(__name__)

def _file_lock(flag=fcntl.LOCK_EX):
    FILE_PATH = get_module_resource('demo_sequence', 'static/SN.LOCK')
    file = open(FILE_PATH)
    fcntl.flock(file.fileno(), flag)
    _logger.info('Acquire Lock')
    return file


class DemoSequence(models.Model):
    _name = 'demo_sequence.fcntl'

    sn = fields.Char('SN', index=True)
    name = fields.Char('name')

    _sql_constraints = [
        ('sn_uniq', 'unique (sn)', "SN is duplicated!"),
    ]

    @api.model
    def create(self, vals):
        file = _file_lock()
        sn_prefix = 'SN' + datetime.date.today().strftime("%y%m%d")
        obj = self.env['demo_sequence.fcntl'].search_read([('sn', '=like', sn_prefix + '%')], limit=1, order='sn DESC')
        # 今天已经有序列号，在最新的序列号上递增
        if obj and obj[0]['sn'].startswith(sn_prefix):
            sn_suffix = int(obj[0]['sn'][-3:]) + 1
            vals['sn'] = sn_prefix + str(sn_suffix).zfill(3) # 补0
        else:
            vals['sn'] = sn_prefix + '001'

        res = super(DemoSequence, self).create(vals)
        # 关闭文件将自动解锁
        file.close()
        return res


class DemoSequence2(models.Model):
    _name = 'demo_sequence.sequence'

    sn = fields.Char('SN', index=True)
    name = fields.Char('name')

    _sql_constraints = [
        ('sn_uniq', 'unique (sn)', "SN is duplicated!"),
    ]

    @api.model
    def create(self, vals):
        vals['sn'] = self.env['ir.sequence'].next_by_code('demo_sequence.sequence')
        return super(DemoSequence2, self).create(vals)
