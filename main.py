
import turtle
import random
import math

# ==========================================
# NOITE ESTRELADA - ANIMAÇÃO PONTILHISTA
# ==========================================

random.seed(15)

tela = turtle.Screen()
tela.setup(1000, 750)
tela.title("A Noite Estrelada - Pontilhismo")
tela.bgcolor("#07152e")
tela.tracer(0)

pincel = turtle.Turtle()
pincel.hideturtle()
pincel.penup()
pincel.speed(0)

pontos = []

azuis = [
    "#102957", "#163b75", "#20569a",
    "#2875b8", "#438dc9", "#75b9df"
]

amarelos = [
    "#ffd447", "#ffe66d", "#fff0a0",
    "#f9bd35", "#fff8ce"
]

def adicionar(x, y, cor, tamanho):
    pontos.append((x, y, cor, tamanho))

# ------------------------------------------
# 1. CÉU AZUL
# ------------------------------------------

for i in range(2500):
    x = random.uniform(-490, 490)
    y = random.uniform(-20, 350)

    onda = math.sin(x / 80) * 15
    y += onda

    adicionar(
        x, y,
        random.choice(azuis),
        random.randint(2, 5)
    )

# ------------------------------------------
# 2. REDemoinhos de Van Gogh
# ------------------------------------------

redemoinhos = [
    (-180, 210, 100),
    (60, 190, 75),
    (280, 240, 65),
    (-330, 100, 45),
    (150, 65, 40),
    (-30, 290, 35)
]

for cx, cy, raio in redemoinhos:
    # Pontos ao redor dos redemoinhos
    for i in range(350):
        angulo = random.uniform(0, 2 * math.pi)
        r = random.uniform(raio * 0.45, raio)

        x = cx + r * math.cos(angulo)
        y = cy + r * math.sin(angulo) * 0.65

        if -480 < x < 480 and -40 < y < 355:
            adicionar(
                x, y,
                random.choice(azuis),
                random.randint(2, 5)
            )

    # Espiral pontilhada
    for i in range(350):
        angulo = i * 0.09
        r = 2 + i * raio / 350

        x = cx + r * math.cos(angulo)
        y = cy + r * math.sin(angulo) * 0.65

        if -480 < x < 480 and -40 < y < 355:
            adicionar(
                x, y,
                random.choice(azuis),
                random.randint(2, 5)
            )

# ------------------------------------------
# 3. LUA
# ------------------------------------------

lua_x, lua_y = 340, 245

# Halo luminoso
for i in range(300):
    angulo = random.uniform(0, 2 * math.pi)
    r = random.uniform(27, 58)

    adicionar(
        lua_x + math.cos(angulo) * r,
        lua_y + math.sin(angulo) * r,
        random.choice(["#284b85", "#4776a6", "#a7c9dc"]),
        random.randint(2, 4)
    )

# Lua preenchida por pontos
for i in range(550):
    angulo = random.uniform(0, 2 * math.pi)
    r = 25 * math.sqrt(random.random())

    adicionar(
        lua_x + math.cos(angulo) * r,
        lua_y + math.sin(angulo) * r,
        random.choice(amarelos),
        random.randint(3, 7)
    )

# Anel luminoso
for i in range(180):
    angulo = random.uniform(0, 2 * math.pi)
    r = random.uniform(29, 40)

    adicionar(
        lua_x + math.cos(angulo) * r,
        lua_y + math.sin(angulo) * r,
        random.choice(amarelos),
        random.randint(2, 4)
    )

# ------------------------------------------
# 4. ESTRELAS
# ------------------------------------------

estrelas = [
    (-350, 260, 15),
    (-230, 150, 12),
    (-65, 235, 14),
    (110, 270, 11),
    (245, 130, 12),
    (390, 95, 10),
    (-400, 20, 10),
    (25, 110, 12)
]

for x, y, raio in estrelas:
    # Brilho ao redor
    for i in range(65):
        angulo = random.uniform(0, 2 * math.pi)
        r = random.uniform(raio * 0.5, raio * 1.8)

        adicionar(
            x + math.cos(angulo) * r,
            y + math.sin(angulo) * r,
            random.choice(["#254d87", "#527eae", "#e6c65b"]),
            random.randint(2, 4)
        )

    # Núcleo
    for i in range(65):
        angulo = random.uniform(0, 2 * math.pi)
        r = raio * math.sqrt(random.random())

        adicionar(
            x + math.cos(angulo) * r,
            y + math.sin(angulo) * r,
            random.choice(amarelos),
            random.randint(3, 6)
        )

    # Raios
    for k in range(4):
        angulo = k * math.pi / 2

        for d in range(4, raio + 12, 5):
            adicionar(
                x + math.cos(angulo) * d,
                y + math.sin(angulo) * d,
                "#ffe66d",
                random.randint(3, 5)
            )

