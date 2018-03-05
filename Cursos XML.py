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

def tipos_cursos(arbol):
	lista = []
	tipos = arbol.xpath('//tipos/tipo/text()')
	subtipos = arbol.xpath('//subtipos/subtipo/text()')
	subsubtipos = arbol.xpath('//subsubtipos/subsubtipo/text()')
	for tipo in tipos:
		if tipo not in lista:
			lista.append(tipo)

	for subtipo in subtipos:
		if subtipo not in lista:
			lista.append(subtipo)

	for subsubtipo in subsubtipos:
		if subsubtipo not in lista:
			lista.append(subsubtipo)

	return lista

def cantidad_curso_por_tipo(arbol):
	lista = []
	for i in tipos_cursos(arbol):
		cursos = arbol.xpath('//curso[tipos/tipo="'+i+'" or subtipos/subtipo="'+i+'" or subsubtipos/subsubtipo="'+i+'" ]')
		lista.append((i, len(cursos)))
	
	return lista 

print(cantidad_curso_por_tipo(arbol))