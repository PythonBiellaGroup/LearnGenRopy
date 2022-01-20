# encoding: utf-8

from gnr.web.gnrbaseclasses import BaseComponent

#Creando un component possiamo richiamare un blocco di codice al bisogno
class CardForm(BaseComponent):
    
    def cardForm(self, pane, title=None, rel_name=None):
        '''
        Aggiunti parametri per gestire l'univocità del soggetto (card)
        che può essere sia donatore che membro dello staff
        '''
        # Evoluzioni Donor #1
        # bc = pane.borderContainer(datapath='.@card_id')
        rgf = pane.roundedGroupFrame()
        rgf.top.linkerBar(field="card_id", newRecordOnly=False, openIfEmpty=True,
                          condition=f"@{rel_name}.id IS NULL OR @{rel_name}.id=:rec_id", 
                          condition_rec_id='^#FORM.record.id', label=title)
        #Passando la table al formbuilder, possiamo sfruttare la "magia" del field
        bce = rgf.center.borderContainer(datapath='.@card_id')
        fb = bce.contentPane(region="center").formbuilder(cols=2, border_spacing='4px', table='donor.card')
        fb.field('name')
        fb.field('surname')
        fb.field('birthplace_id')
        fb.field('gender')
        fb.field('birthdate')
        fb.field('telephone')
        fb.field('email')
        fb.field('address')
        fb.field('city_id')
        fb.field('fiscal_code')

        right = bce.contentPane(region='right', width='100px', margin='10px')
        right.img(src='^.profile_photo', edit=True, crop_width='100px', crop_height='100px', 
                        placeholder=True, upload_folder='site:avatar', upload_filename='=.id')