from flask import Blueprint, request, jsonify
from services.note_service import note_service

note_controller = Blueprint('note_controller', __name__)

@note_controller.route('/notes', methods=['GET'])
def get_all_notes():
    return jsonify(note_service.get_all_notes())

@note_controller.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = note_service.get_note(note_id)
    if note is not None:
        return jsonify(note)
    else:
        return jsonify({"error": "Note not found"}), 404

@note_controller.route('/notes', methods=['POST'])
def create_note():
    data = request.json
    title = data.get('title')
    content = data.get('content')
    if title is not None and content is not None:
        note_service.create_note(title, content)
        return jsonify({"message": "Note created successfully"}), 201
    else:
        return jsonify({"error": "Title and content are required"}), 400

@note_controller.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.json
    title = data.get('title')
    content = data.get('content')
    if title is not None and content is not None:
        try:
            note_service.update_note(note_id, title, content)
            return jsonify({"message": "Note updated successfully"})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
    else:
        return jsonify({"error": "Title and content are required"}), 400

@note_controller.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    try:
        note_service.delete_note(note_id)
        return jsonify({"message": "Note deleted successfully"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404