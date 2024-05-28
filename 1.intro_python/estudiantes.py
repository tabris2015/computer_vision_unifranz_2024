class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def saludar(self):
        print(f"hola, soy {self.nombre} y tengo {self.edad} años")

    def obtener_promedio(self):
        acum = 0
        for materia, nota in self.notas.items():
            acum += nota
            
        promedio = acum / len(self.notas)
        return promedio
    
est1 = Estudiante("juan", 16, {"MAT": 70, "FIS": 90, "QMC": 100})
est2 = Estudiante("ana", 17, {"MAT": 80, "FIS": 50, "QMC": 90})

print(f"{est1.nombre}: {est1.obtener_promedio()}")
print(f"{est2.nombre}: {est2.obtener_promedio()}")
