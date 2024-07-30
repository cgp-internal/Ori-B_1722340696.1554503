import csv

class NoteService:
    def __init__(self, file_name):
        self.file_name = file_name
        self.notes = self.read_notes_from_csv()

    def read_notes_from_csv(self):
        notes = []
        with open(self.file_name, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                notes.append({'id': int(row[0]), 'title': row[1], 'content': row[2]})
        return notes

    def get_all_notes(self):
        return self.notes

    def get_note(self, note_id):
        for note in self.notes:
            if note['id'] == note_id:
                return note
        return None

    def create_note(self, title, content):
        new_id = max([note['id'] for note in self.notes]) + 1
        new_note = {'id': new_id, 'title': title, 'content': content}
        self.notes.append(new_note)
        self.write_notes_to_csv()

    def update_note(self, note_id, title, content):
        for note in self.notes:
            if note['id'] == note_id:
                note['title'] = title
                note['content'] = content
                self.write_notes_to_csv()
                return
        raise ValueError(f"Note with id {note_id} does not exist")

    def delete_note(self, note_id):
        for note in self.notes:
            if note['id'] == note_id:
                self.notes.remove(note)
                self.write_notes_to_csv()
                return
        raise ValueError(f"Note with id {note_id} does not exist")

    def write_notes_to_csv(self):
        with open(self.file_name, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["id", "title", "content"])
            for note in self.notes:
                csv_writer.writerow([note['id'], note['title'], note['content']])


note_service = NoteService('data/notes.csv')