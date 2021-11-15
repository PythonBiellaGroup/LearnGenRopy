# -*- coding: UTF-8 -*-

from gnr.web.gnrwebpage import BaseComponent
        
class LoginComponent(BaseComponent):
    
    def onAuthenticating_donor(self,avatar,rootenv=None):
        department_id = self.db.table('donor.staff').readColumns(where='$user_id=:u_id', 
                            u_id=avatar.user_id, columns='$department_id')
        rootenv['current_department_id'] = department_id 