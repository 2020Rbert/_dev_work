from flask import Flask, request, render_template, jsonify, flash, redirect, url_for
import db_connection as db



app = Flask(__name__)

data_list = []

@app.route("/")
def home():
    return render_template("index.html")  # Zeigt die HTML-Seite mit dem Button

@app.route('/table-test')
def table_test():
    return render_template('table_test.html')

@app.route("/submit_form_in_list", methods=["POST"])
def submit_form_in_list():
    # Daten aus dem Formular abrufen
    model =         request.form.get("model")
    model_text =    request.form.get("other-model")
    username =      request.form.get("username")
    layout =        request.form.get("layout")
    layout_text =   request.form.get("other_kb_text")
    
    if layout == "other_kb":
        layout = layout_text
        
    if model == "other":
        model = model_text
    
    # Daten in die Liste speichern
    data_list.append({"model": model, "user": username, "kbd_layout": layout})
    
    # Debug-Ausgabe der Liste (nur zu Testzwecken)
    #print(data_list)
    
    # Bestätigung für den Benutzer
    #return f"Data submitted! Model: {model}, Issued User: {username}, KBD_Layout: {layout}"
    return f"""
    <html>
    <head>
        <title>Data Saved</title>
    </head>
    <body>
        <h1>Data Successfully Submitted!</h1>
        <p><strong>Model:</strong> {model}</p>
        <p><strong>Issued User:</strong> {username}</p>
        <p><strong>Keyboard Layout:</strong> {layout}</p>
        <a href="/">Go Back</a>
    </body>
    </html>"""

@app.route("/debug_list", methods=["GET"])
def print_list():
    print(f"Current List: {data_list}")  # Ausgabe in der Server-Konsole
    return f"Current List: {data_list}"  # Rückgabe als String für den Browser

# @app.route("/read_db", methods=["GET"])
# def read_db():
    
#     try:
#         result = db.read_db()  # Funktion, die die Datenbank abfragt
#         return jsonify(result)  # Daten als JSON zurückgeben
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

@app.route("/show_db", methods=["GET"])
def show_db():
    print("show_db route wurde aufgerufen") 
    return render_template('read_db_2.html')

@app.route("/read_db", methods=["GET"])
def read_db():
    try:
        result = db.read_db()
        data = [{"id": row[0], "name": row[1], "price": row[2]} for row in result]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/write_db", methods=["POST"])
def submit_form_db():
    try:
        # Konvertiert den eingehenden JSON-Request in ein Python-Dictionary
        data = request.get_json()
        
        # Extrahiert die einzelnen Werte aus dem Dictionary
        model = data.get('model')
        username = data.get('username')
        layout = data.get('layout')
        
        # Ruft die write_db Funktion aus dem db_connection Modul auf
        success = db.write_db(model, username, layout)
        
        # Gibt eine Erfolgs- oder Fehlermeldung zurück
        if success:
            return jsonify({"status": "success", "message": "Data saved successfully"})
        else:
            return jsonify({"status": "error", "message": "Database error"}), 500
            
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/laptops')
def get_laptops():
    try:
        result = db.read_db()  # Ihre bestehende read_db Funktion
        # Formatieren der Daten für DataTables
        data = [
            {
                "model": row[1],  # Anpassen an Ihre Spaltenindizes
                "username": row[2],
                "layout": row[3]
            } 
            for row in result
        ]
        return jsonify({"data": data})  # Wichtig: DataTables erwartet die Daten im "data" Feld
    except Exception as e:
        print(f"Error fetching data: {e}")  # Debug-Ausgabe
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

print("Registered Routes:")
def list_routes():
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule.methods} - {rule}")
list_routes()