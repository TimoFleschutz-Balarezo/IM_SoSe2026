import numpy as np
from pymcdm.methods import PROMETHEE_II, TOPSIS

print("=========================================================================")
print(" LEHRSTUHL FÜR WIRTSCHAFTSINFORMATIK / DECISION SCIENCE                  ")
print(" Interaktives MCDM-Framework: AHP, TOPSIS & PROMETHEE II (Typ I - VI)   ")
print("=========================================================================\n")

# ==========================================
# 1. STRUKTURPARAMETER UND DATENEINGABE
# ==========================================
print("--- Schritt 1: Strukturdefinition ---")
n_alts = int(input("Anzahl der Alternativen (z. B. 4): "))
n_crit = int(input("Anzahl der Kriterien (z. B. 4): "))

print("\n--- Schritt 2: Kriterientypen (Optimierungsrichtung) ---")
print("Geben Sie für jedes Kriterium ein: 1 für Maximierung, -1 für Minimierung")
criteria_types = []
for j in range(n_crit):
    c_type = int(input(f"  Optimierungsrichtung für Kriterium {j+1}: "))
    if c_type not in [1, -1]:
        raise ValueError("Ungültiger Typ! Nur 1 (Max) oder -1 (Min) zulässig.")
    criteria_types = np.append(criteria_types, c_type)

print("\n--- Schritt 3: Performance-Matrix (Entscheidungsmatrix) ---")
dataset = []
for i in range(n_alts):
    print(f"  Leistungsdaten für Alternative {i+1}: ")
    row = []
    for j in range(n_crit):
        val = float(input(f"    Wert für Kriterium {j+1}: "))
        row.append(val)
    dataset.append(row)
dataset = np.array(dataset)

# ==========================================
# 2. SELEKTION DER PRÄFERENZFUNKTIONEN PRO KRITERIUM
# ==========================================
print("\n--- Schritt 4: Kriterienspezifische Konfiguration der Präferenzfunktionen ---")
print("Verfügbare mathematische Typen nach Brans & Vincke:")
print("  [1] usual    - Typ I:   Gewöhnlich (Strikter Sprung 0 auf 1, keine Schwellen)")
print("  [2] ushape   - Typ II:  U-Gestalt (Indifferenzschwelle q, danach direkt 1)")
print("  [3] vshape   - Typ III: V-Gestalt (Linearer Anstieg bis Präferenzschwelle p)")
print("  [4] level    - Typ IV:  Stufenfunktion (Diskreter Sprung bei q und p)")
print("  [5] vshape_2 - Typ V:   V-Gestalt mit Indifferenz (Linearer Anstieg zwischen q und p)")
print("  [6] gaussian - Typ VI:  Gauß-Funktion (Stetig über Standardabweichung s)")

pref_choices = []
p_parameters = np.zeros(n_crit)
q_parameters = np.zeros(n_crit)
s_parameters = np.zeros(n_crit)

for j in range(n_crit):
    print(f"\n  Konfiguration für Kriterium {j+1}:")
    choice = int(input(f"    Wählen Sie die Präferenzfunktion (1-6): "))
    if choice not in [1, 2, 3, 4, 5, 6]:
        raise ValueError("Ungültige Funktionsauswahl!")
    
    pref_choices.append(choice)
    
    # Abfrage der mathematischen Parameter je nach ausgewähltem Typ
    if choice == 2:
        q_parameters[j] = float(input("      Indifferenzschwelle 'q' eingeben: "))
    elif choice == 3:
        p_parameters[j] = float(input("      Präferenzschwelle 'p' eingeben: "))
    elif choice in [4, 5]:
        q_val = float(input("      Indifferenzschwelle 'q' eingeben: "))
        p_val = float(input("      Präferenzschwelle 'p' eingeben: "))
        if q_val >= p_val:
            raise ValueError("Mathematischer Fehler: 'q' muss strikt kleiner als 'p' sein!")
        q_parameters[j] = q_val
        p_parameters[j] = p_val
    elif choice == 6:
        s_parameters[j] = float(input("      Gauß-Parameter 's' (Standardabweichung) eingeben: "))


# MATHEMATISCHE KERN-LOGIK: Kriterienspezifische Auswertung der Differenzen
def evaluate_preference(d, criterion_idx):
    """
    Berechnet die paarweise Präferenz P(d) im Bereich [0, 1] basierend auf der 
    Wahl des Studierenden/Entscheiders für das exakte Kriterium.
    """
    fn_type = pref_choices[criterion_idx]
    q = q_parameters[criterion_idx]
    p = p_parameters[criterion_idx]
    s = s_parameters[criterion_idx]
    
    if d <= 0:
        return 0.0
        
    if fn_type == 1:    # usual
        return 1.0
        
    elif fn_type == 2:  # ushape
        return 1.0 if d > q else 0.0
        
    elif fn_type == 3:  # vshape
        return 1.0 if d > p else d / p
        
    elif fn_type == 4:  # level
        if d <= q: return 0.0
        if d > p: return 1.0
        return 0.5
        
    elif fn_type == 5:  # vshape_2 (Linear mit Indifferenz)
        if d <= q: return 0.0
        if d > p: return 1.0
        return (d - q) / (p - q)
        
    elif fn_type == 6:  # gaussian
        return 1.0 - np.exp(-(d**2) / (2 * (s**2)))
        
    return 0.0

