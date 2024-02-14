"""
 Pour réaliser les améliorations,
 j'ai fais le choix de ne plus afficher  chacun des 10 trajets
 mais de simplement calculer les métriques demandées.
"""
import numpy as np
import pandas

explorer_df = pandas.read_csv("./parcours_explorateurs.csv")

# préparation des données données dans la correction
array_starting_node = explorer_df[explorer_df["type_aretes"]
                                  == "depart"]["noeud_amont"].values
array_arrival_node = explorer_df[explorer_df["type_aretes"]
                                 == "arrivee"]["noeud_aval"].values
dict_upstream_downstream = {
    row["noeud_amont"]: row["noeud_aval"] for _, row in explorer_df.iterrows()}
# ajoute la distance dans le dictionnaire
dict_node_distance = {row["noeud_amont"]: row["distance"]
                      for _, row in explorer_df.iterrows()}

paths_lengths = []

# ici on calcul des longueurs des chemins de chaque explorateur
for starting_node in array_starting_node:
    current_path = [starting_node]
    total_distance = 0

    while current_path[-1] not in array_arrival_node:
        current_node = current_path[-1]
        next_node = dict_upstream_downstream[current_node]
        total_distance += dict_node_distance[current_node]
        current_path.append(next_node)

    paths_lengths.append(total_distance)

"""
on utilise max() & min() pour trouver le chemin le plus long et le plus court
et on utilise numpy pour les autres métriques
"""
max_length = max(paths_lengths)
min_length = min(paths_lengths)
mean_length = np.mean(paths_lengths)
median_length = np.median(paths_lengths)
std_deviation = np.std(paths_lengths)
interquartile_range = np.percentile(
    paths_lengths, 75) - np.percentile(paths_lengths, 25)

# on affiche !
print(f"Chemin le plus long: {max_length} Km")
print(f"Chemin le plus court: {min_length} Km")
print(f"Moyenne des longueurs: {mean_length} Km")
print(f"Médiane des longueurs: {median_length}")
print(f"Écart-type des longueurs: {std_deviation}")
print(f"Écart-interquartile des longueurs: {interquartile_range}")

# Sofiane :)
