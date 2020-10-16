def promedio_facultades(info: dict, contando_externos: bool = True) -> tuple:
	def armarCorreo(nombres: str, apellidos: str, documento: int):
		nom = nombres.split()
		ap = apellidos.split()
		documento = str(documento)
		correo = ""
		# Si el estudiante tiene 2 nombres
		if len(nom) == 2:
			# Primera letra del primer nombre
			correo = correo + nom[0][0]
			# Primera letra del segundo nombre
			correo = correo + nom[1][0]
			# (".") un punto
			correo = correo + "."
			# Primer Apellido
			correo = correo + ap[1]
			# Dos ultimos numeros del documento
			correo = correo + documento[-2] + documento[-1]
		else:
			# Si el estudiante tiene 1 nombre
			if len(nom) == 1:
				# Primera letra del primer nombre
				correo = correo + nom[0][0]
				# Primera letra del primer apellido
				correo = correo + ap[1][0]
				# (".") un punto
				correo = correo + "."
				# Segundo Apellido
				correo = correo + ap[0][:-1]
				# Dos ultimos numeros del documento
				correo = correo + documento[-2] + documento[-1]

		# Convertir todas los caracteres del correo a letras minusculas (funcion lower)
		correo = correo.lower()

		# Convertir los caracteres del alfabeto con tilde (á, é, í, ó, ú) a sin tilde
		# y Convertir el caracter (ñ) a (n)
		# (funcion replace)

		letrasChange = [("á", "a"),
						("é", "e"),
						("í", "i"),
						("ó", "o"),
						("ú", "u"),
						("ñ", "n")]

		for valorReemp, valorCam in letrasChange:
			correo = correo.replace(valorReemp, valorCam)

		return correo

	try:
		correos = set()
		for codigoEst in info:
			nombres = info[codigoEst]["nombres"]
			apellidos = info[codigoEst]["apellidos"]
			documento = info[codigoEst]["documento"]
			# Armamos el correo
			correo = armarCorreo(nombres, apellidos, documento)
			# Añadimos el correo al conjunto
			correos.add(correo)
		# Convertimos el conjunto a una lista
		correos = list(correos)
		# Ordenamos la lista alfabeticamente
		correos.sort()
		return correos
	except:
		return "Error numérico."


""" ¿Como Armar los correos electronicos de los estudiantes?
	
	-> Obtener los nombres del estudiante (tipo str)
	-> Obtener los apellidos del estudiante (tipo str)
	-> Obtener el documento del estudiante (tipo int)
	
	-> Separar los dos nombres (Funcion split)
	-> Separar los dos apellidos (Funcion split)
	SPLIT -> ['', '', .....]
	nombres = "Carlos"
	nombres.split -> ['Carlos']
	[pos0, pos1, pos2, .....]
	a = "abdc"
	valora = a[-2] 
	
	-> Convertir el documento del estudiante a String
	
	CONDICIONALES
	-> Si el estudiante tiene dos nombres
		-----------------------------------
		Estructura
		-----------------------------------
		* Primera letra del primer nombre
		* Primera letra del segundo nombre
		* (".") un punto
		* Primer Apellido
		* Dos ultimos numeros del documento
		-----------------------------------
	-> Si el estudiante tiene un nombre
		-----------------------------------
		Estructura
		-----------------------------------
		* Primera letra del primer nombre
		* Primera letra del primer apellido
		* (".") un punto
		* Segundo Apellido
		* Dos ultimos numeros del documento
		-----------------------------------
	
	-> Convertir todas los caracteres del correo a letras minusculas (funcion lower)
	-> Convertir los caracteres del alfabeto con tilde (á, é, í, ó, ú) a sin tilde 
	   y Convertir el caracter (ñ) a (n)
	   (funcion replace)
	
"""
""" Lista de salida de correos
	-> Debe ser una lista
	-> No deben existir correos repetidos (conjunto -> set())
	-> Deben estar ordenados alfabeticamente (funcion sort)
"""
""" 1. No olvidar el Try Except
	2. Como acceder a la información contenida en el diccionario
	3. Validaciones para cada estudiante
		-> Cuando la variable contando-externos (tipo Bool) es True:
			---------------------------------------------------------------
			* Se tienen en cuenta solo las materias que no fueron retiradas
			* No se tiene en cuenta materias con 0 creditos
			---------------------------------------------------------------

		-> Cuando la variable contando-externos (tipo Bool) es False
		--------------------------------------------------------------------------------------
			* Se tienen en cuenta solo las materias que no fueron retiradas
			* No se tiene en cuenta materias con 0 creditos
			--------------------------------------------------------------------------------------
			* Se tienen en cuenta solo las materias que correspondan a el programa del estudiante
			* No se tienen en cuenta los estudiantes cuyo periodo de ingreso sea 'Curso de verano',
			  el cual esta representado como un 05 en el codigo del estudiante
			--------------------------------------------------------------------------------------

		-> Extra
			* No tener en cuenta materias cuyos creditos sean negativos o [< a 0]
			* No tener en cuenta materias cuya nota sea negativa o [< a 0.0]
	
	4. Armar los correos electronicos de los estudiantes
	
		-> Separar los dos nombres (Funcion split)
		-> Separar los dos apellidos (Funcion split)
		
		CONDICIONALES
		-> Si el estudiante tiene dos nombres
			-----------------------------------
			Estructura
			-----------------------------------
			* Primera letra del primer nombre
			* Primera letra del segundo nombre
			* (".") un punto
			* Primer Apellido
			* Dos ultimos numeros del documento
			-----------------------------------
		-> Si el estudiante tiene un nombre
			-----------------------------------
			Estructura
			-----------------------------------
			* Primera letra del primer nombre
			* Primera letra del primer apellido
			* (".") un punto
			* Segundo Apellido
			* Dos ultimos numeros del documento
			-----------------------------------
		
		-> Convertir todas los caracteres del correo a letras minusculas
		-> Convertir los caracteres del alfabeto con tilde (á, é, í, ó, ú) a sin tilde
		-> Convertir el caracter (ñ) a (n)
	
"""
'''
CONSIDERACIONES JULIAN -> Explicaion Extra
CONSIDERACIONES IMPORTANTES PARA LOS CORREOS ELECTRÓNICOS:
* No debe tener duplicados (Hay que guardarlos en un conjunto [set] para evitar duplicados
							, y luego se convierte a una lista [list])
* Debe estar completamente en minúsculas
* No debe tener acentos

EL PROMEDIO DE LA FACULTAD: 
* Debe reportarse redondeado a dos decimales (Usamos la funcion para redondear -> 
											  round(valor, 2))
* No debe considerar las materias retiradas
* Si contando_externos es False, no debe considerar materias electivas ni vacacionales

FORMULA
( Sumatoria [ NotaMateria * CreditosMateria ] ) / ( Sumatoria (CreditosMateria))

Salida??? -> Tupla
( Diccionario con Facultades , Lista con correos )
Diccionario con Facultades {llave : Valor}
-> Llave = Nombre de la facultad -> String
-> Valor = Promedio de notas de la facultad -> Float
'''