# ==========================================
# 3. GEWICHTUNG VIA AHP
# ==========================================
print("\n--- Schritt 5: Kriterien-Gewichtung via AHP ---")
print("Geben Sie die relativen Präferenzen der oberen Dreiecksmatrix ein (Skala nach Saaty 1-9).")
ahp_matrix = np.ones((n_crit, n_crit))

for i in range(n_crit):
    for j in range(i + 1, n_crit):
        val = float(input(f"  Präferenz von Kriterium {i+1} relativ zu Kriterium {j+1} (z.B. 3 oder 0.33): "))
        ahp_matrix[i, j] = val
        ahp_matrix[j, i] = 1.0 / val

# Berechnung des Prioritätenvektors via geometrischem Mittelwert
row_geometric_mean = np.prod(ahp_matrix, axis=1) ** (1.0 / n_crit)
erp_weights = row_geometric_mean / np.sum(row_geometric_mean)

# AHP-Konsistenzprüfung
ri_dict = {1: 0.0, 2: 0.0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24}
total_sum = np.sum(ahp_matrix, axis=0)
lambda_max = np.sum(total_sum * erp_weights)
ci = (lambda_max - n_crit) / (n_crit - 1) if n_crit > 1 else 0
ri = ri_dict.get(n_crit, 1.32)
cr = ci / ri if ri > 0 else 0

print(f"\nBerechnete Kriteriengewichte (AHP): {np.round(erp_weights, 4)}")
print(f"Consistency Ratio (CR): {round(cr, 4)} -> " + ("KONSISTENT" if cr < 0.1 else "INKONSISTENT!"))

# ==========================================
# 4. MULTI-CRITERIA ANALYSIS & RANKING
# ==========================================
print("\n=========================================================================")
print(" ANALYSEERGEBNISSE ")
print("=========================================================================")

# Mathematischer Neubau des PROMETHEE II Outrankings zur Umgehung von Bibliotheks-Restriktionen
n_alternatives = dataset.shape[0]
aggregated_preferences = np.zeros((n_alternatives, n_alternatives))

for i in range(n_alternatives):
    for k in range(n_alternatives):
        if i == k: 
            continue
        pi_ik = 0
        for j in range(n_crit):
            # Bestimmung der gerichteten Differenz anhand der Optimierungsrichtung
            if criteria_types[j] == 1:
                diff = dataset[i, j] - dataset[k, j]
            else:
                diff = dataset[k, j] - dataset[i, j]
            
            # Berechnung des gewichteten Präferenzwertes
            pi_ik += erp_weights[j] * evaluate_preference(diff, j)
        aggregated_preferences[i, k] = pi_ik
        
# Berechnung der Netto-Flüsse: Phi = Phi+ (Leaving) - Phi- (Entering)
leaving_flows = np.sum(aggregated_preferences, axis=1) / (n_alternatives - 1)
entering_flows = np.sum(aggregated_preferences, axis=0) / (n_alternatives - 1)
flows = leaving_flows - entering_flows

ranking_promethee = np.argsort(-flows) + 1

# TOPSIS als methodische Kontrollinstanz (Distanzanalyse)
topsis = TOPSIS()
topsis_scores = topsis(dataset, erp_weights, criteria_types)
ranking_topsis = np.argsort(-topsis_scores) + 1

# Ergebnisausgabe
print(f"PROMETHEE II Netto-Flüsse (Phi): {np.round(flows, 4)}")
print(f"PROMETHEE II Ranking:            {ranking_promethee}")
print(f"TOPSIS Scores:                   {np.round(topsis_scores, 4)}")
print(f"TOPSIS Ranking:                  {ranking_topsis}\n")

# Komparatives Fazit für die Lehrveranstaltung
if np.array_equal(ranking_topsis, ranking_promethee):
    print("Fazit: Strukturelle Konvergenz. Beide MCDM-Ansätze führen trotz grundlegend")
    print("       verschiedener mathematischer Operationen zum exakt selben Ergebnis.")
else:
    print("Fazit: DIVERGENZ! Die explizite Modellierung von Schwellenwerten (p, q) in")
    print("       PROMETHEE II fängt relationale Präferenzen anders auf als der globale,")
    print("       kompensatorische euklidische Abstand von TOPSIS.")