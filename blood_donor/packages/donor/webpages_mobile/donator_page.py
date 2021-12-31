# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    # Importazione CSS
    # Path ed estensione non servono
    css_requires='donor_style'
    
    def main(self, root, **kwargs):
        root.div("Questa è la mobile page", _class='donator_div')
