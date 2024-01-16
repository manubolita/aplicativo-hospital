import pickle
import os
class Persona:
    def __init__(self, nombre, numero_identificacion):
        self.nombre = nombre
        self.numero_identificacion = numero_identificacion

class HistoriaClinica:
    def __init__(self):
        self.alergias = []
        self.enfermedades_actuales = []
        self.medicamentos_recetados = []

class Paciente(Persona):
    pacientes_registrados = set()

    def __init__(self, nombre, numero_identificacion):
        super().__init__(nombre, numero_identificacion)
        if numero_identificacion in Paciente.pacientes_registrados:
            raise ValueError("Ya existe un paciente con ese número de identificación.")
        Paciente.pacientes_registrados.add(numero_identificacion)
        self.historia_clinica = HistoriaClinica()

    def agregar_alergia(self, alergia):
        self.historia_clinica.alergias.append(alergia)

    def agregar_enfermedad_actual(self, enfermedad):
        self.historia_clinica.enfermedades_actuales.append(enfermedad)

    def agregar_medicamento_recetado(self, medicamento):
        self.historia_clinica.medicamentos_recetados.append(medicamento)

    def reservar_servicio(self, servicio):
        self.servicios_reservados.append(servicio)
        print(f"Servicio '{servicio.nombre}' reservado con éxito.")

    def pagar_servicios(self):
        total_a_pagar = sum(servicio.costo for servicio in self.servicios_reservados)
        print(f"Total a pagar: ${total_a_pagar:.2f}")
        self.servicios_reservados = []
        print("Servicios pagados con éxito.")

class Medico(Persona):
    medicos_registrados = set()

    def __init__(self, nombre, numero_identificacion, especialidad):
        super().__init__(nombre, numero_identificacion)
        if numero_identificacion in Medico.medicos_registrados:
            raise ValueError("Ya existe un médico con ese número de identificación.")
        Medico.medicos_registrados.add(numero_identificacion)
        self.especialidad = especialidad
        self.paciente_asignado = None

    def asignar_paciente(self, paciente):
        self.paciente_asignado = paciente

    def reservar_cita_medica(self):
        if self.paciente_asignado:
            print(f"Cita médica reservada para el paciente {self.paciente_asignado.nombre}.")
        else:
            print("No hay paciente asignado. No se puede reservar cita médica.")

    def finalizar_cita_medica(self):
        if self.paciente_asignado:
            print(f"Cita médica finalizada para el paciente {self.paciente_asignado.nombre}.")
            self.paciente_asignado = None
        else:
            print("No hay cita médica en curso.")

class Enfermera(Persona):
    enfermeras_registradas = set()

    def __init__(self, nombre, numero_identificacion, area):
        super().__init__(nombre, numero_identificacion)
        if numero_identificacion in Enfermera.enfermeras_registradas:
            raise ValueError("Ya existe una enfermera con ese número de identificación.")
        Enfermera.enfermeras_registradas.add(numero_identificacion)
        self.area = area
        self.paciente_asignado = None
        
    def asignar_paciente(self, paciente):
        self.paciente_asignado = paciente

    def dejar_libre(self):
        if self.paciente_asignado:
            print(f"Enfermera liberada. El paciente {self.paciente_asignado.nombre} ha sido atendido.")
            self.paciente_asignado = None
        else:
            print("La enfermera ya está libre.")

class Servicio:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

