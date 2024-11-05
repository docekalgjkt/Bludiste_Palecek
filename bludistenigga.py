import tkinter as tk

# Příklad bludiště - 1 je stěna, 0 je cesta
bludiste = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Konstanty
VELIKOST_CTVERCE = 40  # Velikost každého čtverce
PADDING = 10  # Mezera okolo bludiště

# Inicializace hlavního okna Tkinter
root = tk.Tk()
root.title("Bludiště v Tkinteru")

# Vytvoření canvasu pro kreslení
canvas = tk.Canvas(root, width=len(bludiste[0]) * VELIKOST_CTVERCE + PADDING * 2,
                   height=len(bludiste) * VELIKOST_CTVERCE + PADDING * 2)
canvas.pack()

# Funkce pro vykreslení bludiště na canvas
def nakresli_bludiste():
    for i in range(len(bludiste)):
        for j in range(len(bludiste[i])):
            x1 = PADDING + j * VELIKOST_CTVERCE
            y1 = PADDING + i * VELIKOST_CTVERCE
            x2 = x1 + VELIKOST_CTVERCE
            y2 = y1 + VELIKOST_CTVERCE
            if bludiste[i][j] == 1:
                # Stěna - kreslíme černý čtverec
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")
            else:
                # Cesta - kreslíme bílý čtverec
                canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

# Volání funkce pro vykreslení bludiště
nakresli_bludiste()

# Spuštění hlavní smyčky Tkinteru
root.mainloop()
