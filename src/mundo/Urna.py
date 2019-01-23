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

    def ingresarVotoTelevisionCandidato1(self):
        """
        Ingresa un voto influenciado por la televisión al candidato 1.
        """
        self.candidato1.agregarVotoTelevision()

    def ingresarVotoRadioCandidato1(self):
        """
        Ingresa un voto influenciado por radio al candidato 1.
        """
        self.candidato1.agregarVotoRadio()

    def ingresarVotoInternetCandidato1(self):
        """
        Ingresa un voto influenciado por internet al candidato 1.
        """
        self.candidato1.agregarVotoInternet()

    def ingresarVotoTelevisionCandidato2(self):
        """
        Ingresa un voto influenciado por la televisión al candidato 2.
        """
        self.candidato2.agregarVotoTelevision()

    def ingresarVotoRadioCandidato2(self):
        """
        Ingresa un voto influenciado por radio al candidato 2.
        """
        self.candidato2.agregarVotoRadio()

    def ingresarVotoInternetCandidato2(self):
        """
        Ingresa un voto influenciado por internet al candidato 2.
        """
        self.candidato2.agregarVotoInternet()

    def ingresarVotoTelevisionCandidato3(self):
        """
        Ingresa un voto influenciado por la televisión al candidato 3.
        """
        self.candidato3.agregarVotoTelevision()

    def ingresarVotoRadioCandidato3(self):
        """
        Ingresa un voto influenciado por radio al candidato 3.
        """
        self.candidato3.agregarVotoRadio()

    def ingresarVotoInternetCandidato3(self):
        """
        Ingresa un voto influenciado por internet al candidato 3.
        """
        self.candidato3.agregarVotoInternet()

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

    def calcularPorcentajeVotosCandidato1(self):
        """
        Devuelve el porcentaje de votos obtenidos por el candidato 1.
        Returns:
            float: Porcentaje de votos obtenidos por el candidato 1.
        """

        numVotosCandidato1 = self.candidato1.getVotos()
        votosTotales = self.calcularTotalVotos()

        porcentaje = numVotosCandidato1 / votosTotales * 100

        return porcentaje

    def calcularPorcentajeVotosCandidato2(self):
        """
        Devuelve el porcentaje de votos obtenidos por el candidato 2.
        Returns:
            float: Porcentaje de votos obtenidos por el candidato 2.
        """

        numVotosCandidato2 = self.candidato2.getVotos()
        votosTotales = self.calcularTotalVotos()

        porcentaje = numVotosCandidato2 / votosTotales * 100

        return porcentaje

    def calcularPorcentajeVotosCandidato3(self):
        """
        Devuelve el porcentaje de votos obtenidos por el candidato 3.
        Returns:
            float: Porcentaje de votos obtenidos por el candidato 3.
        """

        numVotosCandidato3 = self.candidato3.getVotos()
        votosTotales = self.calcularTotalVotos()

        porcentaje = numVotosCandidato3 / votosTotales * 100

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