class Hospital:
    def __init__(self):
        self.personas = []
        self.servicios = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def obtener_paciente_por_id(self, id_paciente):
        for persona in self.personas:
            if isinstance(persona, Paciente) and persona.numero_identificacion == id_paciente:
                return persona
        return None

    def obtener_persona_por_id(self, id_persona, tipo_persona):
        for persona in self.personas:
            if isinstance(persona, tipo_persona) and persona.numero_identificacion == id_persona:
                return persona
        return None

    def guardar_informacion(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump({'personas': self.personas, 'servicios': self.servicios}, f)

    def cargar_informacion(self, archivo):
        try:
            with open(archivo, 'rb') as f:
                data = pickle.load(f)
                self.personas = data.get('personas', [])
                self.servicios = data.get('servicios', [])
                print("Información cargada exitosamente.")
        except FileNotFoundError:
            print("Archivo no encontrado. Creando uno nuevo.")
    def mostrar_servicios(self):
        print("\n***** Lista de Servicios *****")
        for servicio in self.servicios:
            print(f"Servicio - Nombre: {servicio.nombre}, Costo: ${servicio.costo:.2f}")

    def mostrar_servicios_pacientes(self):
        print("\n***** Lista de Servicios Reservados por Pacientes *****")
        for persona in self.personas:
            if isinstance(persona, Paciente) and hasattr(persona, 'servicios_reservados') and persona.servicios_reservados:
                print(f"Paciente - Nombre: {persona.nombre}, ID: {persona.numero_identificacion}")
                for servicio in persona.servicios_reservados:
                    print(f"  Servicio Reservado - Nombre: {servicio.nombre}, Costo: ${servicio.costo:.2f}")

    def solicitar_servicio_paciente(self):
        id_paciente = input("Ingrese el número de identificación del paciente: ")
        paciente = self.obtener_paciente_por_id(id_paciente)
        if paciente:
            self.mostrar_servicios()
            nombre_servicio = input("Ingrese el nombre del servicio a reservar: ")
            servicio = next((s for s in self.servicios if s.nombre == nombre_servicio), None)
            if servicio:
                paciente.reservar_servicio(servicio)
                print(f"Servicio '{servicio.nombre}' reservado exitosamente para el paciente {paciente.nombre}.")
            else:
                print("Servicio no encontrado.")
        else:
            print("Paciente no encontrado.")

    def eliminar_servicio(self):
        self.mostrar_servicios()
        nombre_servicio = input("Ingrese el nombre del servicio a eliminar: ")
        servicio = next((s for s in self.servicios if s.nombre == nombre_servicio), None)
        if servicio:
            self.servicios.remove(servicio)
            print(f"Servicio '{servicio.nombre}' eliminado exitosamente.")
        else:
            print("Servicio no encontrado.")
    def guardar_informacion(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump({'personas': self.personas, 'servicios': self.servicios}, f)

    def cargar_informacion(self, archivo):
        try:
            with open(archivo, 'rb') as f:
                data = pickle.load(f)
                self.personas = data.get('personas', [])
                self.servicios = data.get('servicios', [])
                print("Información cargada exitosamente.")
        except FileNotFoundError:
            print("Archivo no encontrado. Creando uno nuevo.")
def menu_servicios(hospital):
    archivo_servicios = 'servicios_data.pkl'

    # Cargar información al inicio del menú de servicios
    hospital.cargar_informacion(archivo_servicios)

    while True:
        
        print("\n***** Menú Servicios *****")
        print("1. Agregar Servicio")
        print("2. Eliminar Servicio")
        print("3. Solicitar Servicio por Paciente")
        print("4. Mostrar Servicios Reservados por Pacientes")
        print("5. Mostrar Lista de Servicios")
        print("6. Guardar y Regresar al Menú Principal")
        print("0. Regresar al Menú Principal")

        opcion = input("Ingrese la opción: ")

        if opcion == "1":
            nombre_servicio = input("Ingrese el nombre del servicio: ")
            costo_servicio = float(input("Ingrese el costo del servicio: "))
            nuevo_servicio = Servicio(nombre_servicio, costo_servicio)
            hospital.agregar_servicio(nuevo_servicio)
            print("Servicio agregado exitosamente.")

        elif opcion == "2":
            hospital.eliminar_servicio()

        elif opcion == "3":
            hospital.solicitar_servicio_paciente()

        elif opcion == "4":
            hospital.mostrar_servicios_pacientes()

        elif opcion == "5":
            hospital.mostrar_servicios()

        elif opcion == "6":
            # Guardar información y salir del menú de servicios
            hospital.guardar_informacion(archivo_servicios)
            print("Información guardada exitosamente. Regresando al Menú Principal.")
            break

        elif opcion == "0":
            # Regresar al Menú Principal sin guardar
            print("Regresando al Menú Principal.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

def menu_medicos_enfermeras(hospital):
    archivo_medicos = 'medicos_data.pkl'

    # Cargar información al inicio del menú de médicos
    hospital.cargar_informacion(archivo_medicos)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n***** Menú Médicos *****")
        print("1. Registrar Médico")
        print("2. Eliminar Médico")
        print("3. Asignar Paciente y Reservar Cita Médica")
        print("4. Finalizar Cita Médica")
        print("5. Asignar Enfermera a Paciente Hospitalizado")
        print("6. Liberar Enfermera")
        print("7. Registrar Enfermera")
        print("8. Eliminar Enfermera")
        print("9. Guardar y Regresar al Menú Principal")
        print("10. mostrar medicos y su disponibilidad")
        print("11. mostrar enfermeras y su disponibilidad")
        print("0. Regresar al Menú Principal")

        opcion = input("Ingrese la opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del médico: ")
            numero_identificacion = input("Ingrese el número de identificación del médico: ")
            especialidad = input("Ingrese la especialidad del médico: ")
            medico = Medico(nombre, numero_identificacion, especialidad)
            hospital.agregar_persona(medico)
            print("Médico registrado exitosamente.")

        elif opcion == "2":
            id_medico = input("Ingrese el número de identificación del médico a eliminar: ")
            medico = hospital.obtener_persona_por_id(id_medico, Medico)
            if medico:
                hospital.personas.remove(medico)
                print("Médico eliminado exitosamente.")
            else:
                print("Médico no encontrado.")

        elif opcion == "3":
            id_medico = input("Ingrese el número de identificación del médico: ")
            medico = hospital.obtener_persona_por_id(id_medico, Medico)
            if medico:
                id_paciente = input("Ingrese el número de identificación del paciente: ")
                paciente = hospital.obtener_paciente_por_id(id_paciente)
                if paciente:
                    medico.asignar_paciente(paciente)
                    medico.reservar_cita_medica()
                    print(f"Paciente asignado al médico {medico.nombre}.")
                else:
                    print("Paciente no encontrado.")
            else:
                print("Médico no encontrado.")

        elif opcion == "4":
            id_medico = input("Ingrese el número de identificación del médico: ")
            medico = hospital.obtener_persona_por_id(id_medico, Medico)
            if medico:
                medico.finalizar_cita_medica()
            else:
                print("Médico no encontrado.")

        elif opcion == "5":
            id_medico = input("Ingrese el número de identificación del médico: ")
            medico = hospital.obtener_persona_por_id(id_medico, Medico)
            if medico:
                id_paciente = input("Ingrese el número de identificación del paciente: ")
                paciente = hospital.obtener_paciente_por_id(id_paciente)
                if paciente:
                    id_enfermera = input("Ingrese el número de identificación de la enfermera: ")
                    enfermera = hospital.obtener_persona_por_id(id_enfermera, Enfermera)
                    if enfermera:
                        enfermera.asignar_paciente(paciente)
                        print(f"Enfermera asignada al paciente {paciente.nombre}.")
                    else:
                        print("Enfermera no encontrada.")
                else:
                    print("Paciente no encontrado.")
            else:
                print("Médico no encontrado.")

        elif opcion == "6":
            id_enfermera = input("Ingrese el número de identificación de la enfermera: ")
            enfermera = hospital.obtener_persona_por_id(id_enfermera, Enfermera)
            if enfermera:
                enfermera.dejar_libre()
            else:
                print("Enfermera no encontrada.")

        elif opcion == "7":
            nombre = input("Ingrese el nombre de la enfermera: ")
            numero_identificacion = input("Ingrese el número de identificación de la enfermera: ")
            area = input("Ingrese el área de la enfermera: ")
            enfermera = Enfermera(nombre, numero_identificacion, area)
            hospital.agregar_persona(enfermera)
            print("Enfermera registrada exitosamente.")

        elif opcion == "8":
            id_enfermera = input("Ingrese el número de identificación de la enfermera a eliminar: ")
            enfermera = hospital.obtener_persona_por_id(id_enfermera, Enfermera)
            if enfermera:
                hospital.personas.remove(enfermera)
                print("Enfermera eliminada exitosamente.")
            else:
                print("Enfermera no encontrada.")

        elif opcion == "9":
            # Guardar información y salir del menú de médicos
            hospital.guardar_informacion(archivo_medicos)
            print("Información guardada exitosamente. Regresando al Menú Principal.")
            break
        elif opcion == "10":
            # Mostrar lista de médicos con pacientes asignados
            print("\n***** Lista de Médicos con Pacientes Asignados *****")
            for persona in hospital.personas:
                if isinstance(persona, Medico):
                    asignado = persona.paciente_asignado.nombre if persona.paciente_asignado else "Ninguno"
                    print(f"Médico - Nombre: {persona.nombre}, ID: {persona.numero_identificacion}, Especialidad: {persona.especialidad}, Paciente Asignado: {asignado}")

        elif opcion == "11":
            # Mostrar lista de enfermeras con pacientes asignados
            print("\n***** Lista de Enfermeras con Pacientes Asignados *****")
            for persona in hospital.personas:
                if isinstance(persona, Enfermera):
                    asignado = persona.paciente_asignado.nombre if persona.paciente_asignado else "Ninguno"
                    print(f"Enfermera - Nombre: {persona.nombre}, ID: {persona.numero_identificacion}, Área: {persona.area}, Paciente Asignado: {asignado}")
        elif opcion == "0":
            # Regresar al Menú Principal sin guardar
            print("Regresando al Menú Principal.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
    
def menu_pacientes(hospital):
    archivo_pacientes = 'pacientes_data.pkl'

    # Cargar información al inicio del menú de pacientes
    hospital.cargar_informacion(archivo_pacientes)

    while True:
        print("\n***** Menú Pacientes *****")
        print("1. Añadir Paciente")
        print("2. Eliminar Paciente")
        print("3. Reservar Servicio")
        print("4. Pagar Servicio")
        print("5. Buscar Paciente por Número de Identificación")
        print("6. modificar historial clinico de un paciente")
        print("7. Guardar y Regresar al Menú Principal")
        print("0. Regresar al Menú Principal")

        opcion = input("Ingrese la opción: ")

        if opcion == "1":
            # Añadir Paciente
            nombre = input("Ingrese el nombre del paciente: ")
            numero_identificacion = input("Ingrese el número de identificación del paciente: ")
            paciente = Paciente(nombre, numero_identificacion)
            
            while True:
                # Submenú para gestionar historia clínica
                print("\n***** Historia Clínica *****")
                print("1. Añadir Alergia")
                print("2. Añadir Enfermedad Actual")
                print("3. Añadir Medicamento Recetado")
                print("0. Finalizar y Regresar")

                opcion_historia = input("Ingrese la opción de la historia clínica: ")

                if opcion_historia == "1":
                    alergia = input("Ingrese la alergia: ")
                    paciente.historia_clinica.alergias.append(alergia)
                    print("Alergia añadida exitosamente.")
                elif opcion_historia == "2":
                    enfermedad = input("Ingrese la enfermedad actual: ")
                    paciente.historia_clinica.enfermedades_actuales.append(enfermedad)
                    print("Enfermedad actual añadida exitosamente.")
                elif opcion_historia == "3":
                    medicamento = input("Ingrese el medicamento recetado: ")
                    paciente.historia_clinica.medicamentos_recetados.append(medicamento)
                    print("Medicamento recetado añadido exitosamente.")
                elif opcion_historia == "0":
                    # Salir del submenú de historia clínica
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")

            # Agregar el paciente al hospital
            hospital.agregar_persona(paciente)
            print("Paciente añadido exitosamente.")

        elif opcion == "2":
            id_paciente = input("Ingrese el número de identificación del paciente a eliminar: ")
            paciente = hospital.obtener_paciente_por_id(id_paciente)
            if paciente:
                hospital.personas.remove(paciente)
                print("Paciente eliminado exitosamente.")
            else:
                print("Paciente no encontrado.")

        elif opcion == "3":
            id_paciente = input("Ingrese el número de identificación del paciente: ")
            paciente = hospital.obtener_paciente_por_id(id_paciente)
            if paciente:
                servicio = input("Ingrese el nombre del servicio a reservar: ")
                paciente.reservar_servicio(servicio)
                print(f"Servicio '{servicio}' reservado exitosamente para el paciente {paciente.nombre}.")
            else:
                print("Paciente no encontrado.")

        elif opcion == "4":
            id_paciente = input("Ingrese el número de identificación del paciente: ")
            paciente = hospital.obtener_paciente_por_id(id_paciente)
            if paciente:
                servicio = input("Ingrese el nombre del servicio a pagar: ")
                paciente.pagar_servicio(servicio)
                print(f"Servicio '{servicio}' pagado exitosamente por el paciente {paciente.nombre}.")
            else:
                print("Paciente no encontrado.")

        elif opcion == "5":
            id_busqueda = input("Ingrese el número de identificación del paciente a buscar: ")
            paciente = hospital.obtener_paciente_por_id(id_busqueda)
            if paciente:
                print(f"Resultado de la búsqueda: Paciente - Nombre: {paciente.nombre}, ID: {paciente.numero_identificacion}")
                # Mostrar historial clínico
                print("\n***** Historial Clínico *****")
                print("Alergias:", ', '.join(paciente.historia_clinica.alergias))
                print("Enfermedades Actuales:", ', '.join(paciente.historia_clinica.enfermedades_actuales))
                print("Medicamentos Recetados:", ', '.join(paciente.historia_clinica.medicamentos_recetados))
            else:
                print("Paciente no encontrado.")
        elif opcion == "6":
            # Modificar Historial Clínico
            id_paciente = input("Ingrese el número de identificación del paciente: ")
            paciente = hospital.obtener_paciente_por_id(id_paciente)
            if paciente:
                while True:
                    # Submenú para modificar historia clínica
                    print("\n***** Modificar Historial Clínico *****")
                    print("1. Añadir Alergia")
                    print("2. Añadir Enfermedad Actual")
                    print("3. Añadir Medicamento Recetado")
                    print("4. Eliminar Alergia")
                    print("5. Eliminar Enfermedad Actual")
                    print("6. Eliminar Medicamento Recetado")
                    print("0. Finalizar y Regresar")

                    opcion_historia = input("Ingrese la opción de la historia clínica a modificar: ")

                    if opcion_historia == "1":
                        alergia = input("Ingrese la alergia: ")
                        paciente.historia_clinica.alergias.append(alergia)
                        print("Alergia añadida exitosamente.")
                    elif opcion_historia == "2":
                        enfermedad = input("Ingrese la enfermedad actual: ")
                        paciente.historia_clinica.enfermedades_actuales.append(enfermedad)
                        print("Enfermedad actual añadida exitosamente.")
                    elif opcion_historia == "3":
                        medicamento = input("Ingrese el medicamento recetado: ")
                        paciente.historia_clinica.medicamentos_recetados.append(medicamento)
                        print("Medicamento recetado añadido exitosamente.")
                    elif opcion_historia == "4":
                        if paciente.historia_clinica.alergias:
                            print("Alergias actuales:", ', '.join(paciente.historia_clinica.alergias))
                            alergia_eliminar = input("Ingrese la alergia a eliminar: ")
                            if alergia_eliminar in paciente.historia_clinica.alergias:
                                paciente.historia_clinica.alergias.remove(alergia_eliminar)
                                print("Alergia eliminada exitosamente.")
                            else:
                                print("La alergia no se encuentra en el historial clínico.")
                        else:
                            print("No hay alergias registradas en el historial clínico.")
                    elif opcion_historia == "5":
                        if paciente.historia_clinica.enfermedades_actuales:
                            print("Enfermedades actuales:", ', '.join(paciente.historia_clinica.enfermedades_actuales))
                            enfermedad_eliminar = input("Ingrese la enfermedad actual a eliminar: ")
                            if enfermedad_eliminar in paciente.historia_clinica.enfermedades_actuales:
                                paciente.historia_clinica.enfermedades_actuales.remove(enfermedad_eliminar)
                                print("Enfermedad actual eliminada exitosamente.")
                            else:
                                print("La enfermedad actual no se encuentra en el historial clínico.")
                        else:
                            print("No hay enfermedades actuales registradas en el historial clínico.")
                    elif opcion_historia == "6":
                        if paciente.historia_clinica.medicamentos_recetados:
                            print("Medicamentos recetados actuales:", ', '.join(paciente.historia_clinica.medicamentos_recetados))
                            medicamento_eliminar = input("Ingrese el medicamento recetado a eliminar: ")
                            if medicamento_eliminar in paciente.historia_clinica.medicamentos_recetados:
                                paciente.historia_clinica.medicamentos_recetados.remove(medicamento_eliminar)
                                print("Medicamento recetado eliminado exitosamente.")
                            else:
                                print("El medicamento recetado no se encuentra en el historial clínico.")
                        else:
                            print("No hay medicamentos recetados registrados en el historial clínico.")
                    elif opcion_historia == "0":
                        # Salir del submenú de modificar historia clínica
                        break
                    else:
                        print("Opción no válida. Intente de nuevo.")
            else:
                print("Paciente no encontrado.")
        elif opcion == "7":
            # Guardar información y salir del menú de pacientes
            hospital.guardar_informacion(archivo_pacientes)
            print("Información guardada exitosamente. Regresando al Menú Principal.")
            break

        elif opcion == "0":
            # Regresar al Menú Principal sin guardar
            print("Regresando al Menú Principal.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

def menu_principal():
    hospital = Hospital()

    archivo_hospital = 'hospital_data.pkl'

    # Cargar información al inicio del programa principal
    hospital.cargar_informacion(archivo_hospital)

    while True:
        print("\n***** Menú Principal *****")
        print("1. Menú Pacientes")
        print("2. Menú Médicos y Enfermeras")
        print("3. Menú Servicios")
        print("4. Ver Personas")
        print("5. Ver Servicios")
        print("6. Guardar y Salir")
        print("0. Salir")

        opcion = input("Ingrese la opción: ")

        if opcion == "1":
            menu_pacientes(hospital)

        elif opcion == "2":
            menu_medicos_enfermeras(hospital)

        elif opcion == "3":
            menu_servicios(hospital)


        elif opcion == "4":
            print("\n***** Lista de Personas *****")
            for persona in hospital.personas:
                if isinstance(persona, Paciente):
                    print(f"Paciente - Nombre: {persona.nombre}, ID: {persona.numero_identificacion}")
                elif isinstance(persona, Medico):
                    print(f"Médico - Nombre: {persona.nombre}, ID: {persona.numero_identificacion}, Especialidad: {persona.especialidad}")
                elif isinstance(persona, Enfermera):
                    print(f"Enfermera - Nombre: {persona.nombre}, ID: {persona.numero_identificacion}, Área: {persona.area}")

        elif opcion == "5":
            print("\n***** Lista de Servicios *****")
            for servicio in hospital.servicios:
                print(f"Servicio - Nombre: {servicio.nombre}, Costo: ${servicio.costo:.2f}")

        elif opcion == "6":
            # Guardar información y salir del programa principal
            hospital.guardar_informacion(archivo_hospital)
            print("Información guardada exitosamente. Saliendo del programa.")
            break

        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    menu_principal()
