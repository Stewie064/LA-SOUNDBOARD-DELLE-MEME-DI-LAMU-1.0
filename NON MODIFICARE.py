import pygame

# Inizializza Pygame
pygame.init()

pygame.display.set_caption('LA SOUNDBOARD DELLE MEME DI LAMU')

# Crea una finestra di visualizzazione
display = pygame.display.set_mode((800, 600))

# Carica i suoni
sound1 = pygame.mixer.Sound('sound1.wav')
sound2 = pygame.mixer.Sound('sound2.wav')
sound3 = pygame.mixer.Sound('sound3.wav')
sound4 = pygame.mixer.Sound('sound4.wav')
sound5 = pygame.mixer.Sound('sound5.wav')
sound6 = pygame.mixer.Sound('sound6.wav')
sound7 = pygame.mixer.Sound('sound7.wav')
sound8 = pygame.mixer.Sound('sound8.wav')
sound9 = pygame.mixer.Sound('sound9.wav')
sound10 = pygame.mixer.Sound('sound10.wav')
sound11 = pygame.mixer.Sound ('sound11.wav')
sound12 = pygame.mixer.Sound ('sound12.wav')
sound13 = pygame.mixer.Sound ('sound13.wav')
sound14 = pygame.mixer.Sound ('sound14.wav')
sound15 = pygame.mixer.Sound ('sound15.wav')
sound16 = pygame.mixer.Sound ('sound16.wav')

channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)
channel5 = pygame.mixer.Channel(4)
channel6 = pygame.mixer.Channel(5)
channel7 = pygame.mixer.Channel(6)
channel8 = pygame.mixer.Channel(7)

sounds_playing = False

# Definisci le dimensioni dei quadrati
square_size = (120, 50)

# Definisci le coordinate dei quadrati
square1_pos = (50, 50)
square2_pos = (50, 120)
square3_pos = (50, 190)
square4_pos = (50, 260)
square5_pos = (50, 330)
square6_pos = (160, 50)
square7_pos = (160, 120)
square8_pos = (160, 190)
square9_pos = (160, 260)
square10_pos = (160, 330)
square11_pos = (160, 390)
square12_pos = (50, 390)
square13_pos = (50, 460)
square14_pos = (160, 460)
square15_pos = (160, 520)
square16_pos = (50, 520)

# Definisci il testo dei quadrati
square1_text = 'Vine boom'
square2_text = 'Gabibbo'
square3_text = 'Charles'
square4_text = 'Donkey Kong'
square5_text = 'fart'
square6_text = 'Wide Walk'
square7_text = 'Parola'
square8_text = 'Paperissima'
square9_text = 'CIAO'
square10_text = 'Skibidi Dop'
square11_text = 'Pasticcio'
square12_text = 'Tesoruccio'
square13_text = 'Verstappen'
square14_text = 'Coconut'
square15_text = 'Monella'
square16_text = 'FUORI'

sounds_paused = False

# Carica il font per il testo
font = pygame.font.Font(None, 24)

background_image = pygame.image.load('urusei_yatsura.jpg')
background_image = pygame.transform.scale(background_image, (800, 600))

