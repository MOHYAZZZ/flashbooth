import os, time, pygame
os.environ.setdefault("SDL_VIDEODRIVER", "kmsdrm")

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
w, h = screen.get_size()
big = pygame.font.Font(None, h)      # number as tall as the screen
small = pygame.font.Font(None, 40)

def show(text, font, bg=(0, 0, 0), fg=(255, 255, 255)):
    screen.fill(bg)
    img = font.render(text, True, fg)
    screen.blit(img, img.get_rect(center=(w // 2, h // 2)))
    pygame.display.flip()

for n in (3, 2, 1):
    show(str(n), big)
    time.sleep(1)

show("", small, bg=(255, 255, 255))   # white screen "flash"
time.sleep(0.3)
show("Click! (photo goes here later)", small)
time.sleep(3)
pygame.quit()