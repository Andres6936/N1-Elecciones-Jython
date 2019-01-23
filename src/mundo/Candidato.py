# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

class Candidato:
    """
    Candidato de la elección.
    """

    # ---------------------------------
    # Atributos
    # ---------------------------------



    # ---------------------------------
    # Constructor
    # ---------------------------------

    def __init__(self, nNombre, nApellido, nPartidoPolitico, nEdad):
        """
        Inicializa los datos del candidato con los valores que vienen por parámetro.
        Args:
            nNombre (str): Nombre del candidato.
            nApellido (str): Apellido del candidato.
            nPartidoPolitico (str): Partido político del candidato.
            nEdad (int): Edad del candidato.
        Poscondicion:
            El costo de campaña se inicializó en cero.
        """

        self.nombre = nNombre
        self.apellido = nApellido
        self.partidoPolitico = nPartidoPolitico
        self.edad = nEdad
        self.costoCampanha = 0
        self.votos = 0

    # ---------------------------------
    # Métodos
    # ---------------------------------

    def getNombre(self):
        """
        Devuelve el nombre del candidato.
        Returns:
            str: Nombre del candidato.
        """
        return self.nombre

    def getApellido(self):
        """
        Devuelve el apellido del candidato.
        Returns:
            str: Apellido del candidato.
        """
        return self.apellido

    def getPartidoPolitico(self):
        """
        Devuelve el partido político del candidato.
        Returns:
            str: Partido político del candidato.
        """
        return self.partidoPolitico

    def getEdad(self):
        """
        Devuelve la edad del candidato.
        Returns:
            int: Edad del candidato.
        """
        return self.edad

    def getCostoCampanha(self):
        """
        Devuelve el costo de campaña del candidato.
        Returns:
            float: Costo de campaña del candidato.
        """
        return self.costoCampanha

    def getVotos(self):
        """
        Devuelve el número de votos del candidato.
        Returns:
            int: Número de votos obtenidos.
        """
        return self.votos

    def ingresarUnVoto(self):
        """
        Ingresa un voto al candidato.
        Poscondicion:
            Se modificó el número de votos aumentándose el existente en 1.
        """
        self.votos += 1

    def agregarVotoTelevision(self):
        """
        Adiciona un voto influenciado por la televisión.
        Poscondicion:
            Se adiciona al costo de la camapaña
            la suma de $1000 y se incrementa el número de votos en 1.
        """
        self.costoCampanha += 1000
        self.ingresarUnVoto()

    def agregarVotoRadio(self):
        """
        Adiciona un voto influenciado por la radio.
        Poscondicion:
            Se adiciona al costo de la campaña la suma de $500 y se
            incrementa el número de votos en 1.
        """
        self.costoCampanha += 500
        self.ingresarUnVoto()

    def agregarVotoInternet(self):
        """
        Adiciona un voto influenciado por internet.
        Poscondicion:
            Se adiciona al costo de la camapaña la suma de $100
            y se incrementa el número de votos en 1.
        """
        self.costoCampanha += 100
        self.ingresarUnVoto()

    def reiniciarConteoVotos(self):
        """
        Se reinicia el conteo de votos.
        Poscondicion:
            self.votos = 0
        """
        self.votos = 0

    def reiniciarCostoCampanha(self):
        """
        Se reinicia el costo de camapaña.
        Poscondicion:
            self.costoCampanha = 0
        """
        self.costoCampanha = 0
