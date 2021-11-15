# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('department',pkey='id',name_long='!![en]Department',name_plural='!![en]Departments',caption_field='name')
        self.sysFields(tbl)
        tbl.column('address',name_long='!![en]Address')
        tbl.column('name',name_long='!![en]Name')
        tbl.column('type_id',size='22',name_long='!![en]Type').relation('department_type.id',relation_name='departments', mode='foreignkey', onDelete='raise')
        tbl.column('telephone',name_long='!![en]Telephone')
        tbl.column('email',name_long='!![en]E-mail')
        tbl.column('city_id',size='22',name_long='!![en]City').relation('glbl.comune.id',relation_name='departments', mode='foreignkey', onDelete='raise')
        tbl.column('notes',name_long='!![en]Notes')
