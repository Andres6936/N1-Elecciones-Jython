# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import unittest

from mundo.Urna import Urna

class UrnaTest(unittest.TestCase):

    def setupEscenario1(self):
        self.urna = Urna()
        
    def setupEscenario2(self):
        self.urna = Urna()
        
        self.urna.ingresarVotoTelevisionCandidato(self.urna.candidato1)
        self.urna.ingresarVotoTelevisionCandidato(self.urna.candidato2)
        self.urna.ingresarVotoTelevisionCandidato(self.urna.candidato3)
        
        self.urna.ingresarVotoRadioCandidato(self.urna.candidato1)
        self.urna.ingresarVotoRadioCandidato(self.urna.candidato2)
        self.urna.ingresarVotoRadioCandidato(self.urna.candidato3)
        
        self.urna.ingresarVotoInternetCandidato(self.urna.candidato1)
        self.urna.ingresarVotoInternetCandidato(self.urna.candidato2)
        self.urna.ingresarVotoInternetCandidato(self.urna.candidato3)
        
    def testInicializacion(self):
        self.setupEscenario1()
        
        self.assertIsNotNone(self.urna.candidato1, "El candidato 1 debe estar inicializado")
        self.assertIsNotNone(self.urna.candidato2, "El candidato 2 debe estar inicializado")
        self.assertIsNotNone(self.urna.candidato3, "El candidato 3 debe estar inicializado")
        
    def testIngresarVotoTelevisionCandidatos(self):
        """
        Prueba 2: Ingresa un voto influeciado por la television a todos los candidatos
        """
        self.setupEscenario1()
        
        self.urna.ingresarVotoTelevisionCandidato(self.urna.candidato1)
        self.urna.ingresarVotoTelevisionCandidato(self.urna.candidato2)
        self.urna.ingresarVotoTelevisionCandidato(self.urna.candidato3)
        
        self.assertTrue(self.urna.candidato1.getVotos() == 1, "Deberia aumentar el numero de votos en 1")
        self.assertTrue(self.urna.candidato2.getVotos() == 1, "Deberia aumentar el numero de votos en 1")
        self.assertTrue(self.urna.candidato3.getVotos() == 1, "Deberia aumentar el numero de votos en 1")
        
        self.assertTrue(self.urna.candidato1.getCostoCampanha() == 1000, "Deberia aumentar el costo de campanha en 1000")
        self.assertTrue(self.urna.candidato2.getCostoCampanha() == 1000, "Deberia aumentar el costo de campanha en 1000")
        self.assertTrue(self.urna.candidato3.getCostoCampanha() == 1000, "Deberia aumentar el costo de campanha en 1000")
    
    def testIngresarVotoRadioCandidatos(self):
        """
        Prueba 3: Ingresa un voto influenciado por la radio a todos los candidatos
        """
        self.setupEscenario1()
        
        self.urna.ingresarVotoRadioCandidato(self.urna.candidato1)
        self.urna.ingresarVotoRadioCandidato(self.urna.candidato2)
        self.urna.ingresarVotoRadioCandidato(self.urna.candidato3)
        
        self.assertTrue(self.urna.candidato1.getVotos() == 1, "Deberia aumentar el numero de votos en 1")
        self.assertTrue(self.urna.candidato2.getVotos() == 1, "Deberia aumentar el numero de votos en 1")
        self.assertTrue(self.urna.candidato3.getVotos() == 1, "Deberia aumentar el numero de votos en 1")
        
        self.assertTrue(self.urna.candidato1.getCostoCampanha() == 500, "Deberia aumentar el costo de campanha en 500")
        self.assertTrue(self.urna.candidato2.getCostoCampanha() == 500, "Deberia aumentar el costo de campanha en 500")
        self.assertTrue(self.urna.candidato3.getCostoCampanha() == 500, "Deberia aumentar el costo de campanha en 500")
    
    def testIngresarVotoInternetCandidatos(self):
        """
        Prueba 4: Ingresa un voto influenciado por la internet a todos los candidatos
        """
        self.setupEscenario1()
        
        self.urna.ingresarVotoInternetCandidato(self.urna.candidato1)
        self.urna.ingresarVotoInternetCandidato(self.urna.candidato2)
        self.urna.ingresarVotoInternetCandidato(self.urna.candidato3)
        
        self.assertTrue(self.urna.candidato1.getVotos() == 1, "Deberia aumentar el numero de votos en 1")
        self.assertTrue(self.urna.candidato2.getVotos() == 1, "Deberia aumentar el numero de votos en 1")
        self.assertTrue(self.urna.candidato3.getVotos() == 1, "Deberia aumentar el numero de votos en 1")
        
        self.assertTrue(self.urna.candidato1.getCostoCampanha() == 100, "Deberia aumentar el costo de campanha en 100")
        self.assertTrue(self.urna.candidato2.getCostoCampanha() == 100, "Deberia aumentar el costo de campanha en 100")
        self.assertTrue(self.urna.candidato3.getCostoCampanha() == 100, "Deberia aumentar el costo de campanha en 100")
        
    def testCalcularTotalVotos(self):
        """
        Prueba 5: Calcula el total de votos que posee la urna
        """
        self.setupEscenario2()
        
        self.assertTrue(self.urna.calcularTotalVotos() == 9, "No calcula el total de votos correctamente")
        
    def testCalcularCostoPromedioCampanha(self):
        """
        Prueba 6: Calcula el costo promedio de campanha de los candidatos
        """
        self.setupEscenario2()
        
        self.assertTrue(self.urna.calcularCostoPromedioCampanha() == 1600, "No calcula el costo promedio de campanha correctamente")
        
    def testVaciarUrna(self):
        """
        Prueba 7: Vaciar la urna de votacion
        """
        self.setupEscenario2()
        
        self.urna.vaciarUrna()
        
        self.assertTrue(self.urna.candidato1.getVotos() == 0, "No inicializa el numero de votos a 0 del candidato 1")
        self.assertTrue(self.urna.candidato1.getCostoCampanha() == 0, "No inicializa el costo de campanha a 0 del candidato 1")
        
        self.assertTrue(self.urna.candidato2.getVotos() == 0, "No inicializa el numero de votos a 0 del candidato 2")
        self.assertTrue(self.urna.candidato2.getCostoCampanha() == 0, "No inicializa el costo de campanha a 0 del candidato 1")
                        
        self.assertTrue(self.urna.candidato3.getVotos() == 0, "No inicializa el numero de votos a 0 del candidato 3")
        self.assertTrue(self.urna.candidato3.getCostoCampanha() == 0, "No inicializa el costo de campanha a 0 del candidato 1")
        