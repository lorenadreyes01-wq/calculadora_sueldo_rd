# Calculadora de Sueldo Neto - República Dominicana

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una **calculadora de sueldo neto** utilizando Python.
El programa permite calcular el salario final de un empleado tomando en cuenta diferentes descuentos y beneficios aplicados al sueldo bruto.

Entre los elementos considerados en el cálculo se encuentran:

* Descuento por **Seguridad Social (TSS)**
* **Impuesto Sobre la Renta (ISR)**
* **Bonificación**
* **Otros descuentos**
* **Doble sueldo (si aplica)**

El objetivo es aplicar conceptos de programación mientras se utilizan valores reales del sistema laboral de la República Dominicana.

---

# Objetivo del Ejercicio

El objetivo de este ejercicio es que los estudiantes investiguen y apliquen conceptos de programación en Python para realizar el cálculo de un sueldo neto, considerando descuentos por seguridad social, retención del impuesto sobre la renta y bonificación.

Además, los estudiantes deben investigar los valores actuales de estos porcentajes según la normativa vigente en República Dominicana para realizar los cálculos correctamente.

Este ejercicio permite reforzar conocimientos como:

* Variables
* Constantes
* Operadores matemáticos
* Condicionales
* Funciones
* Entrada de datos del usuario

---

# Descripción del Problema

Un empleado tiene un **sueldo bruto mensual** al cual se le aplican varios descuentos y beneficios para calcular el **sueldo neto final**.

Los elementos considerados en el programa son:

### Seguridad Social (TSS)

Es un porcentaje del sueldo bruto que se descuenta para el sistema de seguridad social.

Para este proyecto se utiliza el valor:

**5.91% del sueldo bruto**

---

### Impuesto Sobre la Renta (ISR)

El ISR se calcula según los tramos salariales establecidos en la República Dominicana.

Escala mensual utilizada en el programa:

| Rango salarial        | Impuesto                        |
| --------------------- | ------------------------------- |
| Hasta RD$34,685       | Exento                          |
| RD$34,685 – RD$52,027 | 15% del excedente               |
| RD$52,027 – RD$72,260 | RD$2,601.33 + 20% del excedente |
| Más de RD$72,260      | RD$6,648 + 25% del excedente    |

---

### Bonificación

Algunas empresas otorgan bonificaciones a sus empleados dependiendo del desempeño o de las utilidades de la empresa.

En este proyecto se utiliza una bonificación del:

**10% del sueldo**

(si el usuario indica que aplica).

---

### Otros Descuentos

El programa también permite introducir descuentos adicionales, como por ejemplo:

* préstamos personales
* cooperativas
* seguros adicionales
* adelantos de sueldo
* multas o penalidades

Este valor es introducido manualmente por el usuario.

---

### Doble Sueldo

En República Dominicana es común recibir el **doble sueldo o salario de Navidad**, equivalente a un sueldo adicional.

El programa permite indicar si el doble sueldo aplica ese mes.

---

# Funcionamiento del Programa

El programa realiza los siguientes pasos:

1. Solicita al usuario:

   * nombre del empleado
   * años en la empresa
   * sueldo mensual
   * otros descuentos
   * si aplica bonificación
   * si hay doble sueldo

2. Calcula automáticamente:

   * descuento por seguridad social
   * impuesto sobre la renta (ISR)
   * bonificación (si aplica)
   * doble sueldo (si aplica)

3. Muestra todos los resultados en pantalla junto con el **sueldo neto final**.

---

# Fórmula Utilizada

Sueldo Neto =

Sueldo Bruto

* Seguridad Social
* ISR
* Otros Descuentos

- Bonificación
- Doble Sueldo

---

# Ejemplo de Ejecución

Entrada del usuario:

Nombre: Carlos
Años en la empresa: 3
Sueldo mensual: 60000
Otros descuentos: 2000
¿Aplica bonificación?: si
¿Hay doble sueldo?: no

Salida del programa:

Sueldo Bruto: 60000
Seguridad Social: 3546
ISR: 4200
Otros descuentos: 2000
Bonificación: 6000
Doble sueldo: 0

**Sueldo Neto Final: 56254**

---

# Tecnologías Utilizadas

Este proyecto fue desarrollado utilizando:

* Python
* Poetry para la gestión del entorno
* Git y GitHub para control de versiones

---

# Conclusión

Este proyecto demuestra cómo se pueden aplicar conceptos de programación para resolver problemas reales del ámbito laboral y financiero.

Además, permite comprender cómo funcionan los principales descuentos salariales en la República Dominicana y cómo automatizar estos cálculos mediante programación.
