# ejercicio2_roseta.py
from PIL import Image
import math

def bresenham(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Bresenham generalizado, aritmetica entera."""
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    
    while True:
        if 0 <= x < ancho and 0 <= y < alto:
            pixels[x, y] = color
        if x == x1 and y == y1: 
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

def generar_puntos_circulo(cx, cy, radio, n):
    """Calcula las coordenadas de N puntos distribuidos en una circunferencia."""
    puntos = []
    for i in range(n):
        # Ángulo en radianes para cada punto
        angulo = 2 * math.pi * i / n
        # Cálculo trigonométrico de X e Y
        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))
        puntos.append((x, y))
    return puntos

def dibujar_roseta(pixels, puntos, ancho, alto):
    """Conecta todos los puntos entre sí aplicando un gradiente de color."""
    n = len(puntos)

    for i in range(n):
        for j in range(i + 1, n):
            rojo = int((i / n) * 255)
            verde = 100
            azul = int((j / n) * 255)
            color_linea = (rojo, verde, azul)
            
            # Trazamos la línea usando Bresenham
            bresenham(pixels, puntos[i][0], puntos[i][1], puntos[j][0], puntos[j][1], color_linea, ancho, alto)

# Programa principal
if __name__ == "__main__":
    ancho, alto = 700, 700
    
    # Generamos las tres variantes solicitadas (N=12, 24, 36)
    for n in [12, 24, 36]:
        # Fondo negro
        img = Image.new("RGB", (ancho, alto), "black")
        pixels = img.load()
        
        # Generar puntos (Centro en 350,350 y radio de 300)
        puntos = generar_puntos_circulo(350, 350, 300, n)
        
        # Dibujar las conexiones
        dibujar_roseta(pixels, puntos, ancho, alto)
        
        # Guardar cada variante
        nombre_archivo = f"roseta_{n}.png"
        img.save(nombre_archivo)
        print(f"Imagen {nombre_archivo} generada con éxito.")