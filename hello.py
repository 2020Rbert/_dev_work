from flask import Flask, request, render_template

app = Flask(__name__)

data_list = []
@app.route("/")
def home():
    return render_template("index.html")  # Zeigt die HTML-Seite mit dem Button

@app.route("/submit_form", methods=["POST"])
def submit_form():
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

if __name__ == "__main__":
    app.run(debug=True)
