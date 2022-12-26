empleado={
    'Nombre':'Juan',
    'Cedula':104075624,
    'Cargo':"Analista de Datos",
    'Salario':8000000,
    'horas':40,
    'aplicaSubsidio':False,
    'deuda':[15000,30000]
}
# print(empleado)
# print(empleado['Nombre'])
# print(empleado['deuda'][1])

for observadorAtributo,abservadorValor in empleado.items():
    print(observadorAtributo)
    print(abservadorValor)
