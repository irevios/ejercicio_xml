import os
from lxml import etree

def listar_nomb_tema_fechaini( arbol ) :
	lista = []
	nombres = arbol.xpath( '//curso/nombre/text()' )
	for nombre in nombres :
		temas = arbol.xpath( '//curso[nombre="' + nombre + '"]/temas/tema/text()' )
		fechaini = arbol.xpath( '//curso[nombre="' + nombre + '"]/fechainicio/text()' )[0]
		curso = ( nombre.split( '\n\t\t\t' )[1].split( '\n' )[0], temas, fechaini )
		lista.append( curso )
	
	return lista

def curso_por_tema_perfil( tema, perfil, arbol ) :
	cursos = arbol.xpath( '//curso[temas/tema="' + tema + '" and perfiles/perfil="' + perfil + '"]' )
	return len( cursos )

def fecha_por_mes( mes, arbol ) :
	lista = []
	nombres = arbol.xpath( '//curso/nombre/text()' )
	for nombre in nombres :
		fechaini = arbol.xpath( '//curso[nombre="' + nombre + '"]/fechainicio/text()' )[0]
		m = fechaini.split( '/' )[1]
		if int( m ) == mes :
			curso = ( nombre.split( '\n\t\t\t' )[1].split( '\n' )[0], fechaini )
			lista.append( curso )
	
	return lista

def url_mapa( tema, arbol ) :
	lista = []
	nombres = arbol.xpath( '//curso[temas/tema="' + tema + '"]/nombre/text()' )
	for nombre in nombres :
		url = arbol.xpath( '//curso[nombre="' + nombre + '"]/equipamientos/equipamiento/url/text()' )[0].split( '\n' )[1].strip( '\t' )
		if url != '' :
			lista.append(( nombre.split( '\n\t\t\t' )[1].split( '\n' )[0],url ) )
	
	return lista

def tipos_cursos( arbol ) :
	lista = []
	tipos = arbol.xpath( '//tipos/tipo/text()' )
	subtipos = arbol.xpath( '//subtipos/subtipo/text()' )
	subsubtipos = arbol.xpath( '//subsubtipos/subsubtipo/text()' )
	for tipo in tipos :
		lista.append( tipo )

	for subtipo in subtipos :
		lista.append( subtipo )

	for subsubtipo in subsubtipos :
		lista.append( subsubtipo )

	return set( lista )

def cantidad_curso_por_tipo( arbol ) :
	lista = []
	for i in tipos_cursos( arbol ) :
		cursos = arbol.xpath( '//curso[tipos/tipo="' + i + '" or subtipos/subtipo="' + i + '" or subsubtipos/subsubtipo="' + i + '" ]' )
		lista.append( ( i, len( cursos ) ) )
	
	return lista 

def validador_cadena( cadena, arbol, tipo, texto = ' Error. Vuelva a introducirlo: ' ) :
	if tipo == 1 :
		listacadenas = arbol.xpath( '//curso/temas/tema/text()' )
	if tipo == 2 :
		listacadenas = arbol.xpath( '//curso/perfiles/perfil/text()' )
	for i in listacadenas :
		if cadena.upper().replace( 'Á', 'A' ).replace( 'É', 'E' ).replace( 'Í', 'I' ).replace( 'Ó', 'O' ).replace( 'Ú', 'U' ) == i.upper().replace( 'Á', 'A' ).replace( 'É', 'E' ).replace( 'Í', 'I' ).replace( 'Ó', 'O' ).replace( 'Ú', 'U' ) :
			return i
	cadena = input( texto )
	return validador_cadena( cadena, arbol, tipo, texto )

def validador_mes( mes, arbol ) :
	if mes.isdecimal() :
		if int( mes ) >= 1 and int( mes ) <= 12:
			return int( mes )
	if mes.isalpha() :
		meses=[ 'ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE' ]		
		for i in range( len( meses ) ) :
			if mes.upper() == meses[i] :
				return i + 1
	mes = input( ' Mes Incorrecto\n Mes: ' )
	return validador_mes( mes,arbol )


def menu( arbol ) :
	opcion = 0
	while ( opcion != 6) :
		os.system( 'clear' )
		print( ' CURSOS EN ARCHIVO XML\n {}\n 1 - Listar Cursos\n 2 - Cantidad de cursos por tema y perfil\n 3 - Buscar curso por mes de inicio\n 4 - URL Mapa del curso por tema\n 5 - Cantidad de cursos por tipos\n 6 - Salir'.format( '=' * 21 ) )
		opcion = int( input( ' Opción: ' ) )
		if opcion == 1 :
			for i in listar_nomb_tema_fechaini( arbol ) :
				print( ' Nombre: {}\n Temas: {}\n Fecha Inicio: {}\n'.format( i[0], i[1], i[2]) )
		if opcion == 2 :
			tema = validador_cadena( input( ' Tema: ' ), arbol, 1, ' Tema Incorrecto.\n Tema: ' )
			perfil = validador_cadena( input( ' Perfil: ' ), arbol, 2, ' Perfil Incorrecto.\n Perfil: ' )
			print( ' Cursos con el tema "{}" y el perfil "{}": {}'.format( tema, perfil, curso_por_tema_perfil( tema, perfil, arbol ) ) )
		
		if opcion == 3 :
			mes = validador_mes( input( ' Mes de Inicio: ' ), arbol )
			for i in fecha_por_mes( mes, arbol ) :
				print( ' Nombre: {}\n Fecha Inicio: {}\n'.format( i[0], i[1] ) )

		if opcion == 4 :
			tema = validador_cadena( input( ' Tema: ' ), arbol, 1, ' Tema Incorrecto.\n Tema: ' )
			for i in url_mapa( tema,arbol ) :
				print( ' Nombre: {}\n URL: {}\n'.format( i[0], i[1] ) )
		if opcion == 5 :
			for i in cantidad_curso_por_tipo( arbol ) :
				print( ' Tipo: {}\n Cantidad de Cursos: {}\n'.format( i[0], i[1] ) )
		
		input( '\n Pulse cualquier tecla para continuar.' )

arbol = etree.parse( 'cursos.xml' )
menu( arbol )
