# ACTIVIDAD DE APRENDIZAJE 3: ESTRUCTURAS DE CONTROL CONDICIONALES EN PYTHON

## 📋 Descripción
Esta actividad está diseñada para enseñar y practicar el uso de estructuras de control condicionales en Python, cumpliendo con los requerimientos técnicos establecidos.

## 🎯 Objetivos de Aprendizaje
- Comprender el uso de estructuras `if`, `elif`, `else`
- Aplicar operadores de comparación y lógicos
- Desarrollar lógica condicional en aplicaciones prácticas
- Implementar validaciones y toma de decisiones en código

## 📁 Archivos de la Actividad

### 1. `src/actividad_3_condicionales.py`
**Archivo principal de la actividad**
- Contiene ejemplos teóricos con explicaciones
- Incluye 3 ejercicios prácticos principales
- Interfaz gráfica interactiva usando Flet
- Desafío final para práctica avanzada

### 2. `src/ejercicios_condicionales.py`
**Ejercicios adicionales de práctica**
- 10 ejercicios adicionales con diferentes niveles de dificultad
- Cada ejercicio incluye documentación y casos de prueba
- Función para ejecutar todas las pruebas automáticamente

## 🚀 Cómo Ejecutar la Actividad

### Opción 1: Interfaz Gráfica (Recomendada)
```bash
# Navegar al directorio del proyecto
cd app_excel

# Ejecutar la actividad principal
python src/actividad_3_condicionales.py
```

### Opción 2: Ejercicios en Consola
```bash
# Ejecutar los ejercicios adicionales
python src/ejercicios_condicionales.py
```

### Opción 3: Integrar con la Aplicación Principal
Para integrar la actividad con tu aplicación principal, modifica `src/main.py`:

```python
from actividad_3_condicionales import mostrar_actividad_condicionales

# Agregar un botón en el menú
ft.FilledButton("Actividad 3", on_click=lambda _: mostrar_actividad_condicionales())
```

## 📚 Contenido de la Actividad

### Conceptos Teóricos Cubiertos
1. **Estructura básica if-elif-else**
   - Sintaxis correcta
   - Indentación en Python
   - Flujo de ejecución

2. **Operadores de Comparación**
   - `==` (igual a)
   - `!=` (diferente de)
   - `<`, `>`, `<=`, `>=` (comparaciones numéricas)

3. **Operadores Lógicos**
   - `and` (conjunción)
   - `or` (disyunción)
   - `not` (negación)

### Ejercicios Principales

#### Ejercicio 1: Sistema de Calificaciones
```python
def ejercicio_calificacion(nota):
    if nota >= 90:
        return "Excelente (A)"
    elif nota >= 80:
        return "Muy Bueno (B)"
    # ... más condiciones
```

#### Ejercicio 2: Validación para Conducir
```python
def ejercicio_edad_conduccion(edad, licencia=False):
    if edad < 16:
        return "Demasiado joven para conducir"
    elif edad < 18:
        return "Puede obtener permiso de aprendiz"
    # ... más condiciones
```

#### Ejercicio 3: Calculadora Simple
```python
def ejercicio_calculadora(operacion, num1, num2):
    if operacion == "+":
        return f"{num1} + {num2} = {num1 + num2}"
    elif operacion == "/":
        if num2 != 0:  # Condición anidada
            return f"{num1} / {num2} = {num1 / num2:.2f}"
        else:
            return "Error: División por cero"
    # ... más operaciones
```

### Ejercicios Adicionales
1. **Par o Impar** - Determinar si un número es par o impar
2. **Mayor, Menor o Igual** - Comparar dos números
3. **Estación del Año** - Determinar estación según el mes
4. **Seguridad de Contraseña** - Evaluar fortaleza de contraseñas
5. **Categoría de Edad** - Clasificar edades para diferentes actividades
6. **Clima y Temperatura** - Dar recomendaciones según temperatura
7. **Saludo por Hora** - Saludos apropiados según la hora
8. **Número de Dígitos** - Contar dígitos de un número
9. **Día de la Semana** - Convertir número a nombre del día
10. **Derecho a Votar** - Verificar elegibilidad para votar

## 🎯 Desafío Final
Crear una función que determine el tipo de triángulo basado en sus lados:
- **Equilátero**: Todos los lados iguales
- **Isósceles**: Dos lados iguales
- **Escaleno**: Todos los lados diferentes
- **Validación**: Verificar que los lados formen un triángulo válido

## ✅ Requerimientos Técnicos Cumplidos

### 1. Uso Correcto de Indentación
- Todas las estructuras condicionales siguen las reglas de indentación de Python
- Uso consistente de 4 espacios por nivel

### 2. Implementación de Condiciones Simples y Anidadas
- Condiciones básicas con `if-elif-else`
- Condiciones anidadas (if dentro de if)
- Uso de operadores lógicos para condiciones complejas

### 3. Manejo de Casos Especiales
- Validación de entrada de datos
- Manejo de casos límite (división por cero, edades extremas)
- Valores por defecto en parámetros

### 4. Documentación Clara
- Docstrings en todas las funciones
- Comentarios explicativos en código complejo
- Ejemplos de uso y casos de prueba

## 🔧 Personalización y Extensión

### Agregar Nuevos Ejercicios
Para agregar más ejercicios, puedes:

1. **Crear nuevas funciones** en `ejercicios_condicionales.py`
2. **Seguir el patrón** de documentación establecido
3. **Agregar casos de prueba** en la función `ejecutar_pruebas()`

### Modificar la Interfaz
La interfaz gráfica se puede personalizar modificando:
- Colores y estilos en `actividad_3_condicionales.py`
- Agregar más botones o secciones
- Incluir animaciones o efectos visuales

## 📊 Evaluación y Autoevaluación

### Criterios de Evaluación
- ✅ Uso correcto de sintaxis de estructuras condicionales
- ✅ Implementación de lógica condicional apropiada
- ✅ Manejo de casos especiales y validaciones
- ✅ Documentación clara del código
- ✅ Resolución correcta de los ejercicios propuestos

### Autoevaluación
1. Ejecuta todos los ejercicios y verifica los resultados
2. Intenta modificar las condiciones y predecir los resultados
3. Crea tus propios ejercicios siguiendo los patrones establecidos
4. Practica con el desafío final y extiéndelo

## 🆘 Solución de Problemas

### Error Común: Indentación
```python
# ❌ Incorrecto
if condicion:
print("Esto causará error")

# ✅ Correcto
if condicion:
    print("Esto funciona correctamente")
```

### Error Común: Comparaciones
```python
# ❌ Incorrecto
if edad = 18:  # Asignación en lugar de comparación

# ✅ Correcto
if edad == 18:  # Comparación correcta
```

## 📞 Soporte
Si tienes dudas sobre la actividad o encuentras problemas:
1. Revisa la documentación en los archivos
2. Ejecuta las pruebas para verificar el funcionamiento
3. Consulta la documentación oficial de Python sobre estructuras condicionales

---

**¡Disfruta aprendiendo estructuras de control condicionales en Python! 🐍✨** 