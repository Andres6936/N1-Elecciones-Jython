# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

from mundo.Urna import Urna

from interfaz.PanelCandidato import PanelCandidato

from java.awt import BorderLayout
from java.awt import GridLayout

from javax.swing import JFrame
from javax.swing import JPanel

from interfaz.PanelUrna import PanelUrna
from interfaz.PanelImagen import PanelImagen
from interfaz.PanelExtension import PanelExtension

class InterfazElecciones(JFrame):
    
    def __init__(self):
        """
        Constructor donde se arma la interfaz
        """
        
        # Crea la clase principal
        self.urna = Urna()
        
        # Construye la forma
        self.setTitle('Elecciones Usaca')
        self.setLayout( BorderLayout() )
        self.setSize(800, 600)
        self.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE )
        self.setResizable(False)

        # Creación de los paneles aquí
        
        # Panel imagen
        self.panelImagen = PanelImagen();
        self.add(self.panelImagen, BorderLayout.NORTH)
        
        # Construye los paneles de los tres candidatos
        
        panelCandidatos = JPanel()
        panelCandidatos.setLayout(GridLayout( 1, 3 ))
        
        # Agregamos el panel temporal al JFrame
        self.add(panelCandidatos, BorderLayout.CENTER)
        
        self.panelCandidato1 = PanelCandidato()
        panelCandidatos.add(self.panelCandidato1)
        
        self.panelCandidato2 = PanelCandidato()
        panelCandidatos.add(self.panelCandidato2)
        
        self.panelCandidato3 = PanelCandidato()
        panelCandidatos.add(self.panelCandidato3)
        
        panelInferior = JPanel()
        panelInferior.setLayout(BorderLayout())
        self.add(panelInferior, BorderLayout.SOUTH)
        
        self.panelUrna = PanelUrna()
        panelInferior.add(self.panelUrna, BorderLayout.CENTER)
        
        self.panelExtension = PanelExtension()
        panelInferior.add(self.panelExtension, BorderLayout.SOUTH)
        
        self.setLocationRelativeTo(None)
        
        
    def actualizar(self):
        pass
        
    def adicionarVotoCandidato(self):
        pass
    
    def vaciarUrna(self):
        pass
    
    def mostrarDialogoPorcentajeVotos(self):
        pass
    
    def darTotalVotosUrna(self):
        pass
    
    def formatearValorReal(self):
        pass
    
    def reqFuncOpcion1(self):
        pass
    
    def reqFuncOpcion2(self):
        pass
        
        
        