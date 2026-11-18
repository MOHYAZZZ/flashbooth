import os, glob, random, shutil, time, pygame
os.environ.setdefault("SDL_VIDEODRIVER", "kmsdrm")
ROTATION = -90   # same as your other files

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
sw, sh = screen.get_size()
w, h = (sh, sw) if ROTATION in (90, -90) else (sw, sh)
canvas = pygame.Surface((w, h))
big = pygame.font.Font(None, min(w, h))
small = pygame.font.Font(None, 40)

os.makedirs("captures", exist_ok=True)
samples = glob.glob("samples/*.jpg")

def present():
    screen.blit(pygame.transform.rotate(canvas, ROTATION), (0, 0))
    pygame.display.flip()

def show_text(text, font, bg=(0, 0, 0), fg=(255, 255, 255)):
    canvas.fill(bg)
    img = font.render(text, True, fg)
    canvas.blit(img, img.get_rect(center=(w // 2, h // 2)))
    present()

def show_photo(path):
    photo = pygame.image.load(path).convert()
    pw, ph = photo.get_size()
    s = min(w / pw, h / ph)
    img = pygame.transform.smoothscale(photo, (int(pw * s), int(ph * s)))
    canvas.fill((0, 0, 0))
    canvas.blit(img, img.get_rect(center=(w // 2, h // 2)))
    present()

while True:
    show_text("Press the button!", small)
    if input("Enter = take photo, q = quit: ").strip().lower() == "q":
        break
    for n in (3, 2, 1):
        show_text(str(n), big)
        time.sleep(1)
    show_text("", small, bg=(255, 255, 255))   # the "flash"
    time.sleep(0.15)
    dest = time.strftime("captures/%Y%m%d-%H%M%S.jpg")
    shutil.copy(random.choice(samples), dest)  # camera goes here later
    print("Saved", dest)
    show_photo(dest)
    time.sleep(3)

pygame.quit()