# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

from javax.swing import JPanel, JLabel
from javax.swing.border import TitledBorder
from java.awt import GridLayout, Color, Font, Dimension

class PanelUrna(JPanel):
    
    def __init__(self):
        
        self.setBorder(TitledBorder("Totales"))
        self.setLayout(GridLayout(2, 1))
        
        # Etiqueta total votos
        self.etiquetaTotalVotos = JLabel("Total Votos: ")
        self.etiquetaTotalVotos.setHorizontalAlignment(JLabel.CENTER)
        self.etiquetaTotalVotos.setForeground(Color.BLUE.darker())
        self.etiquetaTotalVotos.setFont(Font("Tahoma", Font.BOLD, 24))
        
        # Etiqueta total costo de campanha
        self.etiquetaPromedioCostoCampanha = JLabel("Costo Promedio Campanha: $")
        self.etiquetaPromedioCostoCampanha.setHorizontalAlignment(JLabel.CENTER)
        self.etiquetaPromedioCostoCampanha.setForeground(Color.BLUE.darker())
        self.etiquetaPromedioCostoCampanha.setFont(Font("Tahoma", Font.BOLD, 24))
        
        self.add(self.etiquetaTotalVotos)
        self.add(self.etiquetaPromedioCostoCampanha)
        
        self.setPreferredSize(Dimension(78, 78))
        
    def actualizar(self, nUrna):
        self.etiquetaTotalVotos.setText("Total Votos: " + str(nUrna.calcularTotalVotos()))
        self.etiquetaPromedioCostoCampanha.setText("Costo Promedio Campanha: $" + str(nUrna.calcularCostoPromedioCampanha()))
    
    def formatearValorReal(self):
        pass