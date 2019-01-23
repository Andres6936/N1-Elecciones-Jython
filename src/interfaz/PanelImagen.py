# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

from javax.swing import JPanel, ImageIcon, JLabel
from java.awt import BorderLayout, Color

class PanelImagen(JPanel):
    
    def __init__(self):
        
        self.setLayout(BorderLayout())
        self.setBackground(Color.white)
        
        self.etiquetaImagen = JLabel("")
        self.etiquetaImagen.setHorizontalAlignment(JLabel.CENTER)
        self.etiquetaImagen.setVerticalAlignment(JLabel.CENTER)
        self.etiquetaImagen.setIcon(ImageIcon("data/Encabezado.jpg"))
        
        self.add(self.etiquetaImagen, BorderLayout.CENTER)
        