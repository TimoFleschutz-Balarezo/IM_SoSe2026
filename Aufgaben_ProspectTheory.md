Pyhtonumgebung vorbereiten:
➜  IM_SoSe2026 git:(main) ✗ python3 -m venv .venv
➜  IM_SoSe2026 git:(main) ✗ source .venv/bin/activate
(.venv) ➜  IM_SoSe2026 git:(main) ✗ pip install numpy
(.venv) ➜  IM_SoSe2026 git:(main) ✗ pip install matplotlib

**Übung 1, Frage 1**
Nutzung des vorgebenen Codes DSS_ProspectTheory.py mit den Parametern
Alpha = Beta = 0.5
Lambda = 2.0
BudgetA = 50 (für 50Tsd€)€)
BudgetB = -50 (für -50Tsd€)
Wahrscheinlichkeiten = 1

=================================================================
IT-DECISION SUPPORT SYSTEM (DSS) - PROSPECT THEORY ANALYSIS
=================================================================
Hinweis: Druecken Sie einfach [ENTER], um die wissenschaftlichen Standardwerte zu nutzen.

Parameter ALPHA fuer Gewinne (Konkavitaet) (z.B. 0.5): 0.5
Parameter BETA fuer Verluste (Konvexitaet) (z.B. 0.5): 0.5
Parameter LAMBDA fuer Verlustaversion (z.B. 2.25): 2

--- Definition des IT-Projekts / Option A ---
Ergebnisse Option A in k EUR (kommagetrennt, z.B. 100 oder 100, 200): 50
Wahrscheinlichkeiten Option A (kommagetrennt, z.B. 1.0 oder 0.5, 0.5): 1

--- Definition des IT-Projekts / Option B ---
Ergebnisse Option B in k EUR (kommagetrennt,z.B. 100 oder 100, 200): -50
Wahrscheinlichkeiten Option B (kommagetrennt, z.B. 1.0 oder 0.5, 0.5): 1

=================================================================
ANALYSE-ERGEBNISSE (Kardinalskalierte Metriken)
=================================================================
Option A -> Erwartungswert (EV):   50.0k EUR | Psychologischer PT-Wert (V):  7.07
Option B -> Erwartungswert (EV):  -50.0k EUR | Psychologischer PT-Wert (V): -14.14
-----------------------------------------------------------------
Menschliche Entscheidungsempfehlung: OPTION A bevorzugen.
=================================================================

*Ergebnis für den Gesamtwert = 7.07 + (-14.14) = -7.07*

(Bei Verwendung der Werte 50000 und -50000 ergibt sich -223,6.)

**Übung 1, Frage 2**
Nutzung des vorgebenen Codes DSS_ProspectTheory.py mit den Parametern
Alpha = Beta = 0.5
Lambda = 2.0
BudgetA = -100,0
WahrscheinlichkeitA = 0.5,0.5
BudgetB = -50
WahrscheinlichkeitenB = 1

=================================================================
IT-DECISION SUPPORT SYSTEM (DSS) - PROSPECT THEORY ANALYSIS
=================================================================
Hinweis: Druecken Sie einfach [ENTER], um die wissenschaftlichen Standardwerte zu nutzen.

Parameter ALPHA fuer Gewinne (Konkavitaet) (z.B. 0.5): 0.5
Parameter BETA fuer Verluste (Konvexitaet) (z.B. 0.5): 0.5
Parameter LAMBDA fuer Verlustaversion (z.B. 2.25): 2

--- Definition des IT-Projekts / Option A ---
Ergebnisse Option A in k EUR (kommagetrennt, z.B. 100 oder 100, 200): -100,0
Wahrscheinlichkeiten Option A (kommagetrennt, z.B. 1.0 oder 0.5, 0.5): 0.5,0.5

--- Definition des IT-Projekts / Option B ---
Ergebnisse Option B in k EUR (kommagetrennt,z.B. 100 oder 100, 200): -50
Wahrscheinlichkeiten Option B (kommagetrennt, z.B. 1.0 oder 0.5, 0.5): 1

=================================================================
ANALYSE-ERGEBNISSE (Kardinalskalierte Metriken)
=================================================================
Option A -> Erwartungswert (EV):  -50.0k EUR | Psychologischer PT-Wert (V): -10.00
Option B -> Erwartungswert (EV):  -50.0k EUR | Psychologischer PT-Wert (V): -14.14
-----------------------------------------------------------------
Menschliche Entscheidungsempfehlung: OPTION A bevorzugen.
=================================================================

*Richtige Antwort:*
Der Wert der riskanten Wette (V = -10.0) ist höher (weniger negativ) als der des sicheren Verlusts (v = -14.14). Der IT-Leiter führt das riskante Projekt fort (Risikofreude im Verlustbereich).

**Übung 2, Frage 1**

Anpassung Pyhton-Code für exponentielle Wertfunktion (DSS_ProspectTheory_2.py)

Durchführung mit Gesamtendvermögen:
BudgetA = 9,15
WahrscheinlichkeitA = 0.5,0.5
BudgetB = 2,40
WahrscheinlichkeitenB = 0.5,0.5

=================================================================
ANALYSE-ERGEBNISSE (Kardinalskalierte Metriken)
=================================================================
Option A -> Erwartungswert (EV):   12.0k EUR | Psychologischer PT-Wert (V):  0.22
Option B -> Erwartungswert (EV):   21.0k EUR | Psychologischer PT-Wert (V):  0.24
-----------------------------------------------------------------
Menschliche Entscheidungsempfehlung: OPTION B bevorzugen.
=================================================================

