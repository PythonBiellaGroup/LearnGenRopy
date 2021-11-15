# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('analysis_type',pkey='id',name_long='!![en]Analysis type',
                            name_plural='!![en]Analysis types',caption_field='description')
        self.sysFields(tbl, hierarchical='description')
        tbl.column('description',name_long='!![en]Description')