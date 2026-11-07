"""Pixel-art animated banner for the profile README, built from the skull logo.

Usage: python3 tools/make_banner.py banner.gif path/to/final-logo.jpg
"""
import math, random, sys
from PIL import Image

LOGO = sys.argv[2] if len(sys.argv) > 2 else "final-logo.jpg"
OUT = sys.argv[1] if len(sys.argv) > 1 else "banner.gif"
W, H, SCALE, N = 320, 100, 3, 32

# palette (taken from the logo's red + white + black)
BG0 = (10, 4, 7)
BG1 = (22, 7, 12)
BG2 = (38, 10, 17)
MAROON = (64, 14, 24)
MAROON2 = (96, 20, 34)
RED = (209, 42, 60)
RED_HI = (239, 78, 92)
RED_LO = (150, 26, 42)
WHITE = (244, 236, 236)
GRAY = (176, 162, 166)
INK = (16, 6, 9)
GREEN = (74, 222, 128)
AMBER = (255, 176, 80)

# ---------------------------------------------------------------- font 5x7
F = {
 'A':["01110","10001","10001","11111","10001","10001","10001"],
 'B':["11110","10001","10001","11110","10001","10001","11110"],
 'C':["01111","10000","10000","10000","10000","10000","01111"],
 'D':["11110","10001","10001","10001","10001","10001","11110"],
 'E':["11111","10000","10000","11110","10000","10000","11111"],
 'F':["11111","10000","10000","11110","10000","10000","10000"],
 'G':["01111","10000","10000","10011","10001","10001","01111"],
 'H':["10001","10001","10001","11111","10001","10001","10001"],
 'I':["11111","00100","00100","00100","00100","00100","11111"],
 'J':["00111","00010","00010","00010","00010","10010","01100"],
 'K':["10001","10010","10100","11000","10100","10010","10001"],
 'L':["10000","10000","10000","10000","10000","10000","11111"],
 'M':["10001","11011","10101","10101","10001","10001","10001"],
 'N':["10001","11001","10101","10011","10001","10001","10001"],
 'O':["01110","10001","10001","10001","10001","10001","01110"],
 'P':["11110","10001","10001","11110","10000","10000","10000"],
 'Q':["01110","10001","10001","10001","10101","10010","01101"],
 'R':["11110","10001","10001","11110","10100","10010","10001"],
 'S':["01111","10000","10000","01110","00001","00001","11110"],
 'T':["11111","00100","00100","00100","00100","00100","00100"],
 'U':["10001","10001","10001","10001","10001","10001","01110"],
 'V':["10001","10001","10001","10001","10001","01010","00100"],
 'W':["10001","10001","10001","10101","10101","10101","01010"],
 'X':["10001","10001","01010","00100","01010","10001","10001"],
 'Y':["10001","10001","01010","00100","00100","00100","00100"],
 'Z':["11111","00001","00010","00100","01000","10000","11111"],
 '0':["01110","10011","10101","10101","10101","11001","01110"],
 '1':["00100","01100","00100","00100","00100","00100","01110"],
 '2':["01110","10001","00001","00010","00100","01000","11111"],
 '3':["11110","00001","00001","01110","00001","00001","11110"],
 '4':["00010","00110","01010","10010","11111","00010","00010"],
 '5':["11111","10000","11110","00001","00001","10001","01110"],
 '6':["00110","01000","10000","11110","10001","10001","01110"],
 '7':["11111","00001","00010","00100","01000","01000","01000"],
 '8':["01110","10001","10001","01110","10001","10001","01110"],
 '9':["01110","10001","10001","01111","00001","00010","01100"],
 ' ':["00000"]*7,
 '.':["00000","00000","00000","00000","00000","01100","01100"],
 ',':["00000","00000","00000","00000","01100","00100","01000"],
 '+':["00000","00100","00100","11111","00100","00100","00000"],
 '-':["00000","00000","00000","11111","00000","00000","00000"],
 '>':["01000","00100","00010","00001","00010","00100","01000"],
 '/':["00001","00010","00010","00100","01000","01000","10000"],
 '*':["00000","00000","00100","01110","00100","00000","00000"],
 ':':["00000","01100","01100","00000","01100","01100","00000"],
}

