# Flask Keyboard Layout Manager

## **Projektbeschreibung**
Dieses Projekt ist eine Flask-basierte Webanwendung, die es ermöglicht, Informationen über Modelle, Benutzer und Tastaturlayouts zu erfassen und zu speichern. Es ist ein einfacher Prototyp für das Sammeln und Verwalten von Daten über ein Formular mit einer modernen Benutzererfahrung.

### **Funktionsumfang**
- **Daten erfassen:** 
  - Modelle: Erfasse Informationen zu Geräten (z. B. MacBook Pro, Lenovo).
  - Benutzer: Speichere, welcher Benutzer das Modell erhalten hat.
  - Tastaturlayouts: Wähle ein vordefiniertes Tastaturlayout oder füge ein benutzerdefiniertes Layout hinzu.

- **Dynamische Benutzererfahrung:**
  - Das Formular verwendet **AJAX (Fetch)**, um die Daten asynchron an den Server zu senden, ohne die Seite neu zu laden.
  - Eine Rückmeldung wird nach erfolgreichem Absenden direkt auf der Seite angezeigt.

- **Speicherung der Daten:**
  - Die eingegebenen Daten werden in einer serverseitigen Python-Liste gespeichert (z. B. `data_list`).
  - Die Tastaturlayout-Option "Other" erlaubt es, benutzerdefinierte Layouts hinzuzufügen.

- **Einfache Erweiterbarkeit:**
  - Die Anwendung kann leicht um eine Datenbankanbindung (z. B. SQLite oder PostgreSQL) erweitert werden, um die Daten dauerhaft zu speichern.

---

## **Verwendete Technologien**
- **Backend:** Python (Flask)
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **AJAX:** Dynamisches Senden und Empfangen von Daten ohne Seitenreload.

---

## **Installation und Ausführung**

### **1. Klonen des Repositories**
```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
