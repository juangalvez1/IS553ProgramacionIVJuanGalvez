class Paciente:
    def __init__(self, documento: int, nombre: str, edad: int, estadoDeAtencion: str):
        self.__documento = documento
        self.__nombre = nombre
        self.__edad = edad
        self.__estadoDeAtencion = estadoDeAtencion

    @property
    def documento(self):
        return self.__documento
    
    @documento.setter
    def documento(self, documento: int):
        self.__documento = documento

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad: int):
        self.__edad = edad

    @property
    def estadoDeAtencion(self):
        return self.__estadoDeAtencion
    
    @estadoDeAtencion.setter
    def estadoDeAtencion(self, estadoDeAtencion: str):
        self.__estadoDeAtencion = estadoDeAtencion

    def toDict(self):
        return {
            "documento": self.__documento,
            "nombre": self.__nombre,
            "edad": self.__edad,
            "estadoDeAtencion": self.__estadoDeAtencion
        }

    def __str__(self):
        return f"Documento: {self.__documento:<5} | Nombre: {self.__nombre:<20} | Edad: {self.__edad:<3} | Estado de atención: {self.__estadoDeAtencion:<10}"
    
class PacienteGeneral(Paciente):
    def __init__(self, documento: int, nombre: str, edad: int, estadoDeAtencion: str, nombreEps: str):
        super().__init__(documento, nombre, edad, estadoDeAtencion)
        self.__nombreEps = nombreEps

    @property
    def nombreEps(self):
        return self.__nombreEps
    @nombreEps.setter
    def nombreEps(self, nombreEps: str):
        self.__nombreEps = nombreEps

    def toDict(self):
        data = super().toDict()
        data["nombreEps"] = self.__nombreEps
        return data

    def __str__(self):
        return super().__str__() + f" | EPS: {self.__nombreEps:<7}"
    
class PacientePrioritario(Paciente):
    def __init__(self, documento: int, nombre: str, edad: int, estadoDeAtencion: str, condicionEspecial: str):
        super().__init__(documento, nombre, edad, estadoDeAtencion)
        self.__condicionEspecial = condicionEspecial

    @property
    def condicionEspecial(self):
        return self.__condicionEspecial
    @condicionEspecial.setter
    def condicionEspecial(self, condicionEspecial: str):
        self.__condicionEspecial = condicionEspecial

    def toDict(self):
        data = super().toDict()
        data["condicionEspecial"] = self.condicionEspecial
        return data

    def __str__(self):
        return super().__str__() + f" | Condición especial: {self.__condicionEspecial:<10}"
    
class PacienteUrgencia(Paciente):
    def __init__(self, documento: int, nombre: str, edad: int, estadoDeAtencion: str, nivelDeGravedad: int):
        super().__init__(documento, nombre, edad, estadoDeAtencion)
        self.__nivelDeGravedad = nivelDeGravedad

    @property
    def nivelDeGravedad(self):
        return self.__nivelDeGravedad
    @nivelDeGravedad.setter
    def nivelDeGravedad(self, nivelDeGravedad: int):
        self.__nivelDeGravedad = nivelDeGravedad

    def toDict(self):
        data = super().toDict()
        data["nivelDeGravedad"] = self.nivelDeGravedad
        return data

    def __str__(self):
        return super().__str__() + f" | Nivel de gravedad: {self.__nivelDeGravedad}"