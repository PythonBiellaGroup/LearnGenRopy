# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('staff', pkey='id', caption_field='username', name_long='!![en]Staff')
        self.sysFields(tbl)

        tbl.column('user_id',size='22', group='_', name_long='!![en]User'
                    ).relation('adm.user.id', relation_name='staff', mode='foreignkey', onDelete='raise')
        tbl.column('department_id', size='22', name_long='!![en]Department').relation('donor.department.id',
                        relation_name='user', mode='foreignkey', onDelete='raise')    
        tbl.column('is_active', dtype='B', name_long='!![en]Is active')    

        tbl.aliasColumn('username', '@user_id.username', name_long='!![en]Username')