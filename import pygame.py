import pygame

# Iniciar
pygame.init()

# Dimensões
width = 720
height = 1280
screen = pygame.display.set_mode((width, height))

# Colors
white = (255, 255, 255)
light_gray = (10,12,13)
dark_gray = (80, 80, 80)

# Propriedades caixa
box_x = 20
box_y = 100
box_width = 680
box_height = 50
box_color = light_gray
opacity = 0.7

# Arredondamento da caixa
border_radius = 15  
shadow_offset = 5
shadow_color = dark_gray

# Propriedades do texto
font_size = 48
font = pygame.font.Font(None, font_size)  # Use default font
text_color = dark_gray
heading_text = "Simple Box"
content_text = "This is a simple box created with Pygame.  It has rounded corners and a subtle shadow."

# Carregar as propriedades
heading_surface = font.render(heading_text, True, text_color)
heading_rect = heading_surface.get_rect(center=(width // 2, box_y + 50))

# Propriedade dos conteudos da caixa
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
    pygame.draw.rect(screen, box_color, box_rect, border_radius=border_radius,)

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
