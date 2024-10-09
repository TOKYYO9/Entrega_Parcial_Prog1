# Funcion para cargar un nuevo paciente
def cargarPaciente(numeroPaciente, nombrePaciente, edadPaciente, diagnosticoPaciente, diasPaciente):
    '''
    Comienza creando una lista vacia en la que va a agregando todos los inputs que pedimos previamente.
    Asigna cada valor y nos retorna la lista del nuevo paciente.
    '''
    listaPaciente = []
    listaPaciente.append(numeroPaciente)
    listaPaciente.append(nombrePaciente)
    listaPaciente.append(edadPaciente)
    listaPaciente.append(diagnosticoPaciente)
    listaPaciente.append(diasPaciente)
    return listaPaciente

# Funcion para mostrar todos los pacientes
def mostrarPacientes(pacientes):
    '''
    Recorre la lista pacientes y nos devuelve cada paciente
    '''
    for paciente in pacientes:
        print(paciente)

# Funcion para buscar un paciente por su numero de 'HC'
def buscarPacienteHC(pacienteBuscar):
    '''
    Comienza creando una lista vacia y recorre cada elemento de esta.
    Cuando la posicion '0' es igual a el numero de 'HC' que le indicamos.
    Asigna cada valor y nos retorna la lista del paciente encontrado.
    '''
    pacienteEncontrado = []
    for i in range(len(pacientes)):
        if pacientes[i][0] == pacienteBuscar:
            pacienteEncontrado.append(pacientes[i][0])
            pacienteEncontrado.append(pacientes[i][1])
            pacienteEncontrado.append(pacientes[i][2])
            pacienteEncontrado.append(pacientes[i][3])
            pacienteEncontrado.append(pacientes[i][4])
            return pacienteEncontrado
    print("El paciente no se encontró.")
    return None

# Funcion para buscar el paciente con mas dias de Internacion
def buscarPacienteMasDias(pacientes):

    pacienteMaximo = float('-inf')
    pacienteMasDias = None

    for paciente in pacientes:

        numero = paciente[0]
        nombre = paciente[1]
        edad = paciente[2]
        diagnostico = paciente[3]
        dias = paciente[4]

        if dias > pacienteMaximo:
            pacienteMaximo = dias
            pacienteMasDias = (numero, nombre, edad, diagnostico, dias)
    return pacienteMasDias

#Funcion para buscar el paciente con menos dias de Internacion
def buscarPacienteMenosDias(pacientes):

    pacienteMinimo = float('inf')
    pacienteMenosDias = None

    for paciente in pacientes:

        numero = paciente[0]
        nombre = paciente[1]
        edad = paciente[2]
        diagnostico = paciente[3]
        dias = paciente[4]

        if dias < pacienteMinimo:
            pacienteMinimo = dias
            pacienteMenosDias = (numero, nombre, edad, diagnostico, dias)
    return pacienteMenosDias

# Funcion que ordena la lista de pacientes de forma 'Ascendente' segun su numero de 'HC' (Utilizando 'Bubble Sort')
def ordenarPacientesHC(arreglo):
    n = len(arreglo)

    for i in range(n-1):
        for j in range(n-1-i):
            if arreglo[j][0] > arreglo[j+1][0]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

    for paciente in arreglo:
        print(paciente)

    return arreglo

# Funcion que busca los pacientes los cuales sus dias de Internacion son mayores a cinco.
def pacientesMayoresCinco(pacientes):
    diasLimite = 5
    pacientesEncontrados = []
    
    for paciente in pacientes:
        numero = paciente[0]
        nombre = paciente[1]
        edad = paciente[2]
        diagnostico = paciente[3]
        dias = paciente[4]
        
        if dias > diasLimite:
            pacientesEncontrados.append((numero, nombre, edad, diagnostico, dias))
    
    return pacientesEncontrados

# Variables
pacientes = []

sumaDias = 0
cantidadPacientes = 0

continuar = "1"

# Codigo
print("Gestor de Pacientes Clinicos de Juan Ignacio")
print("")

