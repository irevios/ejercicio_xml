from lxml import etree
arbol = etree.parse('cursos.xml')

def listar_nomb_tema_fechaini( arbol ):
	lista = []
	nombres = arbol.xpath( '//curso/nombre/text()' )
	for i in nombres:
		temas = arbol.xpath( '//curso[nombre="'+i+'"]/temas/tema/text()' )
		fechaini = arbol.xpath( '//curso[nombre="'+i+'"]/fechainicio/text()' )[0]
		curso = ( i.split( '\n\t\t\t' )[1].split( '\n' )[0], temas, fechaini )
		lista.append( curso )
	
	return lista

def curso_por_tema_perfil(tema,perfil,arbol):
	cursos = arbol.xpath('//curso[temas/tema="'+tema+'" and perfiles/perfil="'+perfil+'"]')
	return len(cursos)

def fecha_por_mes(mes,arbol):
	lista = []
	nombres = arbol.xpath('//curso/nombre/text()')
	for i in nombres:
		fechaini = arbol.xpath( '//curso[nombre="'+i+'"]/fechainicio/text()' )[0]
		m = fechaini.split('/')[1]
		if int(m) == mes:
			curso = (i.split( '\n\t\t\t' )[1].split( '\n' )[0],fechaini)
			lista.append(curso)
	return lista

print(fecha_por_mes(10,arbol))