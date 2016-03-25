# XXXXings-Trinkspiel

Aktuellere Version möglicherweise auf "dem" Etherpad.

## 1. Spielfeld

Das Spielfeld ist in der Form einer liegenden Acht angeordnet, dies symbolisiert das endlose Spiel.

Auf der Linie der liegenden Acht befinden sich insgesamt 32 markierte Felder.

Diese Felder können Leer, Aktionsfelder, Alkoholfelder, Regelfelder oder fest vorgegebene Felder sein.

Die Karten, die auf diesen Feldern gezogen werden müssen, werden von den Teilnehmern selbst eingereicht. Dies geschieht anonym.

Die Beispiele, die in den Feldarten im Folgenden angegeben werden, sind als Grundbestand Teil des Spiels.

## 2. Regeln

- Auf Aktions-, Alkohol- oder Regel-Feldern muss eine Karte vom entsprechenden Stapel gezogen werden. Auf den fest vorgegebenen Feldern muss die entsprechende Aktion ausgeführt werden.

- Falls sich eine Karte während des Spiels als nicht annehmbar herausstellt, kann die Gruppe als gemeinsames Gremium diese Karte ablehnen. Wenn das passiert, wird eine neue Karte vom selben Stapel gezogen.

- Falls bei einer Karte als Strafe Alkohol getrunken werden soll, gibt es genau zwei Mengen: Die "große Strafe" und die "kleine Strafe". Die genaue Trinkmenge der beiden Strafen werden vor jedem Spiel individuell festgesetzt. (z.B. ein Schluck/zwei Schluck)

- Bei allen Karten gilt: Betroffene der Karte dürfen nicht zu spezifisch ausgewählt werden (z.B. Vornamen)

- Es gilt: Pro Rundlauf kann ein Zug ausgesetzt werden. Die Anzahl der Züge, die ausgesetzt werden kann, addiert sich nicht auf. (Man hat also immer nur maximal einen Zug, den man aussetzen kann.)

## 3. Kartenarten

#### 3.1 Aktionskarten:
- Einmalige Aktion der Gruppe / einem Teil der Gruppe / eines Einzelnen.
- Karten dürfen den weiteren Verlauf des Spiels nicht ändern. 
- Die von der Aktion Betroffenen müssen die Aktion versuchen.
- Es existiert keine Strafe (außer bei Nichtversuchen/Verweigern der Spielaustritt.)
- Witzigkeit der Karten wird bevorzugt :)
- Requisiten, die zum Erledigen der Aktion benötigt werden, können/sollen mitgebracht werden.
    
    
######Exemplarische Beispiele:
- Jeder der schon mal einen Popel gegessen hat muss sich outen.
- Jeder muss drei Tropfen Maggi trinken. (Requisiten in dem Fall: Maggi)
- Jeder muss an der Achsel seines linken Nachbarn riechen.
- Alle Frauen müssen sich der Körbchengröße nach aufstellen.
- Der Jüngste muss eine peinliche Geschichte erzählen.
    
#### 3.2 Alkoholkarten
Die Karte beschreibt eine Möglichkeit, einen Teil der Gruppe zu wählen, der bestraft wird.
Die Karte beschreibt wie die zu trinkende Menge "berechnet" wird.
    
######Exemplarische Beispiele:
- Derjenige, der am wenigsten Münzen dabei hat, muss trinken.
- Wikingerboxen! Wer aufgibt muss trinken.
- Es müssen der Reihe nach zu gegebenen Bundesländern die Hauptstädte genannt werden. Bei Fehlern muss getrunken werden und der Nächste ist mit dem gleichen Land dran, bis alle Länder durch sind. (Requisiten in dem Fall: Liste mit Bundesländern/Hauptstädten)
- Alle Pärchen müssen aus dem Getränk des Partners trinken.
    
#### 3.3 Regelkarten
 Neue "Regeln" werden eingeführt; die Strafe bei Verstoß ist jeweils trinken. 
 Die Grundregeln des Spiels dürfen nicht geändert werden. Die Regeln sind zeitlich begrenzt (z.B. 15 Minuten - Dies wird vor Spielbeginn festgelegt.) Es gibt immer nur zwei Regeln. Wenn bereits zwei Regeln aktiv sind wird keine neue Regelkarte gezogen. Der Zug ist dann ereignislos.
    
######Exemplarische Beispiele:
- Jeder darf nur noch mit "Mc Lovin" angesprochen werden.
- Wenn der Kartenzieher seine Stirn berührt, müssen alle "Muh" sagen.
- Fluchen ist verboten.
- Jeder Satz muss vor seinem ersten Substantiv einen Fluch beinhalten.

## 4. Feste Aktionen auf dem Spielfeld

Folgende Aktionen sind bereits fest auf dem Spielfeld verankert:

- Einen Schluck trinken.
- Zwei Schluck trinken.
- Eine Runde aussetzen.
- Zwei Runden aussetzen.
- (Felix-Regel) Erzähle eine Witz. Wenn keiner lacht, trink!
- (XXXXing-Regel) Der Älteste trinkt.
- Der Jüngste trinkt.
- (Mehrheitsentschluss) Die Gruppe entscheidet per Mehrheitsvotum, wer trinkt.
    
## 5. Spielfeld

Es gibt 32 Felder.
Davon
- 14 leere,
- 8 fest vorgegebene,
- 4 Aktions-,
- 4 Alkohol-, und
- 2 Regelfelder
        
## 6. Beteiligung

Die Mitspieler müssen jeweils eigene Aktions-, Alkohol- und Regelkarten mitbringen.
Zur Teilnahme am Spiel muss man mindestens 
- 6 Aktions-,
- 6 Alkohol-,
- 3 Regelkarten

mitbringen.

Die Karten werden mittels PGP-Public-Key verschlüsselt. Der Spiele-Master besitzt den entsprechenden Private-Key, und soll diesen dann im Vorfeld des Spiels benutzen um die Dateien zu entschlüsseln und die Spielekarten herzustellen. 

Jede Karte soll **einzeln** als **reine Textdatei** erstellt und verschlüsselt werden, sodass die Weiterverarbeitung möglichst einfach automatisiert werden kann. Der jeweilige Dateiname ist egal; er sollte jedoch im Repo möglicht einmalig sein (modulo Groß/Kleinschreibung wegen Windows). 

Die Dateien sollen mit dem Public-Keys verschlüsselt und danach in den entsprechenden Ordnern abgelegt werden. 

Dann sollte ein Pull-Request gestellt werden.

## 7. Spielevorbereitung

Die Karten müssen im Vornherein beim Spielmaster eingereicht werden. Dieser druckt die Karten aus und stellt so sicher, dass die Attributierung der Karten nicht möglich ist.
Der Spielmaster versucht nach besten Kräften sich keine der Karten (außer seine Eigenen) vor dem Spiel anzuschauen, und die Anonymität der Karten zu wahren.

Vor dem Spiel müssen folgende Parameter im Zensus festgelegt werden:
- Höhe der "großen Strafe" und der "kleinen Strafe"
- Dauer der Regelfelder