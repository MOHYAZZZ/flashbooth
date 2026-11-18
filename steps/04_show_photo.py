import os, sys, time, pygame
os.environ.setdefault("SDL_VIDEODRIVER", "kmsdrm")
ROTATION = -90   # use whichever worked in 03_countdown.py
PHOTO = sys.argv[1] if len(sys.argv) > 1 else "samples/test.jpg"

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
sw, sh = screen.get_size()
w, h = (sh, sw) if ROTATION in (90, -90) else (sw, sh)
canvas = pygame.Surface((w, h))

photo = pygame.image.load(PHOTO).convert()
pw, ph = photo.get_size()
print(f"Screen {sw}x{sh}, canvas {w}x{h}, photo {pw}x{ph}")

def present():
    screen.blit(pygame.transform.rotate(canvas, ROTATION), (0, 0))
    pygame.display.flip()

def show(scale):
    img = pygame.transform.smoothscale(photo, (int(pw * scale), int(ph * scale)))
    canvas.fill((0, 0, 0))
    canvas.blit(img, img.get_rect(center=(w // 2, h // 2)))
    present()

show(min(w / pw, h / ph))   # fit: whole photo, black bars
time.sleep(5)
show(max(w / pw, h / ph))   # fill: whole screen, edges cropped
time.sleep(5)
pygame.quit()