Durchführung mit Referenzpunkt und Betrachtung der Gewinne/Verluste:
BudgetA = -1,5
WahrscheinlichkeitA = 0.5,0.5
BudgetB = -8,30
WahrscheinlichkeitenB = 0.5,0.5

=================================================================
ANALYSE-ERGEBNISSE (Kardinalskalierte Metriken)
=================================================================
Option A -> Erwartungswert (EV):    2.0k EUR | Psychologischer PT-Wert (V):  0.03
Option B -> Erwartungswert (EV):   11.0k EUR | Psychologischer PT-Wert (V):  0.03
-----------------------------------------------------------------
Menschliche Entscheidungsempfehlung: OPTION A bevorzugen.
=================================================================

*Richtige Antwort:*
Endvermögen: Strategie A2 | Referenzpunkt: Strategie A1

**Übung 3, Frage 1**
Nutzung des vorgebenen Codes DSS_ProspectTheory.py mit den Parametern
Alpha = Beta = 0.88
Lambda = 2.25

Annahme der Wahrscheinlichkeiten von 0.5 für Erfolg und Misserfolg

BudgetA = 0,5
WahrscheinlichkeitA = 0.5,0.5
BudgetB = 0,-5
WahrscheinlichkeitenB = 0.5,0.5

=================================================================
ANALYSE-ERGEBNISSE (Kardinalskalierte Metriken)
=================================================================
Option A -> Erwartungswert (EV):    2.5k EUR | Psychologischer PT-Wert (V):  2.06
Option B -> Erwartungswert (EV):   -2.5k EUR | Psychologischer PT-Wert (V): -4.64
-----------------------------------------------------------------
Menschliche Entscheidungsempfehlung: OPTION A bevorzugen.
=================================================================

*Richtige Antwort:*
Bei Variante 2, da die Streichung eines bereits zugeteilten Bonus als schmerzhafter Verlust codiert wird (Verlustaversion) und Menschen höhere Anstrengungen unternehmen, um Verluste zu vermeiden.


**Übung 4, Frage 1**
Nutzung des vorgebenen Codes DSS_ProspectTheory.py mit den Parametern
Alpha = Beta = 0.88
Lambda = 2.25
BudgetA = 100,40,0
WahrscheinlichkeitA = 0.4,0.1,0.5
BudgetB = 40,40,0
WahrscheinlichkeitenB = 0.4,0.1,0.5

=================================================================
ANALYSE-ERGEBNISSE (Kardinalskalierte Metriken)
=================================================================
Option A -> Erwartungswert (EV):   44.0k EUR | Psychologischer PT-Wert (V): 25.59
Option B -> Erwartungswert (EV):   20.0k EUR | Psychologischer PT-Wert (V): 12.85
-----------------------------------------------------------------
Menschliche Entscheidungsempfehlung: OPTION A bevorzugen.
=================================================================

Anpassung des Codes auf eine vereinfachte, verzerrte Gewichtungsfunktion aus dem Paper von Kahnemann und Tversky (DSS_ProspectTheory_4.py)

Bei Nutzung der obingen Parameter:
=================================================================
ANALYSE-ERGEBNISSE (Kardinalskalierte Metriken)
=================================================================
Option A -> Erwartungswert (EV):   44.0k EUR | Psychologischer PT-Wert (V):  7.93
Option B -> Erwartungswert (EV):   20.0k EUR | Psychologischer PT-Wert (V):  4.11
-----------------------------------------------------------------
Menschliche Entscheidungsempfehlung: OPTION A bevorzugen.
=================================================================

Bei Anpassung der Paramater (Zusammenfassung der Wahrscheinlichkeiten für A2 = 40)
Alpha = Beta = 0.88
Lambda = 2.25
BudgetA = 100,40,0
WahrscheinlichkeitA = 0.4,0.1,0.5
BudgetB = 40,0
WahrscheinlichkeitenB = 0.5,0.5

=================================================================
ANALYSE-ERGEBNISSE (Kardinalskalierte Metriken)
=================================================================
Option A -> Erwartungswert (EV):   44.0k EUR | Psychologischer PT-Wert (V):  7.93
Option B -> Erwartungswert (EV):   20.0k EUR | Psychologischer PT-Wert (V): 11.56
-----------------------------------------------------------------
Menschliche Entscheidungsempfehlung: OPTION B bevorzugen.
=================================================================


*Nachweis der stochastischen Dominanz von Alternative A1*

Betrachtung der Bereich  >100, 40-100, 0-40 und >0
P(A1>100)=0
P(A2>100)=0

P(100=>A1>40)=0.4
P(100=>A2>40)=0
P(A1) > P(A2)

P(40=>A1>0)=P(A1=40) + P(A1=100) = 0.1 + 0.4 = 0.5
P(40=>A2>0)=P(A2=40) = 0.1 + 0.4 = 0.5
P(A1) = P(A2)

P(A1=>0)=1
P(A2=>0)=1
P(A1) = P(A2)

*Richtige Antwort:*
Ja, Anbieter A1 dominiert Anbieter A2 im Sinne der stochastischen Dominanz erster Ordnung (Wahrscheinlichkeitsdominanz), da die kumulierten Wahrscheinlichkeiten für das Erreichen eines Mindestwertes bei A1 immer gleich oder höher sind.