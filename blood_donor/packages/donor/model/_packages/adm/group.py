#!/usr/bin/env python
# encoding: utf-8
# Overloading di group del package adm solo per aggiungere record di configurazione/sistema
# Non ridefiniamo colonne

from gnr.core.gnrdecorator import metadata

class Table(object):
    @metadata(mandatory=True)
    def sysRecord_AN(self):
        return self.newrecord(code='AN',description='Ammistratore Nazionale',
                              hierarchical_code='AN')

    def sysRecord_AL(self):
        return self.newrecord(code='AL',description='Ammistratore Locale',
                              hierarchical_code='AL')

    def sysRecord_S(self):
        return self.newrecord(code='S',description='Staff',
                              hierarchical_code='S')

    def sysRecord_D(self):
        return self.newrecord(code='D',description='Donatore',
                              hierarchical_code='D')
