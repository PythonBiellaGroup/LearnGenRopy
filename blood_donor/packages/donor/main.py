#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='donor package',sqlschema='donor',sqlprefix=True,
                    name_short='Donor', name_long='Donor', name_full='Blood Donor')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
