# Excel Web Interface

**Beschreibung:**  
Dies ist eine Python-Webanwendung, die es ermöglicht, Excel-Listen aus der Datei `data/data.xlsx` zu verwalten. Die Benutzer können:

*   Zeilen und Spalten filtern (nach True/False filtern)
*   Daten hinzufügen
*   Daten live bearbeiten
*   Leere Zeilen werden automatisch ausgeblendet.

Die Änderungen in der Excel-Datei werden bei jedem Seitenladen aktualisiert und gespeichert.

## Voraussetzungen:

*   Python 3.x: Installieren Sie Python, falls noch nicht vorhanden.
*   Abhängigkeiten: Flask, Pandas, Openpyxl. Die notwendigen Abhängigkeiten werden in der Datei `requirements.txt` aufgelistet.

## Installation:

### 1\. Automatische Installation der Abhängigkeiten und Start der Anwendung:

Es gibt zwei Optionen, um die Anwendung zu starten – abhängig vom Betriebssystem.

*   **Windows:**  
    Doppelklicken Sie auf die Datei `run.bat`. Dies wird die Installation der Abhängigkeiten über `requirements.txt` sicherstellen und die Anwendung starten.
*   **Linux/macOS:**  
    Öffnen Sie das Terminal und führen Sie den folgenden Befehl aus:  
    
    ```
    ./run.sh
    ```
    

### 2\. Manuelle Installation der Abhängigkeiten:

Falls die automatische Installation fehlschlägt, können die Abhängigkeiten manuell installiert werden. Installieren Sie alle erforderlichen Pakete, indem Sie den folgenden Befehl ausführen:

```
pip install -r requirements.txt
```

### 3\. Start der Anwendung (manuell):

Um die Anwendung manuell zu starten, führen Sie den folgenden Befehl im Terminal (oder in der Eingabeaufforderung) aus:

```
python3 app.py
```

Sobald die Anwendung gestartet ist, können Sie darauf über [http://127.0.0.1:5000](http://127.0.0.1:5000) zugreifen.

## Nutzung:

### 1\. Filtern von Zeilen und Spalten:

*   **Zeilenfilter:** Sie können Zeilen basierend auf bestimmten Kriterien filtern. Leere Zeilen werden automatisch ausgeblendet.
*   **Spaltenfilter:** Spalten können nach True/False-Werten gefiltert werden.

### 2\. Hinzufügen und Bearbeiten von Daten:

Neue Daten können direkt in die Excel-Datei `data/data.xlsx` hinzugefügt werden. Bestehende Daten können in der Weboberfläche live bearbeitet werden. Änderungen werden automatisch gespeichert und bei jedem Seitenladen aktualisiert.

### 3\. Datenaktualisierung:

Die Tabelle wird bei jedem Laden der Seite automatisch aktualisiert und die Daten aus der Excel-Datei neu geladen.

## Dateien und Verzeichnisse:

*   `app.py`: Hauptskript der Webanwendung.
*   `requirements.txt`: Liste der Python-Abhängigkeiten.
*   `run.bat`: Skript zum automatischen Starten der Anwendung auf Windows.
*   `run.sh`: Skript zum automatischen Starten der Anwendung auf Linux/macOS.
*   `data/data.xlsx`: Excel-Datei, die von der Webanwendung verwaltet wird.

## Fehlerbehebung:

### 1\. Port belegt:

Falls der Port 5000 bereits verwendet wird, ändern Sie die Portnummer in `app.py`, indem Sie `app.run(host="127.0.0.1", port=5000)` anpassen. Ändern Sie den Port auf eine andere verfügbare Nummer.

### 2\. Python-Pakete fehlen:

Vergewissern Sie sich, dass alle Pakete installiert sind, indem Sie den folgenden Befehl ausführen:

```
pip install -r requirements.txt
```

### 3\. Excel-Datei fehlt:

Stellen Sie sicher, dass sich die Excel-Datei `data.xlsx` im Verzeichnis `data/` befindet. Falls die Datei fehlt, erstellen Sie eine neue Excel-Datei mit den benötigten Spalten.

**Autor:** Kassem Farhat