# Prueba 1:
print(promedio_facultades({
					20170136837:{
								"nombres" : "Jorge Juan",
								"apellidos" : "Moreno, López",
								"documento" : 88481595,
								"programa": "ARQU",
								"materias" : [
									{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-8218",
												"nota" : 4.49,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-2113",
												"nota" : 2.97,
												"creditos" : 2,
												"retirada" : "Si",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-5048",
												"nota" : 4.26,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20130225137:{
								"nombres" : "Sara Carolina",
								"apellidos" : "Gómez, Fernández",
								"documento" : 58770043,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-7738",
												"nota" : 3.36,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-9115",
												"nota" : 2.62,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-7698",
												"nota" : 1.59,
												"creditos" : 4,
												"retirada" : "Si",
												},
											]
								},
					20110274333:{
								"nombres" : "Carolina Paula",
								"apellidos" : "Ochoa, López",
								"documento" : 82364435,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7972",
												"nota" : 3.15,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20200116062:{
								"nombres" : "Sara Camila",
								"apellidos" : "Martínez, Gómez",
								"documento" : 40079000,
								"programa" : "DIGR",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-9331",
												"nota" : 4.0,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-3530",
												"nota" : 3.4,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-8548",
												"nota" : 3.1,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-9771",
												"nota" : 3.91,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20100379147:{
								"nombres" : "Jorge Juan",
								"apellidos" : "Romero, López",
								"documento" : 39344921,
								"programa" : "DIGR",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-9511",
												"nota" : 2.38,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-6043",
												"nota" : 3.71,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1720",
												"nota" : 2.5,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20200126220:{
								"nombres" : "Sofia",
								"apellidos" : "Cordoba, Romero",
								"documento" : 90333325,
								"programa" : "IQUI",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-4982",
												"nota" : 4.57,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-4982",
												"nota" : 2.8,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-6947",
												"nota" : 2.47,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-2248",
												"nota" : 3.43,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20130271126:{
								"nombres" : "Gabriela",
								"apellidos" : "Alvarez, García",
								"documento" : 72857337,
								"programa" : "ARQU",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-4963",
												"nota" : 3.15,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-2113",
												"nota" : 3.9,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-1221",
												"nota" : 4.37,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20160219974:{
								"nombres" : "Daniela Sara",
								"apellidos" : "Cuellar, Guitiérrez",
								"documento" : 80398132,
								"programa" : "IIND",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-3557",
												"nota" : 3.91,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-5158",
												"nota" : 3.83,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-7543",
												"nota" : 3.41,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20190264705:{
								"nombres" : "Julio Nicolas",
								"apellidos" : "Fernández, Ramírez",
								"documento" : 42697671,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-7888",
												"nota" : 4.68,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20150222512:{
								"nombres" : "Mateo Gabriel",
								"apellidos" : "Niño, Romero",
								"documento" : 12964051,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-3683",
												"nota" : 3.6,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-4014",
												"nota" : 3.15,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-1670",
												"nota" : 4.75,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					}))
# Expected return:
# ({'Arquitectura': 3.81, 'Diseño': 3.58, 'Ingenieria': 3.63, 'Medicina': 3.08}, ['cp.lopez35', 'ds.guitierrez32', 'gg.alvarez37', 'jj.lopez21', 'jj.lopez95', 'jn.ramirez71', 'mg.romero51', 'sc.fernandez43', 'sc.gomez00', 'sr.cordoba25'])

