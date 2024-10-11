#!/bin/bash

# Dieses Skript installiert die erforderlichen Pakete, startet die Flask-App
# und öffnet den Standardbrowser mit der URL http://localhost:5000

echo "Installiere die erforderlichen Python-Pakete..."

# Installiere die Pakete aus der requirements.txt
pip3 install -r requirements.txt --break-system-packages

# Überprüfe, ob die Installation erfolgreich war
if [ $? -ne 0 ]; then
    echo "Fehler bei der Installation der Pakete."
    exit 1
fi

echo "Starte die Flask-Anwendung..."

# Starte die Flask-App im Hintergrund
python3 app.py &

# Warte ein paar Sekunden, damit der Server starten kann
echo "Warte auf den Start des Servers..."
sleep 5

# Öffne den Standardbrowser mit der URL http://localhost:5000
echo "Öffne den Browser unter http://127.0.0.1:5000..."
if command -v xdg-open > /dev/null; then
    xdg-open http://127.0.0.1:5000
elif command -v open > /dev/null; then
    open http://127.0.0.1:5000
else
    echo "Kein unterstützter Browser-Öffnungsbefehl gefunden."
fi

echo "Flask-Anwendung läuft. Drücke STRG+C, um die Anwendung zu beenden."
wait
