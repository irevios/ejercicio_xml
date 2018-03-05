from lxml import etree
from funciones import menu

arbol = etree.parse( 'cursos.xml' )
menu( arbol )