import matplotlib.pyplot as plt
import numpy as np

print("=" * 65)
print("IT-DECISION SUPPORT SYSTEM (DSS) - PROSPECT THEORY ANALYSIS")
print("=" * 65)
print(
    "Hinweis: Druecken Sie einfach [ENTER], um die wissenschaftlichen Standardwerte zu nutzen.\n"
)

# =====================================================================
# 1. INTERAKTIVE PARAMETERABFRAGE (MIT VORBELEGUNG)
# =====================================================================
try:
    #ALPHA = float(
    #    input("Parameter ALPHA fuer Gewinne (Konkavitaet) (z.B. 0.5): ")
    #    or 0.88
    #)
    #BETA = float(
    #    input("Parameter BETA fuer Verluste (Konvexitaet) (z.B. 0.5): ")
    #    or 0.88
    #)
    #LAMBDA = float(
    #    input("Parameter LAMBDA fuer Verlustaversion (z.B. 2.25): ")
    #    or 2.25
    #)

    print("\n--- Definition des IT-Projekts / Option A ---")
    out_a = input("Ergebnisse Option A in k EUR (kommagetrennt, z.B. 100 oder 100, 200): ")
    outcomes_a = np.array([float(x) for x in out_a.split(",")])
    prob_a = input(
        "Wahrscheinlichkeiten Option A (kommagetrennt, z.B. 1.0 oder 0.5, 0.5): "
    )
    probs_a = np.array([float(x) for x in prob_a.split(",")])

    print("\n--- Definition des IT-Projekts / Option B ---")
    out_b = input(
        "Ergebnisse Option B in k EUR (kommagetrennt,z.B. 100 oder 100, 200): "
    )
    outcomes_b = np.array([float(x) for x in out_b.split(",")])
    prob_b = input(
        "Wahrscheinlichkeiten Option B (kommagetrennt, z.B. 1.0 oder 0.5, 0.5): "
    )
    probs_b = np.array([float(x) for x in prob_b.split(",")])

    # Validierung der stochastischen Grundlagen
    if not (
        np.isclose(np.sum(probs_a), 1.0) and np.isclose(np.sum(probs_b), 1.0)
    ):
        print(
            "\n[WARNUNG]: Die Summe der Wahrscheinlichkeiten muss pro Option 1.0 ergeben!"
        )

except ValueError:
    print(
        "\n[FEHLER]: Ungueltige Eingabe. Bitte nutzen Sie ausschliesslich numerische Werte z.B. 1.0 und nicht 1,0."
    )
    exit()


# =====================================================================
# 2. MATHEMATISCHE EVALUATIONSFUNKTIONEN
# =====================================================================
def prospect_value(x):
    """Berechnet den subjektiven Wert v(x) nach der exponentiellen Wertfunktion (Fallstudie 2)."""
    gamma = 0.05
    
    # Exponentieller Gewinnpfad (x >= 0)
    gains_clean = 0.5 * (1 - np.exp(-gamma * x))
    
    # Exponentieller Verlustpfad (x < 0)
    losses_clean = -(1 - np.exp(gamma * x))
    
    return np.where(x >= 0, gains_clean, losses_clean)


# Berechnung der normativen und deskriptiven Kennzahlen
ev_a = np.sum(outcomes_a * probs_a)
ev_b = np.sum(outcomes_b * probs_b)

v_a = np.sum(prospect_value(outcomes_a) * probs_a)
v_b = np.sum(prospect_value(outcomes_b) * probs_b)

# Analytische Konsolenausgabe
print("\n" + "=" * 65)
print("ANALYSE-ERGEBNISSE (Kardinalskalierte Metriken)")
print("=" * 65)
print(
    f"Option A -> Erwartungswert (EV): {ev_a:6.1f}k EUR | Psychologischer PT-Wert (V): {v_a:5.2f}"
)
print(
    f"Option B -> Erwartungswert (EV): {ev_b:6.1f}k EUR | Psychologischer PT-Wert (V): {v_b:5.2f}"
)
print("-" * 65)
if v_a > v_b:
    print("Menschliche Entscheidungsempfehlung: OPTION A bevorzugen.")
