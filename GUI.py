import tkinter as tk
from tkinter import ttk
import json
from ttkthemes import ThemedTk

def sauvegarder():
    # Sauvegarder les données modifiées dans le fichier JSON
    with open("yokaiData.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def modifier_yokai(index):
    yokai = data["yokaiList"][index]
    ancien_nom = yokai["nom"]  # Sauvegarder l'ancien nom
    yokai["nom"] = variables_values["nom"].get()
    sauvegarder()

    # Mettre à jour les noms dans le menu déroulant
    yokai_names[index] = format_yokai_name(index)
    combo_yokai['values'] = yokai_names

    # Sélectionner le Yo-kai avec le nouveau nom
    combo_yokai.set(format_yokai_name(index))
    yokai["nom"] = variables_values["nom"].get()
    yokai["modele3D"] = variables_values["modele3D"].get()
    yokai["PV"] = int(variables_values["PV"].get())
    yokai["Force"] = int(variables_values["Force"].get())
    yokai["Esprit"] = int(variables_values["Esprit"].get())
    yokai["Defense"] = int(variables_values["Defense"].get())
    yokai["VIT"] = int(variables_values["VIT"].get())
    yokai["Rang"] = int(variables_values["Rang"].get())
    yokai["Tribu"] = int(variables_values["Tribu"].get())
    yokai["Element"] = int(variables_values["Element"].get())
    yokai["role"] = int(variables_values["role"].get())
    yokai["Medalium"] = int(variables_values["Medalium"].get())
    sauvegarder()

def selectionner_yokai(event):
    index = combo_yokai.current()
    if index >= 0:
        # Mettre à jour les variables tkinter avec les valeurs du Yo-kai sélectionné
        yokai = data["yokaiList"][index]
        variables_values["nom"].set(yokai["nom"])
        variables_values["modele3D"].set(yokai["modele3D"])
        variables_values["PV"].set(str(yokai["PV"]))
        variables_values["Force"].set(str(yokai["Force"]))
        variables_values["Esprit"].set(str(yokai["Esprit"]))
        variables_values["Defense"].set(str(yokai["Defense"]))
        variables_values["VIT"].set(str(yokai["VIT"]))
        variables_values["Rang"].set(str(yokai["Rang"]))
        variables_values["Tribu"].set(str(yokai["Tribu"]))
        variables_values["Element"].set(str(yokai["Element"]))
        variables_values["role"].set(str(yokai["role"]))
        variables_values["Medalium"].set(str(yokai["Medalium"]))

def ajouter_nouveau_yokai():
    # Ajouter un nouveau Yo-kai avec des valeurs par défaut à 0
    nouveau_yokai = {
        "nom": "Nouveau Yokai",
        "modele3D": "ModeleParDefaut",
        "PV": 0,
        "Force": 0,
        "Esprit": 0,
        "Defense": 0,
        "VIT": 0,
        "Rang": 0,
        "Tribu": 0,
        "Element": 0,
        "role": 0,
        "Medalium": 0
    }
    data["yokaiList"].append(nouveau_yokai)

    # Mettre à jour la liste déroulante
    yokai_names = [yokai["nom"] for yokai in data["yokaiList"]]
    combo_yokai['values'] = yokai_names

    # Sélectionner le nouveau Yo-kai
    combo_yokai.current(len(data["yokaiList"]) - 1)

# Créer et afficher l'interface avec le thème ttkthemes
root = ThemedTk(theme="plastik")  # Choisissez le thème que vous préférez
root.title("YKWB3 Éditeur de BDD")

# Charger les données JSON
with open("YokaiData.json", encoding="utf-8") as f:
    data = json.load(f)

# Déclaration des variables globales
variables_values = {
    "nom": tk.StringVar(value=""),
    "modele3D": tk.StringVar(value=""),
    "PV": tk.StringVar(value=""),
    "Force": tk.StringVar(value=""),
    "Esprit": tk.StringVar(value=""),
    "Defense": tk.StringVar(value=""),
    "VIT": tk.StringVar(value=""),
    "Rang": tk.StringVar(value=""),
    "Tribu": tk.StringVar(value=""),
    "Element": tk.StringVar(value=""),
    "role": tk.StringVar(value=""),
    "Medalium": tk.StringVar(value=""),
}

# Créer un frame
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Créer un menu déroulant pour sélectionner le Yo-kai
def format_yokai_name(index):
    yokai = data["yokaiList"][index]
    return f"{yokai['Medalium']} - {yokai['nom']}"

yokai_names = [format_yokai_name(i) for i in range(len(data["yokaiList"]))]
combo_yokai = ttk.Combobox(frame, values=yokai_names)
combo_yokai.grid(row=0, column=0, padx=(0, 10))
combo_yokai.bind("<<ComboboxSelected>>", selectionner_yokai)

# Ajouter des champs d'entrée pour les variables
variables_labels = ["Nom", "Modèle 3D", "PV", "Force", "Esprit", "Defense", "VIT", "Rang", "Tribu", "Element", "Role", "Medalium"]
variables_names = ["nom", "modele3D", "PV", "Force", "Esprit", "Defense", "VIT", "Rang", "Tribu", "Element", "role", "Medalium"]

for i, label in enumerate(variables_labels):
    ttk.Label(frame, text=label + ":").grid(row=i+1, column=0, sticky=tk.W)
    entry_var = variables_values[variables_names[i]]
    entry_widget = ttk.Entry(frame, textvariable=entry_var)
    entry_widget.grid(row=i+1, column=1, padx=(0, 10))

# Bouton de modification
btn_modifier = ttk.Button(frame, text="Sauvegarder", command=lambda: modifier_yokai(combo_yokai.current()))
btn_modifier.grid(row=len(variables_labels)+1, column=0, columnspan=2, pady=(10, 0))

# Bouton d'ajout d'un nouveau Yo-kai
btn_ajouter = ttk.Button(frame, text="Nouveau Yo-kai", command=ajouter_nouveau_yokai)
btn_ajouter.grid(row=len(variables_labels)+2, column=0, columnspan=2, pady=(10, 0))

# Ajouter un cadre avec un titre et un texte à droite
titre_cadre = ttk.Label(frame, text="""Rangs
Vitesse
Roles""")
titre_cadre.grid(row=0, column=2, padx=(10, 0), pady=(0, 5), sticky=tk.W)

text_partie = """1: E
2: D
3: C
4: B
5: A
6: S



1: lent
2: normal
3: rapide



1: combattant
2: tank
3: guerisseur
4: ranger"""
label_text = ttk.Label(frame, text=text_partie, wraplength=75, anchor="n")  # Ajouter anchor="n" pour le texte en haut
label_text.grid(row=1, column=2, rowspan=len(variables_labels)+2, padx=(10, 0))

# Définir le poids des lignes et des colonnes pour le redimensionnement
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Ajouter un deuxième cadre avec un titre et un texte à droite
titre_cadre2 = ttk.Label(frame, text="""Tribus
Éléments""")
titre_cadre2.grid(row=0, column=3, padx=(10, 0), pady=(0, 5), sticky=tk.W)

text_partie2 = """1: vaillant
2: mystérieux
3: Costaud
4: Minions
5: sombre
6: sinistre
7: insaisissable
8: perfides
9 boss
10 enma
11 wandroid

1: feu
2: eau
3: foudre
4 : Terre
5: glace
6: Vent
7: vortex
8: soin"""
label_text2 = ttk.Label(frame, text=text_partie2, wraplength=150, anchor="n")
label_text2.grid(row=1, column=3, rowspan=len(variables_labels)+2, padx=(10, 0))

# Définir le poids des lignes et des colonnes pour le redimensionnement
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


# Afficher l'interface
icon_path = "icon.ico"  # Remplacez ceci par le chemin de votre icône
root.iconbitmap(default=icon_path)
root.mainloop()