def text_w(s, sc=1, gap=1):
    return len(s) * (5 + gap) * sc - gap * sc

def draw_text(px, s, x, y, col, sc=1, gap=1, shadow=None):
    if shadow:
        draw_text(px, s, x + sc, y + sc, shadow, sc, gap)
    for ch in s:
        g = F[ch]
        for r, row in enumerate(g):
            for c, b in enumerate(row):
                if b == '1':
                    for dy in range(sc):
                        for dx in range(sc):
                            put(px, x + c * sc + dx, y + r * sc + dy, col)
        x += (5 + gap) * sc

def put(px, x, y, col):
    if 0 <= x < W and 0 <= y < H:
        px[x, y] = col

# ---------------------------------------------------------------- skull sprite
def skull_sprite(size=48):
    im = Image.open(LOGO).convert("RGB")
    crop = im.crop((58, 40, 250, 232))          # skull + horn bounding box
    s = crop.resize((size, size), Image.LANCZOS)
    grid = {}
    for y in range(size):
        for x in range(size):
            r, g, b = s.getpixel((x, y))
            t = r + g + b
            if t > 560:
                grid[(x, y)] = WHITE
            elif t < 200:
                grid[(x, y)] = INK
            elif r > 150 and g < 120:
                pass                              # red background: transparent
            else:
                grid[(x, y)] = INK if t < 380 else GRAY
    # shade the right/bottom edge of the white areas for a pixel-art feel
    out = dict(grid)
    for (x, y), c in grid.items():
        if c == WHITE and ((x + 1, y + 1) not in grid):
            out[(x, y)] = GRAY
    # dark outline
    for (x, y) in list(grid):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            p = (x + dx, y + dy)
            if p not in grid and p not in out:
                out[p] = INK
    return out

SKULL = skull_sprite(54)

# The downsampled eyes are re-drawn by hand so they stay clean when animated.
# Big round eye: clear the traced one, then draw a clean ellipse each frame.
EYE_C, EYE_RX, EYE_RY = (18.0, 34.0), 8.0, 11.5
for (x, y), c in list(SKULL.items()):
    if c in (INK, GRAY) and 9 <= x <= 26 and 21 <= y <= 46 and x > 5:
        SKULL[(x, y)] = WHITE

def in_eye(x, y, grow=0.0):
    return ((x + 0.5 - EYE_C[0]) / (EYE_RX + grow)) ** 2 + ((y + 0.5 - EYE_C[1]) / (EYE_RY + grow)) ** 2 <= 1

# blink: lid position per frame (0 open .. 1 closed)
LID = {17: 0.35, 18: 0.75, 19: 1.0, 20: 1.0, 21: 0.6, 22: 0.25}

# ---------------------------------------------------------------- static layers
rnd = random.Random(7)
STARS = [(rnd.randrange(W), rnd.randrange(0, 60), rnd.random()) for _ in range(70)]

def skyline():
    xs, x = [], 0
    while x < W:
        w = rnd.randrange(7, 16)
        h = rnd.randrange(8, 26)
        xs.append((x, w, h))
        x += w + rnd.randrange(0, 3)
    wins = []
    for (bx, bw, bh) in xs:
        for wy in range(H - bh + 3, H - 3, 3):
            for wx in range(bx + 2, bx + bw - 2, 3):
                if rnd.random() < 0.35:
                    wins.append((wx, wy, rnd.randrange(N)))
    return xs, wins

BUILD, WINS = skyline()

MOON_C = (64, 48)
MOON_R = 39

def bayer(x, y):
    m = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]
    return m[y % 4][x % 4] / 16.0

# embers rising
EMBERS = [(rnd.randrange(W), rnd.randrange(H), rnd.choice([1, 2])) for _ in range(26)]

# bugs crawling on the ground line; the scanner zaps them
BUGS = [rnd.randrange(W) for _ in range(5)]

