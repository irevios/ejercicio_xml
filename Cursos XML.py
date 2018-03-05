from lxml import etree
arbol = etree.parse('cursos.xml')

def listar_nomb_tema_fechaini( arbol ):
	lista = []
	nombres = arbol.xpath( '//curso/nombre/text()' )
	for i in nombres:
		temas = arbol.xpath( '//curso[nombre="'+i+'"]/temas/tema/text()' )
		fechaini = arbol.xpath( '//curso[nombre="'+i+'"]/fechainicio/text()' )
		i = i.split( '\n\t\t\t' )[1].split( '\n' )[0]
		curso = ( i, temas, fechaini[0] )
		lista.append( curso )
	
	return lista


print(listar_nomb_tema_fechaini(arbol))