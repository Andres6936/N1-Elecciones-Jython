# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import unittest

from mundo.Candidato import Candidato

class CandidatoTest(unittest.TestCase):
    """
    Esta es la clase usada para verificar que los metodos de la
    clase esten correctamente  implementados.
    """
    
    def setupEscenario1(self):
        """
        Construye un nuevo Candidato.
        """
        self.candidato = Candidato("Felipe", "Pitti", "Independiente", 27)
    
    def testInicializar(self):
        """
        Prueba 1: Iniciaizar los datos del candidato correctamente
        """
        self.setupEscenario1()
        
        self.assertTrue(self.candidato.getNombre() == "Felipe", "No se crea con el nombre dado por parametro")
        self.assertTrue(self.candidato.getApellido() == "Pitti", "No se crea con el apellido dado por parametro")
        self.assertTrue(self.candidato.getPartidoPolitico() == "Independiente", "No se crea con el partido politico dado por parametro")
        self.assertTrue(self.candidato.getEdad() == 27, "No se crea con la edad dada por parametro")
        self.assertTrue(self.candidato.getCostoCampanha() == 0, "No se crea con el costo de campaña en 0")
        self.assertTrue(self.candidato.getVotos() == 0, "No se crea con el numero de votos en 0")
    
    def testAgregarVotoTelevision(self):
        self.setupEscenario1()
        
        self.candidato.agregarVotoTelevision()
        self.assertTrue(self.candidato.getVotos() == 1, "No aumenta el numero de votos en 1")
        self.assertTrue(self.candidato.getCostoCampanha() == 1000, "No aumenta el costo de campanha en 1000")
        
    def testAgregaVotoRadio(self):
        self.setupEscenario1()
        
        self.candidato.agregarVotoRadio()
        self.assertTrue(self.candidato.getVotos() == 1, "No aumenta el numero de votos en 1")
        self.assertTrue(self.candidato.getCostoCampanha() == 500, "No aumenta el costo de campanha en 500")
        
    def testAgregarVotoInternet(self):
        self.setupEscenario1()
        
        self.candidato.agregarVotoInternet()
        self.assertTrue(self.candidato.getVotos() == 1, "No aumenta el nuemro de votos en 1")
        self.assertTrue(self.candidato.getCostoCampanha() == 100, "No aumenta el costo de campanha en 100")
        
    def testReiniciarConteoVotos(self):
        self.setupEscenario1()
        
        self.candidato.agregarVotoTelevision()
        self.candidato.agregarVotoRadio()
        self.candidato.agregarVotoInternet()
        self.candidato.reiniciarConteoVotos()
        
        self.assertTrue(self.candidato.getVotos() == 0, "No inicializa el numero de votos a 0")
        
    def testReiniciarCostoCampanha(self):
        self.setupEscenario1()
        
        self.candidato.agregarVotoTelevision()
        self.candidato.agregarVotoRadio()
        self.candidato.agregarVotoInternet()
        self.candidato.reiniciarCostoCampanha()
        
        self.assertTrue(self.candidato.getCostoCampanha() == 0, "No inicializa el costo de campanha en 0")
    