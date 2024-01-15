class MEDICO:
    def __init__(self,nombre,identificacion,especialidad):
        self.nombre=nombre
        self.identificacion=identificacion
        self.especialidad=especialidad
        self.cita_medica=[]
    def __str__(self):
        return (f'nombre: {self.nombre},identificacion: {self.identificacion},especialidad: {self.especialidad},cita medica:{self.cita_medica}')
                        

class PACIENTE:
    def __init__(self,nombre,identificacion,historial_clinico):
        self.nombre=nombre
        self.identificacion=identificacion
        self.historial_clinico=historial_clinico
    def __str__(self):
        return (f'nombre: {self.nombre},identificacion: {self.identificacion},historial clinico: {self.historial_clinico}')
    
class HISTORIAL_CLINICO:
    def __init__(self,peso,talla):
        self.alergias=[]
        self.enfermedades=[]
        self.peso=peso
        self.talla=talla
        
    def __str__(self):
        return (f'alergias: {self.alergias}, enfermedades: {self.enfermedades}, peso:{self.peso}, talla: {self.talla}')
    
class CITA_MEDICA:
    def __init__(self,fecha,hora,paciente,medico):
        self.fecha=fecha
        self.hora=hora
        self.paciente=paciente
        self.medico=medico
        self.estado=True


class HOSPITAL:
    def __init__(self):
        self.medicos=[]
        self.pacientes=[]
        self.citas_medicas=[]
        self.historiales_clinicos=[]
    
    def registrar_medico(self,nombre,identificacion,especialidad,cita_medica):
         while True:
            nombre = input('Digite el nombre del medico ---> ')
            identificacion = int(input('Digite el id del medico ---> '))
            especialidad = input('Digite la especialidad ---> ')
            cita_medica=[]
            medico=MEDICO(nombre,identificacion,especialidad,cita_medica)
            print(f'medico--->{medico}')
            if self.buscar_medico(medico)!=False:
                print('No se puede agregar el medico, id en uso.')
            else:
                self.adicionar_medico(medico)
                print('medico adicionado correctamente.')

            salir = input('Presione cualquier tecla para salir, o ingrese 1 para continuar: ')
            if salir != '1':
                break

    def buscar_medico(self,medico):
        for m in self.medicos:
            if m.identificacion == medico.identificacion:
                return medico
            else:
                return False
    
    def adicionar_medico(self,medico):
        self.medicos.append(medico)

    def crear_historial_clinico(self):
        while True:
            peso = int(input('Digite el peso del paciente ---> '))
            talla = int(input('Digite la talla del paciente ---> '))
            while True:
                alergia=input('Digite la alergia del paciente ---> ')
                self.alergias.append(alergia)
                salir = input('Presione cualquier tecla para salir, o ingrese 1 para agregar otra alergia: ')
                if salir != '1':
                    break 
            historial_clinico=HISTORIAL_CLINICO(peso,talla)
            print(f'historial clinico--->{historial_clinico}')

            salir = input('Presione cualquier tecla para salir, o ingrese 1 para continuar: ')
            if salir != '1':
                return historial_clinico 
    
    def registrar_paciente(self):
         while True:
            nombre = input('Digite el nombre del medico ---> ')
            identificacion = int(input('Digite el id del medico ---> '))
            historial_clinico=self.crear_historial_clinico()
            paciente=PACIENTE(nombre,identificacion,historial_clinico)
            print(f'paciente--->{paciente}')
            if self.buscar_paciente(paciente)!=False:
                print('No se puede agregar el paciente, id en uso.')
            else:
                self.adicionar_paciente(paciente)
                print('paciente adicionado correctamente.')

            salir = input('Presione cualquier tecla para salir, o ingrese 1 para continuar: ')
            if salir != '1':
                break 
    
    def buscar_paciente(self,paciente):
        for p in self.pacientes:
            if p.identificacion == paciente.identificacion:
                return paciente
            else:
                return False
    
    def adicionar_paciente(self,paciente):
        self.pacientes.append(paciente)

    def adicionar_cita_medica(self):
        pass
    