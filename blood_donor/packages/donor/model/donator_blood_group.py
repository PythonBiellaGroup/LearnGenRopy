# encoding: utf-8
from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('donator_blood_group',pkey='code',name_long='!![en]Blood group',
                            name_plural='!![en]Blood groups',caption_field='code',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('code',size=':3',name_long='!![en]Code')
        tbl.column('description',name_long='!![en]Description')

    #I sysRecord sono record generati automaticamente con lo script gnrdbsetup -u
    @metadata(mandatory=True)
    def sysRecord_APositive(self):
        return self.newrecord(code='A+',description='!![en]Group A, RH positive')

    @metadata(mandatory=True)
    def sysRecord_ANegative(self):
        return self.newrecord(code='A-',description='!![en]Group A, RH negative')

    @metadata(mandatory=True)
    def sysRecord_BPositive(self):
        return self.newrecord(code='B+',description='!![en]Group B, RH positive')

    @metadata(mandatory=True)
    def sysRecord_BNegative(self):
        return self.newrecord(code='B-',description='!![en]Group B, RH negative')

    @metadata(mandatory=True)
    def sysRecord_ABPositive(self):
        return self.newrecord(code='AB+',description='!![en]Group AB, RH positive')

    @metadata(mandatory=True)
    def sysRecord_ABNegative(self):
        return self.newrecord(code='AB-',description='!![en]Group AB, RH negative')

    @metadata(mandatory=True)
    def sysRecord_0Positive(self):
        return self.newrecord(code='0+',description='!![en]Group 0, RH positive')

    @metadata(mandatory=True)
    def sysRecord_0Negative(self):
        return self.newrecord(code='0-',description='!![en]Group 0, RH negative')