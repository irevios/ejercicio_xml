from lxml import etree
arbol = etree.parse('cursos.xml')

def listar_nomb_tema_fechaini( arbol ):
	lista = []
	nombres = arbol.xpath( '//curso/nombre/text()' )
	for nombre in nombres:
		temas = arbol.xpath( '//curso[nombre="'+nombre+'"]/temas/tema/text()' )
		fechaini = arbol.xpath( '//curso[nombre="'+nombre+'"]/fechainicio/text()' )[0]
		curso = ( nombre.split( '\n\t\t\t' )[1].split( '\n' )[0], temas, fechaini )
		lista.append( curso )
	
	return lista

def curso_por_tema_perfil(tema,perfil,arbol):
	cursos = arbol.xpath('//curso[temas/tema="'+tema+'" and perfiles/perfil="'+perfil+'"]')
	return len(cursos)

def fecha_por_mes(mes,arbol):
	lista = []
	nombres = arbol.xpath('//curso/nombre/text()')
	for nombre in nombres:
		fechaini = arbol.xpath( '//curso[nombre="'+nombre+'"]/fechainicio/text()' )[0]
		m = fechaini.split('/')[1]
		if int(m) == mes:
			curso = (nombre.split( '\n\t\t\t' )[1].split( '\n' )[0],fechaini)
			lista.append(curso)
	return lista

def url_mapa(tema,arbol):
	lista = []
	nombres = arbol.xpath('//curso[temas/tema="'+tema+'"]/nombre/text()')
	for nombre in nombres:
		url = arbol.xpath('//curso[nombre="'+nombre+'"]/equipamientos/equipamiento/url/text()')[0].split('\n')[1].strip('\t')
		if url != '':
			lista.append((nombre.split( '\n\t\t\t' )[1].split( '\n' )[0],url))
	
	return lista

print(url_mapa('Educación',arbol))