# Pequenas estrelas espalhadas
for i in range(180):
    adicionar(
        random.uniform(-480, 480),
        random.uniform(-10, 340),
        random.choice(["#d7dce9", "#ffe88a", "#6b9acb"]),
        random.randint(2, 4)
    )

# ------------------------------------------
# 5. MONTANHAS
# ------------------------------------------

for i in range(1200):
    x = random.uniform(-500, 500)

    limite = (
        -170
        + 38 * math.sin(x / 95)
        + 15 * math.sin(x / 35)
    )

    y = random.uniform(-250, limite)

    adicionar(
        x, y,
        random.choice([
            "#07152e", "#0a1d3c",
            "#102849", "#173354"
        ]),
        random.randint(3, 7)
    )

# ------------------------------------------
# 6. CIPRESTE
# ------------------------------------------

for i in range(1400):
    y = random.uniform(-240, 115)

    largura = 8 + (115 - y) * 0.13
    centro = -370 + 0.08 * (y + 240)

    x = random.uniform(
        centro - largura,
        centro + largura
    )

    adicionar(
        x, y,
        random.choice([
            "#06131d", "#0b251f",
            "#12372c", "#174332",
            "#1e5137", "#28633e"
        ]),
        random.randint(3, 7)
    )

# ------------------------------------------
# 7. VILAREJO
# ------------------------------------------

casas = [
    (-220, 35, 48),
    (-170, 28, 36),
    (-115, 42, 55),
    (-50, 30, 40),
    (15, 40, 46),
    (80, 32, 35),
    (130, 45, 52),
    (205, 30, 38),
    (260, 38, 43)
]

for cx, largura, altura in casas:
    base = -215

    # Paredes
    for i in range(100):
        x = random.uniform(cx, cx + largura)
        y = random.uniform(base, base + altura)

        adicionar(
            x, y,
            random.choice(["#102b42", "#17374e", "#24465b"]),
            random.randint(3, 5)
        )

    # Telhados
    for i in range(100):
        x = random.uniform(cx - 5, cx + largura + 5)

        proporcao = abs(
            x - (cx + largura / 2)
        ) / (largura / 2 + 5)

        topo = base + altura + 18

        y = random.uniform(
            base + altura,
            topo - proporcao * 18
        )

        adicionar(
            x, y,
            random.choice(["#152a3e", "#24394a", "#30475a"]),
            random.randint(2, 4)
        )

    # Janelas iluminadas
    for wx in range(cx + 8, cx + largura - 3, 12):
        for wy in range(base + 12, base + altura - 5, 15):
            adicionar(
                wx, wy,
                random.choice(["#ffd75a", "#eebd43", "#ffe89a"]),
                random.randint(3, 5)
            )

# ------------------------------------------
# 8. IGREJA NO CENTRO
# ------------------------------------------

for i in range(240):
    adicionar(
        random.uniform(-17, 17),
        random.uniform(-215, -155),
        random.choice(["#30485c", "#203a50", "#42596a"]),
        random.randint(3, 5)
    )

for i in range(160):
    adicionar(
        random.uniform(-9, 9),
        random.uniform(-175, -135),
        "#385064",
        random.randint(3, 5)
    )

# Cruz
for i in range(35):
    adicionar(
        random.uniform(-2, 2),
        random.uniform(-145, -125),
        "#e8d6a0",
        random.randint(2, 4)
    )

for i in range(20):
    adicionar(
        random.uniform(-8, 8),
        random.uniform(-137, -133),
        "#e8d6a0",
        3
    )

# ------------------------------------------
# 9. ANIMAÇÃO: REVELAR OS PONTOS
# ------------------------------------------

# Mistura os pontos para que a pintura surja
# gradualmente por toda a tela.
random.shuffle(pontos)

indice = 0
lote = 35
intervalo = 1

def animar():
    global indice

    fim = min(indice + lote, len(pontos))

    for i in range(indice, fim):
        x, y, cor, tamanho = pontos[i]

        pincel.goto(x, y)
        pincel.dot(tamanho, cor)

    indice = fim
    tela.update()

    if indice < len(pontos):
        tela.ontimer(animar, intervalo)
    else:
        tela.title("Noite Estrelada - Pintura concluída!")
        print("A pintura foi concluída!")

# Começa com a tela quase vazia
tela.update()
tela.ontimer(animar, 500)

turtle.done()

