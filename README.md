# Ejercicio XML
[LM] - Proyecto 2ª evaluación

## Enunciado
El archivo [cursos.xml](cursos.xml) contiene información de los cursos que se ofrecen en Alcobendas. Se crearán los ejercicios correspondientes a la siguiente lista:

* Listar el nombre, tema y fecha inicio de todos los cursos.
* ¿Cuántos cursos tienen un tema dado y es para un perfil concreto?
* Mostrar los cursos con sus fechas de inicio y fin que empiezen en el mes dado.
* Mostrar la url del mapa de los cursos que tenga el tema dado.
* Mostrar todos los tipos, subtipos y subsubtipos posibles junto a la cantidad de cursos que tiene cada tipo.

## Árbol del XML

```
cursos
 ├── curso [01]
 │	 ├── nombre
 │	 ├── subnombre
 │	 ├── temas
 │	 │	 ├── tema [01]
 │	 │	 └── tema [02]
 │	 ├── subtemas
 │	 │	 ├── subtema [01]
 │	 │	 └── subtema [02]
 │	 ├── tipos
 │	 │	 ├── tipo [01]
 │	 │	 └── tipo [02]
 │	 ├── subtipos
 │	 │	 ├── subtipo [01]
 │	 │	 ├── subtipo [02]
 │	 │	 │	.
 │	 │	 │	.
 │	 │	 └── subtipo [n]
 │	 ├── subsubtipos
 │	 ├── perfiles
 │	 │	 ├── perfil [01]
 │	 │	 └── perfil [02]
 │	 ├── fecha inicio
 │	 ├── fecha fin
 │	 ├── hora inicio
 │	 ├── hora fin
 │	 ├── distrito
 │	 ├── ficha
 │	 ├── equipamientos
 │	 │	  └── equipamiento
 │	 │	 	 	├── url [01]
 │	 │			├── coordenada [01]
 │	 │	 		│	.
 │	 │	 		│	.
 │	 │	 		└── coordenada [n]
 │	 ├── fechainscrempadronados 
 │	 ├── fechainscrempleados
 │	 ├── fechainscrgeneral 
 │	 └── tematicas 
 │	 	 ├── tematica [01]
 │	 	 │	.
 │	 	 │	.
 │	 	 └── tematica [n]
 │
 ├── curso [02]
 │	.
 │	.
 └── curso [n]
```
