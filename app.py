# Flask code

from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "It is a note API"

# temperary Notes

notes =[]

# creat Notes API

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.json

    note = {
        "id": len(notes) + 1,
        "title": data['title'],
        "content": data['content']
    }

    notes.append(note)
    return jsonify({"message": "Note created", "note": note})

# get all Notes API

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

# delete Notes API
@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    global notes
    notes = [n for n in notes if n['id'] != id]
    return jsonify({"message": "Note is  deleted"})

# Search API

@app.route('/notes/search', methods=['GET'])
def search_notes():
    query = request.args.get('q')

    # Edge Case 1: Empty search
    if not query:
        return jsonify({"error": "Search query is empty"}), 400

    result = []

    for note in notes:
        if query.lower() in note['title'].lower() or query.lower() in note['content'].lower():
            result.append(note)

    # Edge Case 2: No result
    if not result:
        return jsonify({"message": "No notes found"}), 404

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug =True)






