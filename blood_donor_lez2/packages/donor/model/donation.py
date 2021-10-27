# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('donation',pkey='id',name_long='Donation',name_plural='Donations',caption_field='reference_num')
        self.sysFields(tbl)
        tbl.column('reference_num',name_long='Reference number')
        tbl.column('donator_id',size='22',name_long='Donator').relation('donator.id',relation_name='donations', mode='foreignkey', onDelete='raise')
        tbl.column('date',dtype='D',name_long='Date')
        tbl.column('result',dtype='B',name_long='Result')
        tbl.column('notes',name_long='Notes')

    def defaultValues(self):
        return dict(date = self.db.workdate)

    def counter_reference_num(self,record=None):
        #2021/000001
        return dict(format='$K$YYYY/$NNNNNN', code='D', period='YYYY', date_field='date', showOnLoad=True)

    def randomValues(self):
        return dict(date = dict(sorted=True))