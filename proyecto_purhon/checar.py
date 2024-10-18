import pygame
from OpenGL.GL import glGetString, GL_VERSION


# Inicializa Pygame
pygame.init()

# Configura la pantalla con OpenGL
pygame.display.set_mode((640, 480), pygame.OPENGL | pygame.DOUBLEBUF)
 
# Obtiene y muestra la versión de OpenGL
opengl_version = glGetString(GL_VERSION)
print(f"Versión de OpenGL: {opengl_version.decode('utf-8')}")

# Finaliza Pygame
pygame.quit()
