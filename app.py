from flask import Flask
from controllers.note_controller import note_controller
from models.Note import Note

app = Flask(__name__)

app.register_blueprint(note_controller)

if __name__ == '__main__':
    app.run(debug=True)