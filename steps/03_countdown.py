import os, time, pygame
os.environ.setdefault("SDL_VIDEODRIVER", "kmsdrm")

ROTATION = 180   # 0 = normal, 180 = upside down, 90 or -90 = portrait

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

# Portrait swaps width and height
sw, sh = screen.get_size()
w, h = (sh, sw) if ROTATION in (90, -90) else (sw, sh)
canvas = pygame.Surface((w, h))

big = pygame.font.Font(None, min(w, h))
small = pygame.font.Font(None, 40)

def present():
    """Rotate the canvas and put it on the real screen."""
    screen.blit(pygame.transform.rotate(canvas, ROTATION), (0, 0))
    pygame.display.flip()

def show(text, font, bg=(0, 0, 0), fg=(255, 255, 255)):
    canvas.fill(bg)
    img = font.render(text, True, fg)
    canvas.blit(img, img.get_rect(center=(w // 2, h // 2)))
    present()

for n in (3, 2, 1):
    show(str(n), big)
    time.sleep(1)

show("", small, bg=(255, 255, 255))
time.sleep(0.3)
show("Click!", small)
time.sleep(3)
pygame.quit()