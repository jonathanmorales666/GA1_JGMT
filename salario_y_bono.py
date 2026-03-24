# Jonathan Gabriel Morales Torres
# Ejercicio 13: Salario del empleado jonathan :)

salario_base= 3500.00        # Salario mensual en quetzales
bono_productividad =500.00   # Bono mensualn fijo
impuesto = 0.12              # 12% de impuesto sobre el salario total

# Datos del empleado ( variables )
nombre_empleado = "Jonathan Morales"
es_empleado_fijo = True

#Cálculo del salario bruto ( salario base + bono )
salario_bruto = salario_base + bono_productividad

#Cálculo del descuento por impuestos
descuento = salario_bruto * impuesto

# Cálculo del salario neto
salario_neto = salario_bruto - descuento

# Mostrar información
print("Nombre del empleado: ", nombre_empleado)
print("¿Empleadp fijo?: ", es_empleado_fijo)
print("Salario base:", salario_base)
print("Bono de productividad:", bono_productividad)
print("Salario bruto:", salario_bruto)
print("Descuento por impuesto:", descuento)
print("Salario neto:", salario_neto)