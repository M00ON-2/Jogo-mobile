import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Colors
white = (255, 255, 255)
light_gray = (220, 220, 220)
dark_gray = (80, 80, 80)

# Box properties
box_x = 100
box_y = 100
box_width = 600
box_height = 400
box_color = light_gray
border_radius = 15  # Rounded corners
shadow_offset = 5
shadow_color = dark_gray

# Text properties
font_size = 48
font = pygame.font.Font(None, font_size)  # Use default font
text_color = dark_gray
heading_text = "Simple Box"
content_text = "This is a simple box created with Pygame.  It has rounded corners and a subtle shadow."

# Render text
heading_surface = font.render(heading_text, True, text_color)
heading_rect = heading_surface.get_rect(center=(width // 2, box_y + 50))

# Content text properties
content_font_size = 24
content_font = pygame.font.Font(None, content_font_size)
content_color = dark_gray
content_lines = []
max_line_width = box_width - 40  # Margin inside the box

def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        test_width, _ = font.size(test_line)
        if test_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)
    return lines

content_lines = wrap_text(content_text, content_font, max_line_width)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Draw shadow
    shadow_rect = pygame.Rect(box_x + shadow_offset, box_y + shadow_offset, box_width, box_height)
    pygame.draw.rect(screen, shadow_color, shadow_rect, border_radius=border_radius)

    # Draw the box
    box_rect = pygame.Rect(box_x, box_y, box_width, box_height)
    pygame.draw.rect(screen, box_color, box_rect, border_radius=border_radius)

    # Draw heading
    screen.blit(heading_surface, heading_rect)

    # Draw content
    y_offset = heading_rect.bottom + 20
    for line in content_lines:
        line_surface = content_font.render(line, True, content_color)
        line_rect = line_surface.get_rect(center=(width // 2, y_offset))
        screen.blit(line_surface, line_rect)
        y_offset += content_font_size + 5  # Add spacing between lines

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()


##class Caixa:
 #   def __init__(self, largura=None, altura=None, cor=None, texto=None, arredondamento=None, x=None, y=None):
  #      self.largura = largura
   #     self.altura = altura
    #    self.cor = cor
     #   self.texto = texto
      #  self.arredondamento = arredondamento
       # self.x = x
        # self.y = y

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# ...