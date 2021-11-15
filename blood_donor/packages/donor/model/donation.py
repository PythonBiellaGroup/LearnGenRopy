# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('donation',pkey='id',name_long='!![en]Donation',
                                    name_plural='!![en]Donations',caption_field='reference_num',
                                    partition_per_dep='department_id')
        self.sysFields(tbl)
        tbl.column('reference_num',name_long='!![en]Reference number')
        tbl.column('donator_id',size='22',name_long='!![en]Donator').relation(
                                    'donator.id',relation_name='donations', mode='foreignkey', onDelete='cascade')
        tbl.column('date',dtype='D',name_long='!![en]Date')
        tbl.column('result',dtype='B',name_long='!![en]Result')
        tbl.column('notes',name_long='!![en]Notes')

        tbl.aliasColumn('department_id', "@donator_id.department_id", name_long='!![en]Department', static=True)

    def defaultValues(self):
        return dict(date = self.db.workdate)

    def counter_reference_num(self,record=None):
        #2021/000001
        return dict(format='$K$YYYY/$NNNNNN', code='D', period='YYYY', date_field='date', showOnLoad=True, date_tolerant=True)

    def randomValues(self):
        return dict(date = dict(sorted=True))

    def trigger_onInserting(self, record):
        if record.get('matricola'):
            donator_number = record.get('matricola')
            donator_id = self.db.table('donor.donator').readColumns(where='$registration_num=:rn', 
                                                                    rn=donator_number, columns='$id')
            record['donator_id'] = donator_id
            #In alternativa è possibile definire un hook def importer_ per avere più controllo sul processo di importazione