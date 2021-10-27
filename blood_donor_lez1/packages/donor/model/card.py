# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('card', pkey='id', name_long='!![en]Card', name_plural='!![en]Cards',caption_field='surname')
        self.sysFields(tbl)
        
        tbl.column('name', name_long='!![en]Name')
        tbl.column('surname', name_long='!![en]Surname')
        tbl.column('birthdate', dtype='D', name_long='!![en]Birthdate')
        tbl.column('phone', name_long='!![en]Phone')
        tbl.column('email', name_long='!![en]E-mail')
        tbl.column('birthplace',size='22', group='_', name_long='!![en]Birthplace'
                    ).relation('glbl.comune.id', mode='foreignkey', onDelete='raise')
        tbl.column('address', name_long='!![en]Address')
        tbl.column('city_code', name_long='City code', name_short='City').relation(
                    'glbl.comune.id', mode='foreignkey', onDelete='raise')
        tbl.column('fiscal_code', size='16', name_long='Fiscal code')
        tbl.column('genre', name_long='!![en]Genre')

