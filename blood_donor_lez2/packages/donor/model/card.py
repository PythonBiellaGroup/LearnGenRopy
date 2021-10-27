# encoding: utf-8

import names

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('card', pkey='id', name_long='Card', name_plural='Cards', caption_field='full_name')
        self.sysFields(tbl)
        
        tbl.column('name',name_long='Name')
        tbl.column('surname',name_long='Surname')
        tbl.column('birthplace_id',size='22',name_long='Birthplace').relation(
                    'glbl.comune.id',relation_name='donators_by_birthplace', mode='foreignkey', onDelete='raise')
        tbl.column('gender',name_long='Gender', values='M:Male,F:Female')
        tbl.column('birthdate',dtype='D',name_long='Birthdate')
        tbl.column('telephone',name_long='Telephone')
        tbl.column('email',name_long='E-mail')
        tbl.column('address',name_long='Address')
        tbl.column('city_id',size='22',name_long='City').relation(
                    'glbl.comune.id',relation_name='donators_by_city', mode='foreignkey', onDelete='raise')
        tbl.column('fiscal_code',size='16',name_long='Fiscal code')

        tbl.formulaColumn('fullname', "$surname ||' '||$name", name_long='Fullname')

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