elif v_b > v_a:
    print("Menschliche Entscheidungsempfehlung: OPTION B bevorzugen.")
else:
    print(
        "Menschliche Entscheidungsempfehlung: Indifferenz zwischen beiden Optionen."
    )
print("=" * 65)

# =====================================================================
# 3. GRAPHICAL PLOTTING (Symmetrisches & Synchronisiertes Layout)
# =====================================================================
all_outcomes = np.concatenate([outcomes_a, outcomes_b])
max_val = max(np.max(np.abs(all_outcomes)) * 1.2, 50)
x_axis = np.linspace(-max_val, max_val, 500)
y_axis = prospect_value(x_axis)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Subplot 1: Die verhaltensbarometrische S-Kurve
ax1.plot(x_axis, y_axis, color='navy', label="Subjektive Wertfunktion v(x)", linewidth=2)
ax1.axhline(0, color='black', linestyle='--', linewidth=0.8)
ax1.axvline(0, color='black', linestyle='--', linewidth=0.8)
ax1.scatter(outcomes_a, prospect_value(outcomes_a), color='green', s=120, zorder=5, label="Komponenten Option A")
ax1.scatter(outcomes_b, prospect_value(outcomes_b), color='crimson', s=120, zorder=5, label="Komponenten Option B")
ax1.set_title("Position der Projektausgaenge auf der S-Kurve", fontsize=10, fontweight='bold')
ax1.set_xlabel("Objektiver Ausgang (x in k EUR)", fontsize=9)
ax1.set_ylabel("Subjektiver Wert v(x)", fontsize=9)
ax1.grid(True, alpha=0.3)
ax1.legend(loc="upper left")

# Subplot 2: Aggregierter Vergleich (Inklusive Wahrscheinlichkeiten)
labels = ['Option A', 'Option B']
ev_values = [ev_a, ev_b]
v_values = [v_a, v_b]

x = np.arange(len(labels))
width = 0.35

ax2.bar(x - width/2, ev_values, width, label='Erwartungswert (EV in k EUR)', color='teal')
ax2_twin = ax2.twinx()
ax2_twin.bar(x + width/2, v_values, width, label='Prospect-Wert (V)', color='orange')

# Mathematische Synchronisation der dualen Y-Achsen
min_ev, max_ev = min(ev_values), max(ev_values)
min_v, max_v = min(v_values), max(v_values)

if min_ev >= 0 and min_v >= 0:
    ax2.set_ylim(0, max(50, max_ev * 1.2))
    ax2_twin.set_ylim(0, max(1, max_v * 1.2))
    loc_leg = 'upper center'
elif max_ev <= 0 and max_v <= 0:
    ax2.set_ylim(min_ev * 1.2, 0)
    ax2_twin.set_ylim(min_v * 1.2, 0)
    loc_leg = 'lower center'
else:
    bound_ev = max(abs(min_ev), abs(max_ev)) * 1.2
    bound_v = max(abs(min_v), abs(max_v)) * 1.2
    ax2.set_ylim(-bound_ev, bound_ev)
    ax2_twin.set_ylim(-bound_v, bound_v)
    loc_leg = 'upper center'

# Gemeinsame solide schwarze Nullachse einziehen
ax2.axhline(0, color='black', linestyle='-', linewidth=1.0, zorder=3)

ax2.set_ylabel('Objektiver Erwartungswert (k EUR)', color='teal')
ax2_twin.set_ylabel('Subjektiver Gesamtwert (V)', color='orange')
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.set_title("Aggregierter Management-Vergleich", fontsize=10, fontweight='bold')

lines, labels_l = ax2.get_legend_handles_labels()
lines2, labels_l2 = ax2_twin.get_legend_handles_labels()
ax2.legend(lines + lines2, labels_l + labels_l2, loc=loc_leg)

plt.suptitle(f"IT-Decision Support System (Prospect Theory Analysis)", fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()