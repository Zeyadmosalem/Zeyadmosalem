"""Animated pixel-art banner for the profile README: the skull logo as a hooded coder at a laptop.

Usage: python3 tools/make_banner.py banner.gif path/to/logo.png  (transparent skull, or the round final-logo JPG)
"""
import math, random, sys
from PIL import Image

LOGO = sys.argv[2] if len(sys.argv) > 2 else "tools/logo.png"
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
 '<':["00010","00100","01000","10000","01000","00100","00010"],
 '{':["00110","01000","01000","10000","01000","01000","00110"],
 '}':["01100","00010","00010","00001","00010","00010","01100"],
 '(':["00010","00100","01000","01000","01000","00100","00010"],
 ')':["01000","00100","00010","00010","00010","00100","01000"],
 ';':["00000","01100","01100","00000","01100","00100","01000"],
 '=':["00000","00000","11111","00000","11111","00000","00000"],
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
    src = Image.open(LOGO)
    if src.mode == "RGBA":                        # transparent skull (portfolio assets/logo.png)
        im = Image.new("RGB", src.size, (209, 42, 60))
        im.paste(src, (0, 0), src)
        x0, y0, x1, y1 = src.getbbox()
        side = max(x1 - x0, y1 - y0)
        crop = im.crop((x0, y0, x0 + side, y0 + side))
    else:                                         # the round "final logo" JPG
        crop = src.convert("RGB").crop((58, 40, 250, 232))
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


# ================================================================ the coder scene
PANEL = (30, 9, 15)
PANEL_HI = (48, 13, 22)
STEEL = (58, 40, 46)
STEEL_HI = (92, 70, 76)
SCREEN_BG = (26, 6, 10)
HOOD = (84, 18, 31)
HOOD_HI = (128, 28, 45)
GLOW = (120, 30, 44)

def bayer(x, y):
    m = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]
    return m[y % 4][x % 4] / 16.0

def rect(px, x0, y0, x1, y1, col):
    for y in range(y0, y1):
        for x in range(x0, x1):
            put(px, x, y, col)

def frame_box(px, x0, y0, x1, y1, body, hi, lo):
    rect(px, x0, y0, x1, y1, body)
    for x in range(x0, x1):
        put(px, x, y0, hi); put(px, x, y1 - 1, lo)
    for y in range(y0, y1):
        put(px, x0, y, hi); put(px, x1 - 1, y, lo)

rnd = random.Random(5)
SK = skull_sprite(38)
STARS = [(rnd.randrange(8, 38), rnd.randrange(12, 40), rnd.random()) for _ in range(14)]
EMBERS = [(rnd.randrange(150, W), rnd.randrange(H), rnd.choice([1, 2])) for _ in range(16)]

# code on the monitor: each line = (indent, [(len, colour)])
CODE_COLS = [RED_HI, GRAY, GRAY, GREEN, AMBER, STEEL_HI]
CODE = []
indent = 0
for k in range(N):
    segs = [(rnd.randrange(2, 6), rnd.choice(CODE_COLS)) for _ in range(rnd.randrange(1, 4))]
    CODE.append((indent, segs))
    indent = max(0, min(3, indent + rnd.choice([-1, 0, 0, 1])))

CX, CY = 66, 38          # centre of the skull head

