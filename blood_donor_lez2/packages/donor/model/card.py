# encoding: utf-8

import names

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('card', pkey='id', name_long='!![en]Card', name_plural='!![en]Cards', caption_field='fullname')
        self.sysFields(tbl)
        
        tbl.column('name',name_long='!![en]Name')
        tbl.column('surname',name_long='!![en]Surname')
        tbl.column('birthplace_id',size='22',name_long='!![en]Birthplace').relation(
                    'glbl.comune.id',relation_name='donators_by_birthplace', mode='foreignkey', onDelete='raise')
        tbl.column('gender',name_long='!![en]Gender', values='M:Male,F:Female')
        tbl.column('birthdate',dtype='D',name_long='!![en]Birthdate')
        tbl.column('telephone',name_long='!![en]Telephone')
        tbl.column('email',name_long='!![en]E-mail')
        tbl.column('address',name_long='!![en]Address')
        tbl.column('city_id',size='22',name_long='!![en]City').relation(
                    'glbl.comune.id',relation_name='donators_by_city', mode='foreignkey', onDelete='raise')
        tbl.column('fiscal_code',size='16',name_long='!![en]Fiscal code')

        tbl.formulaColumn('fullname', "$surname ||' '||$name", name_long='!![en]Fullname')

    def randomValues(self):
        return dict(name=dict(default_value='batch_#P'), fiscal_code=False,
                    city_id=dict(ask=False), birthplace_id=dict(ask=False),
                    email=False)

    def trigger_onInserting(self, record):
        if record['name'].startswith('batch_'):
            record['name'] = names.get_first_name()
            record['surname'] = names.get_last_name()
            record['email'] = '{name}.{surname}@gmail.com'.format(name=record['name'].lower(), 
                                                                    surname=record['surname'].lower())