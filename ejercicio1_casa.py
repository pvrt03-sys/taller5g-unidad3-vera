# ejercicio1_casa.py
from PIL import Image
import math
def dda(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Traza una linea usando el algoritmo DDA."""
    dx = x1 - x0
    dy = y1 - y0
    pasos = max(abs(dx), abs(dy))
    
    if pasos == 0: 
        return
        
    x_inc = dx / pasos
    y_inc = dy / pasos
    
    x, y = x0, y0
    for _ in range(int(pasos) + 1):
        px, py = round(x), round(y)
        if 0 <= px < ancho and 0 <= py < alto:
            pixels[px, py] = color
        x += x_inc
        y += y_inc

def dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Dibuja un rectángulo usando 4 líneas DDA."""
    dda(pixels, x0, y0, x1, y0, color, ancho, alto) # Línea superior
    dda(pixels, x0, y1, x1, y1, color, ancho, alto) # Línea inferior
    dda(pixels, x0, y0, x0, y1, color, ancho, alto) # Línea izquierda
    dda(pixels, x1, y0, x1, y1, color, ancho, alto) # Línea derecha

def dibujar_triangulo(pixels, p1, p2, p3, color, ancho, alto):
    """Dibuja un triángulo conectando 3 puntos con DDA."""
    dda(pixels, p1[0], p1[1], p2[0], p2[1], color, ancho, alto)
    dda(pixels, p2[0], p2[1], p3[0], p3[1], color, ancho, alto)
    dda(pixels, p3[0], p3[1], p1[0], p1[1], color, ancho, alto)

def dibujar_sol(pixels, cx, cy, radio, n_rayos, color, ancho, alto):
    """Dibuja un sol irradiando líneas desde el centro."""
    for i in range(n_rayos):
        angulo = (2 * math.pi * i) / n_rayos
        fin_x = cx + int(radio * math.cos(angulo))
        fin_y = cy + int(radio * math.sin(angulo))
        dda(pixels, cx, cy, fin_x, fin_y, color, ancho, alto)
        
if __name__ == "__main__":
    ancho, alto = 600, 500
    # Lienzo con fondo celeste
    imagen = Image.new("RGB", (ancho, alto), (200, 230, 255))
    pixels = imagen.load()

    
    color_piso = (34, 139, 34)       # Verde
    color_pared = (255, 228, 196)    # Beige
    color_techo = (178, 34, 34)      # Rojo ladrillo
    color_puerta = (139, 69, 19)     # Marrón
    color_ventana = (135, 206, 250)  # Celeste claro
    color_sol = (255, 215, 0)        # Amarillo
    color_marco = (0, 0, 0)          # Negro

   
    dda(pixels, 0, 400, ancho - 1, 400, color_piso, ancho, alto)

 
    dibujar_rectangulo(pixels, 150, 200, 450, 400, color_pared, ancho, alto)

  
    dibujar_triangulo(pixels, (100, 200), (300, 100), (500, 200), color_techo, ancho, alto)

   
    dibujar_rectangulo(pixels, 260, 300, 340, 400, color_puerta, ancho, alto)

  
    dibujar_rectangulo(pixels, 180, 240, 230, 290, color_ventana, ancho, alto) # Ventana izquierda
    dibujar_rectangulo(pixels, 370, 240, 420, 290, color_ventana, ancho, alto) # Ventana derecha

    
    dibujar_sol(pixels, 500, 100, 60, 12, color_sol, ancho, alto)

    imagen.save("casa.png")
    print("Imagen casa.png generada con éxito.")