while continuar == "1":

    print("Menu Principal")
    print("[1] Cargar Pacientes")
    print("[2] Mostrar todos los Pacientes")
    print("[3] Buscar pacientes por Numero de Historia Clinica")
    print("[4] Ordenar pacientes por numero de Historia Clinica")
    print("[5] Mostrar paciente con mas dias de Internacion")
    print("[6] Mostrar paciente con menos dias de Internacion")
    print("[7] Cantidad de pacientes con mas de cinco dias de Internacion")
    print("[8] Promedio de dias de internacion de todos los pacientes")
    print("[9] Salir")
    respuesta = int(input("Respuesta: "))

    if respuesta == 1:
        numero = int(input("Ingrese el numero de 'HC' del paciente: "))
        nombre = input("Ingrese el nombre del Paciente: ")
        edad = int(input("Ingrese la edad del Paciente: "))
        diagnostico = input("Ingrese el diagnostico del Paciente: ")
        dias = int(input("Ingrese los dias de Internacion del Paciente: "))
        pacienteAgregado = cargarPaciente(numero, nombre, edad, diagnostico, dias)
        pacientes.append(pacienteAgregado)
        print(f"Nuevo paciente cargado: {nombre}")
        sumaDias += dias
        cantidadPacientes += 1
    elif respuesta == 2:
        mostrarPacientes(pacientes)
    elif respuesta == 3:
        pacienteBuscar = int(input("Ingrese el numero de 'HC' del paciente a buscar: "))
        pacienteEncontrado = buscarPacienteHC(pacienteBuscar)
        if pacienteEncontrado:
            print(f"Paciente encontrado: {pacienteEncontrado[1]}")
            print(f"Edad: {pacienteEncontrado[2]}")
            print(f"Diagnostico: {pacienteEncontrado[3]}")
            print(f"Dias de Internacion: {pacienteEncontrado[4]}")
    elif respuesta == 4:
        print("Lista de pacientes ordenada por numero de 'HC':")
        ordenarPacientesHC(pacientes)
    elif respuesta == 5:
        pacienteMasDias = buscarPacienteMasDias(pacientes)
        if pacienteMasDias:
            numero, nombre, edad, diagnostico, dias = pacienteMasDias
            print(f"Paciente con mas de Internacion: {nombre}")
            print(f"Edad: {edad} | Diagnostico: {diagnostico} | Dias: {dias}")
    elif respuesta == 6:
        pacienteMenosDias = buscarPacienteMenosDias(pacientes)
        if pacienteMenosDias:
            numero, nombre, edad, diagnostico, dias = pacienteMenosDias
            print(f"Paciente con menos de Internacion: {nombre}")
            print(f"Edad: {edad} | Diagnostico: {diagnostico} | Dias: {dias}")
    elif respuesta == 7:
        pacientesMayores = pacientesMayoresCinco(pacientes)
        if pacientesMayores:
            print("Se encontraron pacientes con dias de Internacion mayores a cinco.")
            for numero, nombre, edad, diagnostico, dias in pacientesMayores:
                print(f"Numero: {numero} | Nombre: {nombre} | Edad: {edad} | Diagnostico: {diagnostico} | Dias de Internacion: {dias}")
        else:
            print("No se encontraron pacientes con dias de Internacion mayores a cinco.")
    elif respuesta == 8:
        promedioDiasInternacion = (sumaDias / cantidadPacientes)
        print(f"El promedio de dias de Internacion de todos los pacientes es de {round(promedioDiasInternacion, 2)}")
    elif respuesta == 9:
        print("Gracias por usar el Gestor de Pacientes Clinicos de Juan Ignacio.")
        continuar = False
        break

    print("")
    print("[1] Menu Principal")
    print("[2] Salir del Gestor")
    seguir = input("Respuesta: ")
    if seguir == "1":
        continuar = "1"
    elif seguir == "2":
        continuar = False
    else:
        print("No ingresaste una opcion correcta.")