def main():
    pass


if __name__ == '__main__':
    main()

    import pygame
    import sys

    # Initialize pygame
    pygame.init()

    # Set the dimensions of the window
    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))

    # Set the title of the window
    pygame.display.set_caption('Loading Screen Example')

    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (100, 100, 100)

    # Load custom font
    try:
        font = pygame.font.Font("Arial.ttf", 74)  # Replace "Arial.ttf" with the path to your font
        button_font = pygame.font.Font("Arial.ttf", 36)  # Replace "Arial.ttf" with the path to your font
    except FileNotFoundError:
        font = pygame.font.SysFont(None, 74)  # Fallback to system default font
        button_font = pygame.font.SysFont(None, 36)  # Fallback to system default font

    # Define button dimensions
    button_width = 200
    button_height = 70
    button_x = (window_width - button_width) // 2
    button_y = (window_height // 2) + 50


    def fade_in(surface, target_alpha, increment=5):
        alpha = surface.get_alpha() or 0
        new_alpha = min(alpha + increment, target_alpha)
        surface.set_alpha(new_alpha)
        return new_alpha == target_alpha


    def render_main_screen():
        title_text = font.render('Universal Studios', True, white)
        title_text.set_alpha(0)
        title_rect = title_text.get_rect(center=(window_width // 2, window_height // 3))

        button_surface = pygame.Surface((button_width, button_height))
        button_surface.fill(white)
        button_surface.set_alpha(0)
        button_text = button_font.render('test', True, black)
        button_text_rect = button_text.get_rect(center=(button_width // 2, button_height // 2))

        return title_text, title_rect, button_surface, button_text, button_text_rect


    def render_slot_screen():
        slots = []
        slot_width = 300
        slot_height = 100
        slot_padding = 20
        starting_y = (window_height - (slot_height * 3 + slot_padding * 2)) // 2

        for i in range(3):
            slot_rect = pygame.Rect((window_width - slot_width) // 2, starting_y + i * (slot_height + slot_padding),
                                    slot_width, slot_height)
            slots.append(slot_rect)

        return slots


    def main():
        running = True
        in_main_screen = True

        title_text, title_rect, button_surface, button_text, button_text_rect = render_main_screen()
        slots = render_slot_screen()

        while running:
            window.fill(black)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if in_main_screen:
                        if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                            in_main_screen = False  # Switch to slot screen

            if in_main_screen:
                # Fade in text and button
                fade_in(title_text, 255)
                if fade_in(button_surface, 255):
                    window.blit(button_surface, (button_x, button_y))
                    window.blit(button_text, (button_x + (button_width - button_text_rect.width) // 2,
                                              button_y + (button_height - button_text_rect.height) // 2))

                # Display "Universal Studios" text
                window.blit(title_text, title_rect)
            else:
                # Slot screen
                for slot_rect in slots:
                    pygame.draw.rect(window, gray, slot_rect)
                    slot_text = button_font.render("Slot", True, white)
                    slot_text_rect = slot_text.get_rect(center=slot_rect.center)
                    window.blit(slot_text, slot_text_rect)

            pygame.display.flip()
            pygame.time.delay(50)  # Delay for smoother animation

        pygame.quit()
        sys.exit()


    if __name__ == '__main__':
        main()

