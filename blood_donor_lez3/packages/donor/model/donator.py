# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('donator',pkey='id',name_long='!![en]Donator',name_plural='!![en]Donators',caption_field='fullname')
        self.sysFields(tbl)

        tbl.column('registration_num', size='6',name_long='Registration number', name_short='Reg.num.')
        tbl.column('user_id',size='22', group='_', name_long='!![en]User'
                    ).relation('adm.user.id', mode='foreignkey', onDelete='raise', one_one='*')
        tbl.column('card_id',size='22', group='_', name_long='!![en]Card'
                    ).relation('donor.card.id', mode='foreignkey', onDelete='raise', one_one='*') 
        tbl.column('blood_group_code',size=':3',name_long='!![en]Blood Group', validate_notnull=True).relation(
                    'donator_blood_group.code',relation_name='donators', mode='foreignkey', onDelete='raise')
        tbl.column('department_id',size='22',name_long='!![en]Department').relation('department.id',relation_name='donators', mode='foreignkey', onDelete='raise')
        tbl.column('job',name_long='Job')
        tbl.column('journal_request',dtype='B',name_long='!![en]Journal request')
        tbl.column('news_request',dtype='B',name_long='!![en]News request')
        tbl.column('notes',name_long='!![en]Notes')

        tbl.aliasColumn('fullname', "@card_id.fullname", name_long='!![en]Fullname')
        tbl.aliasColumn('surname', "@card_id.surname", name_long='!![en]Surname', static=True)

        tbl.formulaColumn('first_donation_date', select=dict(table='donor.donation', columns='$date',
                                                                where='$donator_id=#THIS.id',
                                                                order_by='$date ASC', limit=1),
                                                                dtype='D', name_long='!![en]First donation date')
        tbl.formulaColumn('last_donation_date', select=dict(table='donor.donation', columns='$date',
                                                                where='$donator_id=#THIS.id',
                                                                order_by='$date DESC', limit=1),
                                                                dtype='D', name_long='!![en]Last donation date')
        tbl.formulaColumn('is_active', "CASE WHEN $last_donation_date > NOW() - INTERVAL '365 DAYS' THEN TRUE ELSE FALSE END",
                                                                dtype='B', name_long='!![en]Is active')
        tbl.formulaColumn('donations_number', select=dict(table='donor.donation', columns='COUNT(*)',
                                                                where='$donator_id=#THIS.id'),
                                                                dtype='I', name_long='!![en]Donations number')                                                        

    def counter_registration_num(self,record=None):
        return dict(format='$NNNNNN', code='')

    def randomValues(self):
        return dict(registration_num=False)