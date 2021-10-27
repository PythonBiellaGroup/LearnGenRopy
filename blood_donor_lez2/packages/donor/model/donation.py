# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('donation',pkey='id',name_long='!![en]Donation',name_plural='!![en]Donations',caption_field='reference_num')
        self.sysFields(tbl)
        tbl.column('reference_num',name_long='!![en]Reference number')
        tbl.column('donator_id',size='22',name_long='!![en]Donator').relation('donator.id',relation_name='donations', mode='foreignkey', onDelete='raise')
        tbl.column('date',dtype='D',name_long='!![en]Date')
        tbl.column('result',dtype='B',name_long='!![en]Result')
        tbl.column('notes',name_long='!![en]Notes')

    def defaultValues(self):
        return dict(date = self.db.workdate)

    def counter_reference_num(self,record=None):
        #2021/000001
        return dict(format='$K$YYYY/$NNNNNN', code='D', period='YYYY', date_field='date', showOnLoad=True)

    def randomValues(self):
        return dict(date = dict(sorted=True))