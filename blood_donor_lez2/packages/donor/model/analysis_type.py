# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('analysis_type',pkey='id',name_long='Analysis type',name_plural='Analysis types',caption_field='description',lookup=True)
        self.sysFields(tbl)
        tbl.column('description',name_long='Description')