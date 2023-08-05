# -*- coding: utf-8 -*-
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from trytond.report import Report


class ReportOdt(Report):
    __name__ = 'pim_memos.reportodt'

    @classmethod
    def execute(cls, ids, data):
        """ edit filename
        """
        pool = Pool()
        IrDate = pool.get('ir.date')
        ExpObj = pool.get(data['model'])(data['id'])

        (ext1, cont1, dirprint, titel) = super(ReportOdt, cls).execute(ids, data)
        titel = '%s-note-%s' % (IrDate.today().strftime('%Y%m%d'), ExpObj.rec_name[:15])
        return (ext1, cont1, dirprint, titel)

    @classmethod
    def get_context(cls, records, header, data):
        report_context = super(ReportOdt, cls).get_context(records, header, data)
        report_context['islastitem'] = cls.is_last_item
        return report_context

    @classmethod
    def is_last_item(cls, liste, item):
        """ check if 'item' is the last in 'liste'
        """
        if liste[-1].id == item.id:
            return True
        else :
            return False

# ende ReportOdt