# Avvia il ciclo di gioco
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Controlla se un quadrato è stato cliccato
            if event.button == 1:
                if pygame.Rect(square1_pos, square_size).collidepoint(event.pos):
                    sound1.play()
                elif pygame.Rect(square2_pos, square_size).collidepoint(event.pos):
                    sound2.play()
                elif pygame.Rect(square3_pos, square_size).collidepoint(event.pos):
                    sound3.play()
                elif pygame.Rect(square4_pos, square_size).collidepoint(event.pos):
                    sound4.play()
                elif pygame.Rect(square5_pos, square_size).collidepoint(event.pos):
                    sound5.play()
                elif pygame.Rect(square6_pos, square_size).collidepoint(event.pos):
                    sound6.play()
                elif pygame.Rect(square7_pos, square_size).collidepoint(event.pos):
                    sound7.play()
                elif pygame.Rect(square8_pos, square_size).collidepoint(event.pos):
                    sound8.play()
                elif pygame.Rect(square9_pos, square_size).collidepoint(event.pos):
                    sound9.play()
                elif pygame.Rect(square10_pos, square_size).collidepoint(event.pos):
                    sound10.play()
                elif pygame.Rect(square11_pos, square_size).collidepoint(event.pos):
                    sound11.play()
                elif pygame.Rect(square12_pos, square_size).collidepoint(event.pos):
                    sound12.play()
                elif pygame.Rect(square13_pos, square_size).collidepoint(event.pos):
                    sound13.play()
                elif pygame.Rect(square14_pos, square_size).collidepoint(event.pos):
                    sound14.play()
                elif pygame.Rect(square15_pos, square_size).collidepoint(event.pos):
                    sound15.play()
                elif pygame.Rect(square16_pos, square_size).collidepoint(event.pos):
                    sound16.play()

        

                

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if sounds_playing:
                    sound1.stop()
                    sound2.stop()
                    sound3.stop()
                    sound4.stop()
                    sound5.stop()
                    sound6.stop()
                    sound7.stop()
                    sound8.stop()
                    sound9.stop()
                    sound10.stop()
                    sound11.stop()
                    sound12.stop()
                    sound13.stop()
                    sound14.stop()
                    sound15.stop()
                    sound16.stop()
                sounds_playing = not sounds_playing

    # Disegna l'immagine di sfondo
    display.blit(background_image, (0, 0))

    # Disegna i quadrati sulla finestra
    pygame.draw.rect(display, (255, 0, 0), (square1_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square2_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square3_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square4_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square5_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square6_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square7_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square8_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square9_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square10_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square11_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square12_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square13_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square14_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square15_pos, square_size))
    pygame.draw.rect(display, (255, 0, 0), (square16_pos, square_size))
   
    # Disegna il testo sui quadrati
    square1_text_surface = font.render(square1_text, True, (255, 255, 255))
    square2_text_surface = font.render(square2_text, True, (255, 255, 255))
    square3_text_surface = font.render(square3_text, True, (255, 255, 255))
    square4_text_surface = font.render(square4_text, True, (255, 255, 255))
    square5_text_surface = font.render(square5_text, True, (255, 255, 255))
    square6_text_surface = font.render(square6_text, True, (255, 255, 255))
    square7_text_surface = font.render(square7_text, True, (255, 255, 255))
    square8_text_surface = font.render(square8_text, True, (255, 255, 255))
    square9_text_surface = font.render(square9_text, True, (255, 255, 255))
    square10_text_surface = font.render(square10_text, True, (255, 255, 255))
    square11_text_surface = font.render(square11_text, True, (255, 255, 255))
    square12_text_surface = font.render(square12_text, True, (255, 255, 255))
    square13_text_surface = font.render(square13_text, True, (255, 255, 255))
    square14_text_surface = font.render(square14_text, True, (255, 255, 255))
    square15_text_surface = font.render(square15_text, True, (255, 255, 255))
    square16_text_surface = font.render(square16_text, True, (255, 255, 255))
    display.blit(square1_text_surface, (square1_pos[0] + 10, square1_pos[1] + 15))
    display.blit(square2_text_surface, (square2_pos[0] + 10, square2_pos[1] + 15))
    display.blit(square3_text_surface, (square3_pos[0] + 10, square3_pos[1] + 15))
    display.blit(square4_text_surface, (square4_pos[0] + 10, square4_pos[1] + 15))
    display.blit(square5_text_surface, (square5_pos[0] + 10, square5_pos[1] + 15))
    display.blit(square6_text_surface, (square6_pos[0] + 10, square6_pos[1] + 15))
    display.blit(square7_text_surface, (square7_pos[0] + 10, square7_pos[1] + 15))
    display.blit(square8_text_surface, (square8_pos[0] + 10, square8_pos[1] + 15))
    display.blit(square9_text_surface, (square9_pos[0] + 10, square9_pos[1] + 15))
    display.blit(square10_text_surface, (square10_pos[0] + 10, square10_pos[1] + 15))
    display.blit(square11_text_surface, (square11_pos[0] + 10, square11_pos[1] + 15))
    display.blit(square12_text_surface, (square12_pos[0] + 10, square12_pos[1] + 15))
    display.blit(square13_text_surface, (square13_pos[0] + 10, square13_pos[1] + 15))
    display.blit(square14_text_surface, (square14_pos[0] + 10, square14_pos[1] + 15))
    display.blit(square15_text_surface, (square15_pos[0] + 10, square15_pos[1] + 15))
    display.blit(square16_text_surface, (square16_pos[0] + 10, square16_pos[1] + 15))

    pygame.display.update()

# Chiudi Pygame
pygame.quit()
