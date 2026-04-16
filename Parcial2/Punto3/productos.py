class Producto:
    def __init__(self, id: int, nombre: str, precio: float, cantidad: int):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def toDict(self):
        return {
            "tipo": "Producto",
            "id": self.__id,
            "nombre": self.__nombre,
            "precio": self.__precio,
            "cantidad": self.__cantidad
        }

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre:<20} | Precio: ${self.__precio:>10,.0f} | Stock: {self.__cantidad:>3}"
    
    
class Computador(Producto):
    def __init__(self, id: int, nombre: str, precio: float, cantidad: int, ram: float, procesador: str):
        super().__init__(id, nombre, precio, cantidad)
        self.__ram = ram
        self.__procesador = procesador

    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, ram):
        if not isinstance(ram, (int, float)):
            raise TypeError("La RAM debe ser un número")
        if ram <= 0:
            raise ValueError("La RAM debe ser mayor a 0")
        self.__ram = ram

    @property
    def procesador(self):
        return self.__procesador

    @procesador.setter
    def procesador(self, procesador):
        if not isinstance(procesador, str) or not procesador.strip():
            raise ValueError("El procesador no puede estar vacío")
        self.__procesador = procesador

    def toDict(self):
        data = super().toDict()
        data.update({
            "tipo": "Computador",
            "ram": self.__ram,
            "procesador": self.__procesador
        })
        return data
    
    def __str__(self):
        return super().__str__() + f" | RAM: {self.__ram:<16} | CPU: {self.__procesador}"
    
    
class Celular(Producto):
    def __init__(self, id: int, nombre: str, precio: float, cantidad: int, almacenamiento: float, camaras:int):
        super().__init__(id, nombre, precio, cantidad)
        self.__almacenamiento = almacenamiento
        self.__camaras = camaras

    @property
    def almacenamiento(self):
        return self.__almacenamiento

    @almacenamiento.setter
    def almacenamiento(self, almacenamiento):
        if not isinstance(almacenamiento, (int, float)):
            raise TypeError("El almacenamiento debe ser un número")
        if almacenamiento <= 0:
            raise ValueError("El almacenamiento debe ser mayor a 0")
        self.__almacenamiento = almacenamiento

    @property
    def camaras(self):
        return self.__camaras

    @camaras.setter
    def camaras(self, camaras):
        if not isinstance(camaras, int):
            raise TypeError("El número de cámaras debe ser entero")
        if camaras < 0:
            raise ValueError("El número de cámaras no puede ser negativo")
        self.__camaras = camaras

    def toDict(self):
        data = super().toDict()
        data.update({
            "tipo": "Celular",
            "almacenamiento": self.__almacenamiento,
            "camaras": self.__camaras
        })
        return data

    def __str__(self):
        return super().__str__() + f" | Almacenamiento: {self.__almacenamiento}GB | Cámaras: {self.__camaras}"
    
    
class Accesorio(Producto):
    def __init__(self, id: int, nombre: str, precio: float, cantidad: int, categoria: str):
        super().__init__(id, nombre, precio, cantidad)
        self.__categoria = categoria

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        if not isinstance(categoria, str) or not categoria.strip():
            raise ValueError("El categoria no puede estar vacío")
        self.__categoria = categoria

    def toDict(self):
        data = super().toDict()
        data.update({
            "tipo": "Accesorio",
            "categoria": self.__categoria
        })
        return data
    
    def __str__(self):
        return super().__str__() + f" | Categoria: {self.__categoria}"