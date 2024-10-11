from flask import Flask, render_template, request, jsonify, redirect, url_for, send_file, flash
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Notwendig für Flash-Messages

# Lade die Excel-Datei und ersetze NaN-Werte durch leere Strings
def load_data():
    df = pd.read_excel('data/data.xlsx', dtype=str)  # Lese alles als String
    df = df.fillna('')  # Ersetze alle NaN-Werte durch leere Strings
    return df

@app.route('/')
def index():
    df = load_data()

    # Suchfunktion
    query = request.args.get('search', '')
    if query:
        df = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]

    # Zeige die gefilterte Tabelle an
    records = df.to_dict(orient='records')
    columns = df.columns.tolist()

    return render_template('index.html', records=records, columns=columns, query=query)

# Eventname Filterfunktion
@app.route('/event/<event_name>')
def show_event(event_name):
    df = load_data()

    # Filtere nach dem Eventnamen
    filtered_df = df[df['Eventname'] == event_name]

    # Blende Spalten aus, die den Wert 'false' enthalten, als String
    filtered_df = filtered_df.loc[:, ~(filtered_df.astype(str).apply(lambda x: x.str.lower()) == 'false').all()]

    # Konvertiere die gefilterten Daten in ein Dictionary für das Template
    records = filtered_df.to_dict(orient='records')
    columns = filtered_df.columns.tolist()

    return render_template('event.html', event_name=event_name, records=records, columns=columns)

# Funktion zum Aktualisieren einer Zelle
@app.route('/update_cell', methods=['POST'])
def update_cell():
    data = request.json
    event_name = data['event_name']
    column_name = data['column_name']
    new_value = data['new_value']

    df = load_data()

    # Aktualisiere den Wert in der entsprechenden Zeile und Spalte
    if event_name in df['Eventname'].values:
        df.loc[df['Eventname'] == event_name, column_name] = new_value

        # Speichere die aktualisierte Excel-Datei
        df.to_excel('data/data.xlsx', index=False)
        return jsonify(success=True)
    else:
        return jsonify(success=False)

# Filterfunktion nach True/False
@app.route('/filter/<column>/<value>')
def filter_by_column(column, value):
    df = load_data()

    # Filtere nach der entsprechenden Spalte und dem Wert (True oder False als String)
    filtered_df = df[df[column].astype(str).str.lower() == value.lower()]

    # Konvertiere die gefilterten Daten in ein Dictionary für das Template
    records = filtered_df.to_dict(orient='records')
    columns = df.columns.tolist()

    return render_template('index.html', records=records, columns=columns, selected_column=column, selected_value=value)

# Funktion zum Hinzufügen neuer Daten
@app.route('/add', methods=['GET', 'POST'])
def add_data():
    df = load_data()
    columns = df.columns.tolist()

    if request.method == 'POST':
        # Erstelle ein leeres Dictionary für die neue Zeile
        new_row = {}
        for col in columns:
            value = request.form.get(col, '')
            new_row[col] = value if value.strip() else ''  # Leere Felder bleiben leer

        # Erstelle einen neuen DataFrame mit der neuen Zeile
        new_df = pd.DataFrame([new_row])

        # Füge die neue Zeile zum existierenden DataFrame hinzu
        df = pd.concat([df, new_df], ignore_index=True)

        # Speichere den aktualisierten DataFrame in die Excel-Datei
        df.to_excel('data/data.xlsx', index=False)

        return redirect(url_for('index'))

    return render_template('add.html', columns=columns)

# Spalten löschen
@app.route('/delete_row/<event_name>', methods=['POST'])
def delete_row(event_name):
    df = load_data()

    # Überprüfe, ob der Eventname existiert und lösche die Zeile
    if event_name in df['Eventname'].values:
        df = df[df['Eventname'] != event_name]

        # Speichere die aktualisierte Excel-Datei
        df.to_excel('data/data.xlsx', index=False)
        flash(f'Zeile mit Eventname "{event_name}" erfolgreich gelöscht!', 'success')
    else:
        flash(f'Zeile mit Eventname "{event_name}" nicht gefunden!', 'danger')

    return redirect(url_for('index'))

# Exportiere die aktuelle Excel-Datei
@app.route('/export')
def export_excel():
    excel_path = 'data/data.xlsx'
    if os.path.exists(excel_path):
        return send_file(excel_path, as_attachment=True)
    else:
        return "Excel file not found."

if __name__ == '__main__':
    app.run(debug=True)
