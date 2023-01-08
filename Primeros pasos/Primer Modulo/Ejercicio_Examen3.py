enero = 300
febrero = 300
marzo = 300
abril = 300
mayo = 300
junio = 300
julio = 500
agosto = 500
septiembre = 500
octubre = 500
noviembre = 700
diciembre = 700

suma = (enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre + noviembre + diciembre)
promedio = suma / 12.

print(f"El sueldo promedio es: ${int(promedio)}")

if promedio < 300:
    print("Sueldo bajo: por debajo de $300 dólares.")
elif promedio > 900:
    print("Sueldo mejor de lo normal: más de $900 dólares.")
else:
    print("Sueldo normal: entre $300 a $900 dólares.")