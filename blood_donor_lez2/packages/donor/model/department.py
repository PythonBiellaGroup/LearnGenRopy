# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('department',pkey='id',name_long='Department',name_plural='Departments',caption_field='name')
        self.sysFields(tbl)
        tbl.column('address',name_long='Address')
        tbl.column('name',name_long='Name')
        tbl.column('type_id',size='22',name_long='Type').relation('department_type.id',relation_name='departments', mode='foreignkey', onDelete='raise')
        tbl.column('telephone',name_long='Telephone')
        tbl.column('email',name_long='E-mail')
        tbl.column('city_id',size='22',name_long='City').relation('glbl.comune.id',relation_name='departments', mode='foreignkey', onDelete='raise')
        tbl.column('notes',name_long='Notes')
