# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

from mundo.Candidato import Candidato

class Urna:
    """
    Es la urna de votación con tres candidatos.
    """

    # ---------------------------------
    # Atributos
    # ---------------------------------



    # ---------------------------------
    # Constructor
    # ---------------------------------

    def __init__(self):
        """
        Inicializa los tres candidatos.
        Poscondicion:
            Se inicializaron los tres candidatos con los valores por parámetro
            nombre, apellido, partido político y edad.
        """

        # Inicializa el candidato 1.
        self.candidato1 = Candidato('Felipe', 'Pitti', 'Independiente', 27)
        """
        El candidato número 1 de las elecciones.
        """

        # Inicializa el candidato 2.
        self.candidato2 = Candidato('Susanita', 'Chirusi', 'Revolucionario', 26)
        """
        El candidato número 2 de las elecciones.
        """

        # Inicializa el candidato 3.
        self.candidato3 = Candidato('Manolito', 'Goreiro', 'Tradicional', 26)
        """
        El candidato número 3 de las elecciones.
        """

    # ---------------------------------
    # Métodos
    # ---------------------------------


    def getCandidato1(self):
        """
        Devuelve el candidato 1.
        Returns:
            Candidato: Candidato 1
        """
        return self.candidato1

    def getCandidato2(self):
        """
        Devuelve el candidato 2.
        Returns:
            Candidato: Candidato 2.
        """
        return self.candidato2

    def getCandidato3(self):
        """
        Devuelve el candidato 3.
        Returns:
            Candidato: Candidato 3.
        """
        return self.candidato3

    def ingresarVotoTelevisionCandidato(self, nCandidato):
        """
        Ingresa un voto influenciado por la television al candidato.
        
        Args:
            nCandidato (Candidato): Candidato a ingresar voto.
            
        Poscondition:
            Aumenta en 1 los votos al candidato.
        """
        nCandidato.agregarVotoTelevision()
        
    def ingresarVotoRadioCandidato(self, nCandidato):
        """
        Ingresa un voto influeciado por la radio al candidato.
        
        Args:
            nCandidato (Candidato): Candidato a ingresar voto.
            
        Poscondition:
            Aumenta en 1 los votos al candidato.
        """
        nCandidato.agregarVotoRadio()
        
    def ingresarVotoInternetCandidato(self, nCandidato):
        """
        Ingresar un voto influenciado por la internet al candidato.
        
        Args:
            nCandidato (Candidato): Candidato a ingresar voto.
            
        Poscondition:
            Aumenta en 1 los votos al candidato.
        """
        nCandidato.agregarVotoInternet()

    def calcularTotalVotos(self):
        """
        Devuelve el total de votos en la urna.
        Returns:
            int: La sumatoria de los votos de los tres candidatos.
        """
        return self.candidato1.getVotos() + self.candidato2.getVotos() + self.candidato3.getVotos()

    def calcularCostoPromedioCampanha(self):
        """
        Devuelve el costo promedio de camapaña de los candidatos.
        Returns:
            float: La razón de la sumatoria de los costos de la campaña de
            los candidatos y el número total de candidatos.
        """

        total = self.candidato1.getCostoCampanha() + self.candidato2.getCostoCampanha() + self.candidato3.getCostoCampanha()
        promedio = total / 3

        return promedio
    
    def calcularPorcentajeVotosCandidato(self, nCandidato):
        """
        Devuelve el porcentaje de votos obtenido por el candidato.
        
        Args:
            nCandidato (Candidato): Candidato a promediar.
            
        Returns:
            float: Porcentaje de votos obtneidos por el candidato.
        """
        numeroVotosCandidato = nCandidato.getVotos()
        votosTotales = self.calcularTotalVotos()
        
        if (votosTotales != 0):
            porcentaje = numeroVotosCandidato / votosTotales * 100
        else:
            return 0
        
        return porcentaje

    def vaciarUrna(self):
        """
        Restaura la urna al estado inicial, todos los candidatos qeudan sin votos y
        costo de campaña en 0.
        """

        # Reiniciar candidato 1.
        self.candidato1.reiniciarConteoVotos()
        self.candidato1.reiniciarCostoCampanha()

        # Reiniciar candidato 2.
        self.candidato2.reiniciarConteoVotos()
        self.candidato2.reiniciarCostoCampanha()

        # Reinicia candidato 3.
        self.candidato3.reiniciarConteoVotos()
        self.candidato3.reiniciarCostoCampanha()

    # ---------------------------------
    # Punto de Extensión
    # ---------------------------------

    def metodo1(self):
        """
        Método para la extensión 1.
        Returns:
            str: Respuesta 1.
        """
        return 'Respuesta 1'

    def metodo2(self):
        """
        Método para la extensión 2.
        Returns:
            str: Respuesta 2.
        """
        return 'Respuesta 2'
