import turtle
import math
import random

# =====================================
# NOITE ESTRELADA - PONTILHISMO
# Inspirado em Vincent van Gogh
# =====================================

random.seed(15)

tela = turtle.Screen()
tela.setup(1000, 750)
tela.title("Noite Estrelada - Pontilhismo")
tela.bgcolor("#07152e")
tela.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

def ponto(x, y, cor, tamanho):
    t.goto(x, y)
    t.dot(tamanho, cor)

# Paleta de cores
azuis = [
    "#102957", "#163b75", "#20569a",
    "#2875b8", "#438dc9", "#75b9df"
]

amarelos = [
    "#ffd447", "#ffe66d", "#fff0a0",
    "#f9bd35", "#fff8ce"
]

# -------------------------------------
# 1. Céu com ondas e espirais pontilhadas
# -------------------------------------

for faixa in range(7):
    y_base = -10 + faixa * 65

    for i in range(240):
        x = random.uniform(-490, 490)

        onda = (
            math.sin(x / 85 + faixa * 0.8) * 18
            + math.sin(x / 35 + faixa) * 5
        )

        y = y_base + onda + random.uniform(-20, 20)

        ponto(
            x, y,
            random.choice(azuis),
            random.randint(2, 5)
        )

# Grandes redemoinhos de Van Gogh
redemoinhos = [
    (-180, 210, 100, 3.5),
    (60, 190, 75, 4.0),
    (280, 245, 65, 3.2),
    (-330, 100, 48, 3.5),
    (150, 65, 42, 3.5),
    (-30, 290, 35, 3.0)
]

for cx, cy, raio, voltas in redemoinhos:
    for i in range(850):
        angulo = random.uniform(0, math.pi * 2)

        # Distribuição dos pontos em anéis
        r = random.uniform(raio * 0.45, raio)
        x = cx + r * math.cos(angulo)
        y = cy + r * math.sin(angulo) * 0.65

        if -480 < x < 480 and -50 < y < 355:
            ponto(
                x, y,
                random.choice(azuis),
                random.randint(2, 5)
            )

    # Espiral de pinceladas
    for i in range(550):
        a = i * 0.045
        r = 3 + i * raio / 550

        x = cx + r * math.cos(a * voltas)
        y = cy + r * math.sin(a * voltas) * 0.65

        if -480 < x < 480 and -50 < y < 355:
            ponto(
                x, y,
                random.choice(azuis),
                random.randint(2, 5)
            )

# -------------------------------------
# 2. Lua brilhante
# -------------------------------------

lua_x, lua_y = 340, 245

# Halo da lua
for i in range(500):
    angulo = random.uniform(0, 2 * math.pi)
    r = random.uniform(28, 57)

    x = lua_x + math.cos(angulo) * r
    y = lua_y + math.sin(angulo) * r

    ponto(x, y, random.choice(
        ["#284b85", "#4776a6", "#a7c9dc"]
    ), random.randint(2, 4))

# Disco lunar feito de pontos
for i in range(650):
    angulo = random.uniform(0, 2 * math.pi)
    r = 25 * math.sqrt(random.random())

    x = lua_x + math.cos(angulo) * r
    y = lua_y + math.sin(angulo) * r

    ponto(x, y, random.choice(amarelos),
          random.randint(3, 7))

# Anéis de luz
for i in range(150):
    a = random.uniform(0, 2 * math.pi)
    r = random.uniform(30, 42)

    ponto(
        lua_x + math.cos(a) * r,
        lua_y + math.sin(a) * r,
        "#f9c94b",
        random.randint(2, 4)
    )

# -------------------------------------
# 3. Estrelas luminosas
# -------------------------------------

estrelas = [
    (-350, 260, 17),
    (-230, 150, 13),
    (-65, 235, 15),
    (110, 270, 12),
    (245, 130, 13),
    (390, 95, 10),
    (-400, 20, 11),
    (25, 110, 12)
]

for x, y, raio in estrelas:
    # Aura estrelada
    for i in range(100):
        a = random.uniform(0, 2 * math.pi)
        r = random.uniform(raio * 0.5, raio * 1.8)

        ponto(
            x + math.cos(a) * r,
            y + math.sin(a) * r,
            random.choice(["#254d87", "#527eae", "#e6c65b"]),
            random.randint(2, 4)
        )

    # Centro da estrela
    for i in range(100):
        a = random.uniform(0, 2 * math.pi)
        r = raio * math.sqrt(random.random())

        ponto(
            x + math.cos(a) * r,
            y + math.sin(a) * r,
            random.choice(amarelos),
            random.randint(3, 7)
        )

    # Raios em forma de cruz
    for k in range(4):
        a = k * math.pi / 2

        for d in range(4, raio + 12, 5):
            ponto(
                x + math.cos(a) * d,
                y + math.sin(a) * d,
                "#ffe66d",
                random.randint(3, 6)
            )

