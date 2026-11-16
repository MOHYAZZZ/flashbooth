import os, time, pygame
os.environ.setdefault("SDL_VIDEODRIVER", "kmsdrm")

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
w, h = screen.get_size()
font = pygame.font.Font(None, 48)

for colour in [(255, 0, 0), (0, 255, 0), (0, 0, 255)]:
    screen.fill(colour)
    pygame.display.flip()
    time.sleep(1)

screen.fill((0, 0, 0))
text = font.render(f"Hello! {w}x{h}", True, (255, 255, 255))
screen.blit(text, text.get_rect(center=(w // 2, h // 2)))
pygame.display.flip()
time.sleep(5)
pygame.quit()