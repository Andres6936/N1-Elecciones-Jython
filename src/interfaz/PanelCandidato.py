# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

from javax.swing import JPanel
from javax.swing import JLabel
from javax.swing import JButton
from javax.swing import ImageIcon
from javax.swing import BorderFactory

from java.awt import BorderLayout
from java.awt import GridLayout
from java.awt import Dimension
from java.awt import Color

class PanelCandidato( JPanel ):
    """
    Panel que contiene la información de un candidato
    """
    
    PORCENTAJE_VOTOS = "Porcentaje Votos"
    """
    Comando actualizar datos del candidato
    """
    
    VOTAR = "Votar"
    """
    Comando votar por el candidato
    """
    
    def __init__(self, nCandidato):
        
        self.candidato = nCandidato
        
        self.botonDarPorcentajeVotos = JButton( self.PORCENTAJE_VOTOS )
        self.botonDarPorcentajeVotos.setPreferredSize(Dimension( 160, 20 ))
        self.botonDarPorcentajeVotos.setActionCommand(self.PORCENTAJE_VOTOS);
        #self.botonDarPorcentajeVotos.addActionListener(self)
        
        self.botonVotar = JButton( self.VOTAR )
        self.botonVotar.setPreferredSize(Dimension( 160, 20 ))
        self.botonVotar.setActionCommand(self.VOTAR)
        #self.botonVotar.addActionListener(self)
        
        self.etiquetaNombreCandidato = JLabel("Nombre: ")
        self.etiquetaNombreCandidato.setHorizontalAlignment(JLabel.LEFT)
        
        self.etiquetaApellidoCandidato = JLabel("Apellido: ")
        self.etiquetaApellidoCandidato.setHorizontalAlignment(JLabel.LEFT)
        
        self.etiquetaEdadCandidato = JLabel("Edad: ")
        self.etiquetaEdadCandidato.setHorizontalAlignment(JLabel.LEFT)
        
        self.etiquetaPartidoPoliticoCandidato = JLabel("Partido Politico: ")
        self.etiquetaPartidoPoliticoCandidato.setHorizontalAlignment(JLabel.LEFT)
        
        self.etiquetaCostoCampanhaCandidato = JLabel("Costo Campanha: $ ")
        self.etiquetaCostoCampanhaCandidato.setHorizontalAlignment(JLabel.LEFT)
        
        self.etiquetaNumeroVotos = JLabel("Numero de Votos: ")
        self.etiquetaNumeroVotos.setHorizontalAlignment(JLabel.CENTER)
        self.etiquetaNumeroVotos.setForeground(Color.RED.darker( ))
        
        panelImagen = JPanel()
        panelInformacion = JPanel()
        
        self.setLayout(BorderLayout( ))
        self.setBorder(BorderFactory.createTitledBorder("Candidato"))
        
        self.add(panelImagen, BorderLayout.CENTER)
        panelImagen.setLayout(BorderLayout( ))
        
        etiquetaTemp = JLabel()
        etiquetaTemp.setHorizontalAlignment(JLabel.CENTER)
        etiquetaTemp.setIcon(ImageIcon( "data/Candidato1.gif" ))
        
        panelImagen.add(etiquetaTemp, BorderLayout.CENTER)
        
        panelInformacion.setLayout(GridLayout(8, 1))
        
        panelInformacion.add(self.etiquetaNombreCandidato)
        panelInformacion.add(self.etiquetaApellidoCandidato)
        panelInformacion.add(self.etiquetaEdadCandidato)
        panelInformacion.add(self.etiquetaPartidoPoliticoCandidato)
        panelInformacion.add(self.etiquetaCostoCampanhaCandidato)
        panelInformacion.add(self.etiquetaNumeroVotos)
        
        panelInformacion.add(self.botonDarPorcentajeVotos)
        panelInformacion.add(self.botonVotar)
        
        self.add(panelInformacion, BorderLayout.SOUTH)
        
    def actualizar(self):
        
        self.etiquetaNombreCandidato.setText("Nombre: " + self.candidato.getNombre())
        self.etiquetaApellidoCandidato.setText("Apellido: " + self.candidato.getApellido())
        self.etiquetaEdadCandidato.setText("Edad: " + str(self.candidato.getEdad()))
        self.etiquetaPartidoPoliticoCandidato.setText("Partido Politico: " + self.candidato.getPartidoPolitico())
        self.etiquetaCostoCampanhaCandidato.setText("Costo Campanha: $" + str(self.candidato.getCostoCampanha()))
        self.etiquetaNumeroVotos.setText("Numero de Votos: " + str(self.candidato.getVotos()))
    
    def actionPerformed(self):
        pass
    
    def formatearValorReal(self):
        pass
        
        