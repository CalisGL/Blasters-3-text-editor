import tkinter as tk
from tkinter import ttk
import json
from ttkthemes import ThemedTk

def sauvegarder():
    # Sauvegarder les données modifiées dans le fichier JSON
    with open("dialogues.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def modifier_yokai(index):
    if index >= 0 and index < len(data["dialogueList"]):
        yokai = data["dialogueList"][index]
        ancien_nom = yokai["ID"]  # Sauvegarder l'ancien nom
        
        # Convertir la nouvelle ID en entier
        new_id = int(variables_values["ID"].get())
        yokai["ID"] = new_id
        sauvegarder()

        # Mettre à jour les noms dans le menu déroulant
        yokai_names[index] = format_yokai_name(index)
        combo_yokai['values'] = yokai_names

        # Sélectionner le Yo-kai avec le nouveau nom
        combo_yokai.set(format_yokai_name(index))
        yokai["fr"] = variables_values["fr"].get()
        yokai["en"] = variables_values["en"].get()
        sauvegarder()
    else:
        print("Index invalide : ", index)

def selectionner_yokai(event):
    index = combo_yokai.current()
    if index >= 0 and index < len(yokai_names):
        # Mettre à jour les variables tkinter avec les valeurs du Yo-kai sélectionné
        yokai = data["dialogueList"][index]
        variables_values["ID"].set(str(yokai["ID"]))
        variables_values["fr"].set(yokai["fr"])
        variables_values["en"].set(yokai["en"])
        variables_values["nomFR"].set(yokai["nomFR"])
        variables_values["nomEN"].set(yokai["nomEN"])

def ajouter_nouveau_yokai():
    # Ajouter un nouveau Yo-kai avec des valeurs par défaut à 0
    nouveau_yokai = {
        "ID": 0,
        "fr": "français",
        "en": "anglais",
        "nomFR": "Nom Français",
        "nomEN": "Nom Anglais"
    }
    data["dialogueList"].append(nouveau_yokai)

    # Mettre à jour la liste déroulante
    global yokai_names  # Utiliser la variable globale yokai_names
    yokai_names = [format_yokai_name(i) for i in range(len(data["dialogueList"]))]
    combo_yokai['values'] = yokai_names

    # Sélectionner le nouveau Yo-kai
    combo_yokai.current(len(data["dialogueList"]) - 1)

# Créer et afficher l'interface avec le thème ttkthemes
root = ThemedTk(theme="plastik")  # Choisissez le thème que vous préférez
root.title("YKWB3 Éditeur de textes")

# Charger les données JSON
with open("dialogues.json", encoding="utf-8") as f:
    data = json.load(f)

# Déclaration des variables globales
variables_values = {
    "ID": tk.StringVar(value=""),
    "fr": tk.StringVar(value=""),
    "en": tk.StringVar(value=""),
    "nomFR": tk.StringVar(value=""),
    "nomEN": tk.StringVar(value=""),
}

# Créer un frame
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Créer un menu déroulant pour sélectionner le Yo-kai
def format_yokai_name(index):
    yokai = data["dialogueList"][index]
    return f"{yokai['ID']} - {yokai['fr']}"

yokai_names = [format_yokai_name(i) for i in range(len(data["dialogueList"]))]
combo_yokai = ttk.Combobox(frame, values=yokai_names)
combo_yokai.grid(row=0, column=0, padx=(0, 10))
combo_yokai.bind("<<ComboboxSelected>>", selectionner_yokai)

# Ajouter des champs d'entrée pour les variables
variables_labels = ["ID", "Français", "Anglais", "Nom Français", "Nom Anglais"]
variables_names = ["ID", "fr", "en", "nomFR", "nomEN"]

for i, label in enumerate(variables_labels):
    ttk.Label(frame, text=label + ":").grid(row=i+1, column=0, sticky=tk.W)
    entry_var = variables_values[variables_names[i]]
    entry_widget = ttk.Entry(frame, textvariable=entry_var)
    entry_widget.grid(row=i+1, column=1, padx=(0, 10))

# Bouton de modification
btn_modifier = ttk.Button(frame, text="Sauvegarder", command=lambda: modifier_yokai(combo_yokai.current()))
btn_modifier.grid(row=len(variables_labels)+1, column=0, columnspan=2, pady=(10, 0))

# Bouton d'ajout d'un nouveau Yo-kai
btn_ajouter = ttk.Button(frame, text="Nouveau dialogue", command=ajouter_nouveau_yokai)
btn_ajouter.grid(row=len(variables_labels)+2, column=0, columnspan=2, pady=(10, 0))




# Afficher l'interface
icon_path = "icon.ico"  # Remplacez ceci par le chemin de votre icône
root.iconbitmap(default=icon_path)
root.mainloop()