# -------------------------------------
# 4. Montanhas ao fundo
# -------------------------------------

for i in range(1800):
    x = random.uniform(-500, 500)

    y_montanha = (
        -170
        + 38 * math.sin(x / 95)
        + 15 * math.sin(x / 35)
    )

    y = random.uniform(-245, y_montanha)

    ponto(
        x, y,
        random.choice([
            "#07152e", "#0a1d3c",
            "#102849", "#173354"
        ]),
        random.randint(3, 7)
    )

# Ondas de luz sobre as montanhas
for i in range(700):
    x = random.uniform(-490, 490)

    y = (
        -170
        + 38 * math.sin(x / 95)
        + 15 * math.sin(x / 35)
        + random.uniform(-12, 8)
    )

    ponto(
        x, y,
        random.choice(["#23466b", "#315a80", "#47789a"]),
        random.randint(2, 4)
    )

# -------------------------------------
# 5. Cipreste escuro à esquerda
# -------------------------------------

for i in range(1800):
    y = random.uniform(-240, 115)

    # Árvore estreita embaixo e pontiaguda em cima
    largura = 8 + (115 - y) * 0.13
    centro = -370 + 0.08 * (y + 240)

    x = random.uniform(
        centro - largura,
        centro + largura
    )

    ponto(
        x, y,
        random.choice([
            "#06131d", "#0b251f",
            "#12372c", "#174332"
        ]),
        random.randint(3, 8)
    )

# Pontos verdes que sugerem a textura da árvore
for i in range(500):
    y = random.uniform(-225, 100)
    largura = 8 + (115 - y) * 0.13
    centro = -370 + 0.08 * (y + 240)

    x = random.uniform(
        centro - largura,
        centro + largura
    )

    ponto(
        x, y,
        random.choice(["#1e5137", "#28633e", "#47784a"]),
        random.randint(2, 4)
    )

# -------------------------------------
# 6. Vilarejo com casas pontilhadas
# -------------------------------------

for cx, largura, altura in [
    (-220, 35, 48),
    (-170, 28, 36),
    (-115, 42, 55),
    (-50, 30, 40),
    (15, 40, 46),
    (80, 32, 35),
    (130, 45, 52),
    (205, 30, 38),
    (260, 38, 43)
]:
    base = -215

    # Paredes das casas
    for i in range(180):
        x = random.uniform(cx, cx + largura)
        y = random.uniform(base, base + altura)

        ponto(
            x, y,
            random.choice(["#102b42", "#17374e", "#24465b"]),
            random.randint(3, 5)
        )

    # Telhados triangulares
    for i in range(180):
        x = random.uniform(cx - 5, cx + largura + 5)
        proporcao = abs(
            x - (cx + largura / 2)
        ) / (largura / 2 + 5)

        y_topo = base + altura + 18
        y = random.uniform(
            base + altura,
            y_topo - proporcao * 18
        )

        ponto(
            x, y,
            random.choice(["#152a3e", "#24394a", "#30475a"]),
            random.randint(2, 4)
        )

    # Janelas iluminadas
    for wx in range(cx + 8, cx + largura - 3, 12):
        for wy in range(base + 12, base + altura - 5, 15):
            ponto(
                wx, wy,
                random.choice(["#ffd75a", "#eebd43", "#ffe89a"]),
                random.randint(3, 5)
            )

# -------------------------------------
# 7. Pequena igreja
# -------------------------------------

igreja_x = 0
igreja_y = -215

for i in range(300):
    x = random.uniform(-17, 17)
    y = random.uniform(-215, -155)

    ponto(
        x, y,
        random.choice(["#30485c", "#203a50", "#42596a"]),
        random.randint(3, 5)
    )

# Torre
for i in range(180):
    x = random.uniform(-9, 9)
    y = random.uniform(-175, -135)

    ponto(x, y, "#385064", random.randint(3, 5))

# Cruz da igreja
for i in range(35):
    ponto(
        random.uniform(-2, 2),
        random.uniform(-145, -125),
        "#e8d6a0",
        random.randint(2, 4)
    )

for i in range(20):
    ponto(
        random.uniform(-8, 8),
        random.uniform(-137, -133),
        "#e8d6a0",
        3
    )

# -------------------------------------
# 8. Estrelas pequenas espalhadas
# -------------------------------------

for i in range(220):
    x = random.uniform(-480, 480)
    y = random.uniform(-10, 340)

    ponto(
        x, y,
        random.choice(["#d7dce9", "#ffe88a", "#6b9acb"]),
        random.randint(2, 4)
    )

# Finalizar desenho
tela.update()

print("Pintura pontilhista concluída!")
turtle.done()
