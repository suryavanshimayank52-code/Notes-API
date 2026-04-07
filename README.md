# Notes API
this is a simple backend project built using Flask that allows  to create, read,delete,and search notes.
## Features
- Create  note
- get all notes
- Delete a note
- Search notes by title or content
## Tech Stack
- Python
- Flask
## API Endpoints
### 1. Create Note
POST /notes
Body:
{
"title": "this is my first Note",
"Content": "this is my note"
}
### 2. Get all Notes
Get /notes
---
### 3. Delete Note
Delete /notes/<id>
---
### 3. Search Notes
Get /notes/search?q=keyword
---
## Edge Cases Handled
- Empty search query
- No matching results
## How to Run
1. Install Flask
pip intsall flask
2. Run the app
python app.py
3. open in browser
http://127.0.0.1:500
## Author
Mayank Suryavanshi







  