LINE1 = "ZEYAD M. SALEM"
LINE2 = "QA AUTOMATION ENGINEER / SDET"
LINE3 = "> 2,900+ TESTS PASSING"

def frame(i):
    t = i / N
    img = Image.new("RGB", (W, H), BG0)
    px = img.load()

    # sky gradient, dithered
    for y in range(H):
        v = y / H
        for x in range(W):
            d = bayer(x, y)
            if v > 0.45 + d * 0.35:
                px[x, y] = BG2 if v > 0.75 + d * 0.2 else BG1

    # stars (twinkle)
    for (sx, sy, ph) in STARS:
        b = math.sin(2 * math.pi * (t * 2 + ph))
        if b > 0.6:
            put(px, sx, sy, WHITE)
            if b > 0.92:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    put(px, sx + dx, sy + dy, MAROON2)
        elif b > -0.3:
            put(px, sx, sy, GRAY if ph > 0.5 else MAROON2)

    # blood moon (the logo's red circle), with pulsing halo
    cx, cy = MOON_C
    pulse = 0.5 + 0.5 * math.sin(2 * math.pi * t)
    for y in range(cy - MOON_R - 6, cy + MOON_R + 7):
        for x in range(cx - MOON_R - 6, cx + MOON_R + 7):
            d = math.hypot(x - cx + 0.5, y - cy + 0.5)
            if d <= MOON_R:
                # light from upper-left
                l = ((x - cx) * -0.6 + (y - cy) * -0.8) / MOON_R
                if l + bayer(x, y) * 0.5 > 0.75:
                    c = RED_HI
                elif l + bayer(x, y) * 0.5 < -0.45:
                    c = RED_LO
                else:
                    c = RED
                put(px, x, y, c)
            elif d <= MOON_R + 2 + pulse * 3 and bayer(x, y) < 0.5 - (d - MOON_R) / 12:
                put(px, x, y, MAROON2)

    # skull, bobbing
    bob = round(math.sin(2 * math.pi * t) * 1.5)
    ox, oy = cx - 27, cy - 29 + bob
    for (x, y), c in SKULL.items():
        put(px, ox + x, oy + y, c)
    # big eye: socket, lid, red pupil and a fixed shine
    lid = LID.get(i, 0.0)
    top = EYE_C[1] - EYE_RY
    cut = top + lid * EYE_RY * 2 * 0.5 + (EYE_RY if lid >= 1 else 0)
    glow = (RED_LO, RED, RED_HI, RED)[(i // 4) % 4]
    look = 1 if 8 <= i <= 15 else 0
    pcx, pcy = int(EYE_C[0]) + look, int(EYE_C[1]) + 1
    for y in range(int(top) - 1, int(EYE_C[1] + EYE_RY) + 2):
        for x in range(int(EYE_C[0] - EYE_RX) - 1, int(EYE_C[0] + EYE_RX) + 2):
            if not in_eye(x, y):
                continue
            if lid >= 1:
                if y == int(EYE_C[1]) + 2 or (y == int(EYE_C[1]) + 1 and abs(x + 0.5 - EYE_C[0]) < EYE_RX - 2):
                    put(px, ox + x, oy + y, INK)
                continue
            if y < cut:
                continue                      # covered by the lid (bone colour)
            put(px, ox + x, oy + y, INK)
            if lid > 0 and y == int(cut) and in_eye(x, y - 1):
                put(px, ox + x, oy + y - 1, GRAY)
    if lid < 0.5:
        # red ember pupil: a small vertical slit
        for dy in range(-1, 3):
            for dx in (0, 1):
                y = pcy + dy
                if y >= cut:
                    put(px, ox + pcx + dx, oy + y, glow if dy in (0, 1) else RED_LO)
        # shine
        if lid == 0:
            for (x, y) in ((13, 27), (14, 27), (13, 28), (14, 28), (16, 26)):
                put(px, ox + x, oy + y, WHITE)

    # angry eye: same ember pupil and a squint while the big eye blinks
    if lid < 0.5:
        ax, ay = 40 + look, 37
        for (dx, dy) in ((0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)):
            put(px, ox + ax + dx, oy + ay + dy, glow if dy < 2 else RED_LO)
        put(px, ox + 43, oy + 34, WHITE)

    # skyline silhouette
    for (bx, bw, bh) in BUILD:
        for y in range(H - bh, H):
            for x in range(bx, bx + bw):
                put(px, x, y, BG0 if x not in (bx,) else MAROON)
        for x in range(bx, bx + bw):
            put(px, x, H - bh, MAROON)
    for (wx, wy, ph) in WINS:
        on = ((i + ph) // 8) % 3 != 0
        if on:
            put(px, wx, wy, MAROON2 if ph % 3 else RED_LO)

    # scanner beam sweeping the city (a test run)
    sx = int(t * (W + 40)) - 20
    for y in range(H - 30, H):
        for k, col in ((0, RED_HI), (-1, RED), (-2, RED_LO), (-4, MAROON2)):
            put(px, sx + k, y, col)
    # ground line
    for x in range(W):
        put(px, x, H - 1, MAROON2 if x > sx else RED_LO)

    # bugs: alive ahead of the beam, a green check behind it
    for bx in BUGS:
        bx = (bx + i) % W
        if bx > sx:
            leg = (i // 2) % 2
            body = [(0,0),(1,0),(2,0),(3,0),(0,-1),(1,-1),(2,-1),(3,-1),(1,-2),(2,-2)]
            for (dx, dy) in body:
                put(px, bx + dx, H - 3 + dy, RED_HI)
            for (dx, dy) in ((-1, 1 - leg), (4, leg), (-1, -1 + leg), (4, -leg)):
                put(px, bx + dx, H - 3 + dy, RED)
            put(px, bx + 1, H - 6, AMBER); put(px, bx + 2, H - 6, AMBER)
        elif sx - bx < 30:
            for (dx, dy) in ((0, 0), (1, 1), (2, 2), (3, 1), (4, 0), (5, -1), (6, -2)):
                put(px, bx + dx, H - 7 + dy, GREEN)

    # embers rising
    for (ex, ey, sp) in EMBERS:
        y = (ey - i * sp) % H
        x = ex + round(math.sin((y + ex) / 9))
        if math.hypot(x - MOON_C[0], y - MOON_C[1]) > MOON_R + 2:
            put(px, x, y, RED if sp == 2 else MAROON2)

    # text block
    tx = 128
    draw_text(px, LINE1, tx, 16, WHITE, sc=2, shadow=RED_LO)
    draw_text(px, LINE2, tx, 38, RED_HI)
    # terminal line: types out, then holds with a blinking cursor
    n = min(len(LINE3), i * 2)
    shown = LINE3[:n]
    draw_text(px, shown, tx, 52, GRAY)
    cx2 = tx + text_w(shown) + 4 if shown else tx
    if n == len(LINE3):
        # the check mark when the run is green
        for (dx, dy) in ((0, 3), (1, 4), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)):
            put(px, cx2 + dx, 52 + dy, GREEN)
        cx2 += 11
    if (i // 3) % 2 == 0:
        for y in range(52, 59):
            put(px, cx2, y, RED_HI)
            put(px, cx2 + 1, y, RED_HI)

    return img.resize((W * SCALE, H * SCALE), Image.NEAREST)

frames = [frame(i) for i in range(N)]
cols = [BG0,BG1,BG2,MAROON,MAROON2,RED,RED_HI,RED_LO,WHITE,GRAY,INK,GREEN,AMBER]
pal = Image.new('P', (1, 1)); flat = [v for c in cols for v in c]; pal.putpalette(flat + flat[:3] * (256 - len(cols)))
qf = [f.quantize(palette=pal, dither=Image.NONE) for f in frames]
qf[0].save(OUT, save_all=True, append_images=qf[1:], duration=90, loop=0, optimize=True, disposal=1)
print("ok", OUT)
