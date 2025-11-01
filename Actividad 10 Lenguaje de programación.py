from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo,_precio_base):
        self._marca = marca
        self._modelo = modelo
        self._precio_base = max(1,_precio_base)
        if _precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero.")


    @abstractmethod
    def impuesto(self):
        pass
    def precio_final(self):
        return self._precio_base + self.impuesto()

    def ficha(self):
        return f"{self._marca} {self._modelo} ($ {self._precio_base:.2f})"

    def __str__(self):
        return f"{self.ficha()} | Precio final: $ {self.precio_final():.2f}"
    
class Carro(Vehiculo):
    def __init__(self, marca, modelo, precio_base, num_puertas):
        super().__init__(marca, modelo, precio_base)
        self.num_puertas = num_puertas

    def impuesto(self):
        imp= self._precio_base * 0.08  # 8% de impuesto
        desc= self._precio_base * 0.01 if self.num_puertas ==5 else 0
        return imp - desc  # impuesto final para el automóvil
    def ficha(self):
        if self.num_puertas ==1:
            return f"Carro | {super().ficha()} | {self.num_puertas} puerta"
        return f"Carro | {super().ficha()} | {self.num_puertas} puertas"
    
class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio_base, cc):
        super().__init__(marca, modelo, precio_base)
        self.cc = cc

    def impuesto(self):
        return self._precio_base * 0.10  # 10% de impuesto
    
if __name__ == "__main__":
    inventario = [
        Carro("Toyota", "Corolla", 20000, 4),
        Carro("Honda", "Civic", 22000, 5),
        Moto("Yamaha", "YZF-R3", 5000, 321),
        Moto("Kawasaki", "Ninja 250", 4500, 249)
    ]

    total = 0.0
    for v in inventario:
        print(v)
        total += v.precio_final()

    print(f"Precio total del inventario: $ {total:.2f}")