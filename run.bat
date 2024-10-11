@echo off

:: Dieses Skript installiert die erforderlichen Pakete, startet die Flask-Anwendung
:: und öffnet anschließend den Standardbrowser mit der Adresse http://localhost:5000

echo Installation der erforderlichen Python-Pakete...

:: Installiere die Pakete aus der requirements.txt-Datei
pip3 install -r requirements.txt

:: Überprüfe, ob die Installation erfolgreich war
if %ERRORLEVEL% neq 0 (
    echo Fehler bei der Installation der Pakete.
    exit /b 1
)

echo Starte die Flask-Anwendung...

:: Starte die Flask-App im Hintergrund
start /b python3 app.py

:: Warte einige Sekunden, damit der Server gestartet wird
echo Warte auf den Start des Servers...
timeout /t 5 /nobreak >nul

:: Öffne den Standardbrowser mit der URL http://localhost:5000
echo Öffne den Browser unter http://127.0.0.1:5000...
start http://127.0.0.1:5000

:: Fertig
echo Flask-Anwendung läuft. Drücke eine beliebige Taste, um dieses Fenster zu schließen...
pause >nul
exit
