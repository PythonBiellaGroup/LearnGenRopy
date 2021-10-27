# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('department_type',pkey='id',name_long='!![en]Department type',name_plural='!![en]Department types',caption_field='description',lookup=True)
        self.sysFields(tbl)
        tbl.column('description',name_long='!![en]Description')