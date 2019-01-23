# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

from javax.swing import JPanel, JButton
from javax.swing.border import TitledBorder
from java.awt import GridLayout

class PanelExtension(JPanel):
    
    VACIAR_URNA = "VACIAR_URNA"
    """
    Commando vaciar Urna
    """
    
    OPCION_1 = "OPCION_1"
    """
    Comando Opcion 1
    """
    
    OPCION_2 = "OPCION_2"
    """
    Comando Opcion 2
    """
    
    def __init__(self):
        
        self.setBorder(TitledBorder("Opciones"))
        self.setLayout(GridLayout(1, 3))
        
        # Boton vaciar Urna
        self.botonVaciarUrna = JButton("Vaciar Urna")
        self.botonVaciarUrna.setActionCommand(self.VACIAR_URNA)
        #self.botonVaciarUrna.addActionListener(self)
        self.add(self.botonVaciarUrna)
        
        self.botonOpcion1 = JButton("Opcion 1")
        self.botonOpcion1.setActionCommand(self.OPCION_1)
        #self.botonOpcion1.setActionListener(self)
        self.add(self.botonOpcion1)
        
        self.botonOpcion2 = JButton("Opcion 2")
        self.botonOpcion2.setActionCommand(self.OPCION_2)
        #self.botonOpcion2.setActionListener(self)
        self.add(self.botonOpcion2)
        
    def actionPerformed(self):
        pass
        
        