def draw(px, i):
    t = i / N
    # ---- wall
    for y in range(H):
        for x in range(W):
            px[x, y] = BG1 if bayer(x, y) > y / H * 0.9 else BG2
    for x in range(0, W, 48):
        for y in range(0, 78):
            put(px, x, y, BG0)

    # ---- window with the night city + blood moon
    frame_box(px, 6, 8, 40, 48, PANEL_HI, HOOD_HI, BG0)
    rect(px, 8, 10, 38, 46, BG0)
    for (sx, sy, ph) in STARS:
        if math.sin(2 * math.pi * (t * 2 + ph)) > 0.2:
            put(px, sx, sy, GRAY if ph > 0.5 else MAROON2)
    for y in range(13, 26):
        for x in range(23, 36):
            if math.hypot(x - 29 + 0.5, y - 19 + 0.5) <= 5.5:
                put(px, x, y, RED_HI if (x - 29) + (y - 19) < -3 else RED)
    for (bx, bw, bh) in ((8, 5, 8), (13, 6, 13), (19, 4, 6), (23, 7, 11), (30, 8, 7)):
        rect(px, bx, 46 - bh, bx + bw, 46, PANEL)
        for wy in range(46 - bh + 2, 45, 3):
            if (wy + bx + i // 6) % 4 == 0:
                put(px, bx + 2, wy, RED_LO)
    rect(px, 22, 10, 24, 46, PANEL_HI)
    rect(px, 8, 27, 38, 29, PANEL_HI)

    # ---- shelf with books
    rect(px, 100, 26, 142, 28, PANEL_HI)
    bx = 103
    for (w, h, c) in ((3, 9, RED_LO), (2, 7, STEEL), (3, 10, MAROON2), (2, 8, RED), (4, 6, STEEL_HI), (3, 9, HOOD_HI)):
        rect(px, bx, 26 - h, bx + w, 26, c)
        bx += w + 1
    # a tiny pixel bug in a jar on the shelf
    frame_box(px, 130, 17, 138, 26, BG0, STEEL_HI, STEEL)
    put(px, 133 + (i // 4) % 2, 22, RED_HI); put(px, 134 + (i // 4) % 2, 22, RED_HI); put(px, 133 + (i // 4) % 2, 21, AMBER)

    # ---- the coder: hood
    bob = 1 if (i // 2) % 4 == 0 else 0
    hx, hy = CX, CY + bob
    for y in range(hy - 25, hy + 30):
        for x in range(hx - 28, hx + 29):
            d = ((x + 0.5 - hx) / 26) ** 2 + ((y + 0.5 - hy - 2) / 25) ** 2
            if d <= 1:
                rim = ((x + 0.5 - hx) / 26) ** 2 + ((y + 0.5 - hy - 1) / 25) ** 2 > 0.82 and x < hx
                put(px, x, y, HOOD_HI if rim else HOOD)
    # body / shoulders
    for y in range(hy + 16, 79):
        half = 20 + (y - hy - 16) * 0.9
        for x in range(int(hx - half), int(hx + half) + 1):
            put(px, x, y, HOOD if x > hx - half + 2 else HOOD_HI)
    # hoodie strings
    for y in range(hy + 18, hy + 27):
        put(px, hx - 5, y, GRAY); put(px, hx + 5, y, GRAY)
    # inside of the hood (shadow around the face)
    for y in range(hy - 20, hy + 22):
        for x in range(hx - 21, hx + 22):
            if ((x + 0.5 - hx) / 20) ** 2 + ((y + 0.5 - hy) / 21) ** 2 <= 1:
                put(px, x, y, BG0)
    # skull head
    ox, oy = hx - 19, hy - 21
    for (x, y), c in SK.items():
        # screen glow from the laptop on the lower face
        if c == WHITE and y > 26 and bayer(x, y) < 0.35:
            c = (250, 214, 214)
        put(px, ox + x, oy + y, c)
    glow = (RED_LO, RED, RED_HI, RED)[(i // 3) % 4]
    for (x, y) in ((12, 23), (13, 23), (12, 24), (13, 24), (27, 25), (28, 25)):
        put(px, ox + x, oy + y, glow)

    # ---- desk
    rect(px, 0, 78, W, H, PANEL)
    for x in range(0, W):
        put(px, x, 78, HOOD_HI)
        put(px, x, 79, MAROON2)
    for y in range(80, H):
        for x in range(0, W):
            if bayer(x, y) > 0.85:
                put(px, x, y, BG1)

    # ---- laptop (lid faces us) with the logo sticker
    frame_box(px, 44, 58, 90, 78, STEEL, STEEL_HI, PANEL)
    rect(px, 40, 77, 94, 79, STEEL_HI)
    for y in range(63, 74):
        for x in range(61, 73):
            if math.hypot(x - 67 + 0.5, y - 68.5) <= 5.2:
                put(px, x, y, RED)
    for (x, y) in ((65, 66), (66, 66), (68, 66), (69, 66), (65, 67), (66, 67), (68, 67), (69, 67), (67, 70), (65, 71), (66, 71), (67, 71), (68, 71), (69, 71), (64, 68), (70, 68), (64, 69), (65, 69), (66, 69), (67, 69), (68, 69), (69, 69), (70, 69)):
        put(px, x, y, WHITE)
    for (x, y) in ((65, 67), (66, 67), (68, 67), (69, 67)):
        put(px, x, y, INK)
    # glow spilling over the lid top
    for x in range(46, 89):
        if bayer(x, 57) < 0.5:
            put(px, x, 57, GLOW)

    # ---- skeleton hands typing on either side of the lid
    for side, x0 in ((0, 37), (1, 90)):
        up = ((i + side * 2) // 2) % 2
        y0 = 73 - up
        for (dx, dy) in ((0, 1), (1, 0), (2, 0), (3, 0), (4, 1), (1, 1), (2, 1), (3, 1), (0, 2), (2, 2), (4, 2)):
            put(px, x0 + dx, y0 + dy, WHITE)
        for dx in range(-1, 6):
            put(px, x0 + dx, y0 - 1, HOOD_HI)      # sleeve cuff

    # ---- mug + steam
    frame_box(px, 14, 70, 22, 78, GRAY, WHITE, STEEL_HI)
    rect(px, 22, 72, 24, 76, GRAY)
    put(px, 16, 73, RED); put(px, 17, 73, RED); put(px, 18, 73, RED); put(px, 17, 74, RED)
    for k in range(4):
        y = 68 - ((i + k * 3) % 12)
        x = 16 + k % 3 + round(math.sin((y + k) / 2))
        put(px, x, y, STEEL if (i + k * 3) % 12 < 7 else PANEL_HI)

    # ---- second monitor with scrolling code
    frame_box(px, 100, 38, 144, 70, STEEL, STEEL_HI, PANEL)
    rect(px, 102, 40, 142, 68, SCREEN_BG)
    scroll = i // 2
    for row in range(9):
        ind, segs = CODE[(scroll + row) % N]
        y = 41 + row * 3
        put(px, 103, y, MAROON2)                    # line number gutter
        x = 106 + ind * 3
        for (l, c) in segs:
            for k in range(l):
                if x < 141:
                    put(px, x, y, c)
                x += 1
            x += 1
    # blinking cursor on the last line
    if (i // 2) % 2 == 0:
        rect(px, 106, 65, 108, 67, RED_HI)
    rect(px, 119, 70, 125, 76, STEEL)
    rect(px, 113, 76, 131, 78, STEEL_HI)

    # ---- speech bubble: </> while coding, then a green check when the build passes
    phase = i % N
    if 2 <= phase < 14 or 18 <= phase < 30:
        bx0, by0, bx1, by1 = 88, 4, 112, 15
        rect(px, bx0 + 1, by0, bx1 - 1, by1, WHITE)
        rect(px, bx0, by0 + 1, bx1, by1 - 1, WHITE)
        put(px, bx0 + 3, by1, WHITE); put(px, bx0 + 2, by1 + 1, WHITE); put(px, bx0 + 1, by1 + 2, WHITE)
        if phase < 14:
            draw_text(px, "</>", bx0 + 4, by0 + 2, RED)
        else:
            for (dx, dy) in ((0, 3), (1, 4), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (1, 3), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)):
                put(px, bx0 + 9 + dx, by0 + 2 + dy, (40, 170, 90))

    # ---- divider + embers on the right
    for (ex, ey, sp) in EMBERS:
        y = (ey - i * sp) % H
        if y < 77:
            put(px, ex + round(math.sin((y + ex) / 9)), y, RED if sp == 2 else MAROON2)

    # ---- text
    tx = 148
    draw_text(px, "ZEYAD M. SALEM", tx, 26, WHITE, sc=2, gap=1, shadow=RED_LO)
    draw_text(px, "FULL-STACK DEVELOPER", tx, 48, RED_HI)
    line = "> BUILD. TEST. SHIP."
    n = min(len(line), i)
    shown = line[:n]
    draw_text(px, shown, tx, 62, GRAY)
    cx2 = tx + text_w(shown) + 4 if shown else tx
    if n == len(line):
        for (dx, dy) in ((0, 3), (1, 4), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)):
            put(px, cx2 + dx, 62 + dy, GREEN)
        cx2 += 11
    if (i // 3) % 2 == 0:
        rect(px, cx2, 62, cx2 + 2, 69, RED_HI)

def frame(i):
    img = Image.new("RGB", (W, H), BG0)
    draw(img.load(), i)
    return img.resize((W * SCALE, H * SCALE), Image.NEAREST)

frames = [frame(i) for i in range(N)]
cols = [BG0, BG1, BG2, MAROON, MAROON2, RED, RED_HI, RED_LO, WHITE, GRAY, INK, GREEN, AMBER,
        PANEL, PANEL_HI, STEEL, STEEL_HI, SCREEN_BG, HOOD, HOOD_HI, GLOW, (250, 214, 214), (40, 170, 90)]
pal = Image.new('P', (1, 1)); flat = [v for c in cols for v in c]
pal.putpalette(flat + flat[:3] * (256 - len(cols)))
qf = [f.quantize(palette=pal, dither=Image.NONE) for f in frames]
qf[0].save(OUT, save_all=True, append_images=qf[1:], duration=100, loop=0, optimize=True, disposal=1)
print("ok", OUT)
