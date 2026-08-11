# Pseudocódigo del Taller 10 - Sistema de Gestión Académica

## Descripción
Este documento contiene el pseudocódigo completo para el Taller 10, que implementa un Sistema de Gestión Académica. El sistema permite administrar estudiantes, registrar notas, calcular promedios y generar reportes.

## Estructura del Documento

### 1. Pseudocódigo Principal
- **pseudocodigo-taller10.txt**: Contiene el código completo del sistema
- **diagrama-flujo-principal.txt**: Diagramas de flujo del sistema
- **diagrama-clases.txt**: Diagrama de clases UML
- **estructuras-datos.txt**: Definición detallada de estructuras de datos

## Funcionalidades del Sistema

1. **Registro de Estudiantes**: Permite ingresar nuevos estudiantes al sistema
2. **Consulta de Estudiantes**: Busca y muestra información de un estudiante
3. **Listado de Estudiantes**: Muestra todos los estudiantes registrados
4. **Registro de Notas**: Permite ingresar notas por asignatura
5. **Consulta de Notas**: Muestra las notas de un estudiante
6. **Cálculo de Promedios**: Calcula y muestra los promedios generales
7. **Generación de Reportes**: Crea reportes estadísticos del sistema

## Estructuras de Datos Utilizadas

### Estudiante
- `cedula`: Identificador único
- `nombre`: Nombre completo
- `edad`: Edad del estudiante
- `carrera`: Carrera que cursa

### Notas
- `cedula`: Identificador del estudiante
- `asignatura`: Nombre de la materia
- `parcial1`: Nota del primer parcial (0-20)
- `parcial2`: Nota del segundo parcial (0-20)
- `examen`: Nota del examen final (0-20)

### Reporte
- `totalEstudiantes`: Cantidad total de estudiantes
- `aprobados`: Cantidad de estudiantes aprobados
- `suspensos`: Cantidad de estudiantes en suspenso
- `reprobados`: Cantidad de estudiantes reprobados
- `promedioGeneral`: Promedio de todos los estudiantes

## Algoritmos Principales

### Cálculo de Promedio
promedio = (parcial1 * 0.3) + (parcial2 * 0.3) + (examen * 0.4)

text

### Determinación de Estado
- **Aprobado**: Promedio >= 14
- **Suspenso**: 10 <= Promedio < 14
- **Reprobado**: Promedio < 10

## Ejemplo de Ejecución
================================================
SISTEMA DE GESTIÓN ACADÉMICA - TALLER 10
================================================

Registrar estudiante

Consultar estudiante

Listar estudiantes

Registrar notas

Consultar notas

Calcular promedios

Generar reporte

Salir

Seleccione una opción: 1

================================================
REGISTRO DE NUEVO ESTUDIANTE
================================================

Ingrese la cédula del estudiante: 1234567890
Ingrese el nombre completo: María González
Ingrese la edad: 21
Ingrese la carrera: Ingeniería en Sistemas
✅ Estudiante registrado exitosamente!

text

## Autor
[Nombre del Estudiante]

## Fecha
[Fecha actual]

## Licencia
Este proyecto es parte del curso de Lógica de Programación.