import sqlite3

from dictionary_api import Meaning, WordData

class DictionaryDB():

    def __init__(self):
        self.con = sqlite3.connect("dictionary.db")

    def close(self):
        self.con.close()

    def create_db(self):
        cur = self.con.cursor()

        cur.execute("CREATE TABLE dictionary(id INTEGER PRIMARY KEY, " \
                    "word TEXT, " \
                    "origin TEXT)")
        cur.execute("CREATE TABLE meaning(id INTEGER PRIMARY KEY, word_id INTEGER, part_of_speech TEXT, definition TEXT, example TEXT, " \
                    "FOREIGN KEY(word_id) REFERENCES dictionary(id))")
        
    def add_word(self, word_data: WordData):
        cur = self.con.cursor()

        cur.execute("INSERT INTO dictionary(word, origin) VALUES(?, ?) returning id", (word_data.word, word_data.origin))
        word_id = cur.fetchone()[0]

        for meaning in word_data.meanings:
            cur.execute("INSERT INTO meaning(word_id, part_of_speech, definition, example) VALUES(?, ?, ?, ?)", 
                        (word_id, meaning.part_of_speech, meaning.definition, meaning.example))
        
        self.con.commit()

    def remove_word(self, word: str):
        cur = self.con.cursor()

        cur.execute("DELETE FROM meaning WHERE word_id IN (SELECT id FROM dictionary WHERE word=?)", (word,))
        cur.execute("DELETE FROM dictionary WHERE word=?", (word,))

        self.con.commit()

    def get_words(self) -> list[WordData]:
        cur = self.con.cursor()

        cur.execute("SELECT * FROM dictionary")
        words = cur.fetchall()

        word_datas = []
        for word in words:
            word_id, word_text, origin = word
            cur.execute("SELECT part_of_speech, definition, example FROM meaning WHERE word_id=?", (word_id,))
            meanings_data = cur.fetchall()
            meanings = [Meaning(pos, definition, example) for pos, definition, example in meanings_data]
            word_datas.append(WordData(word_text, [], origin, meanings))

        return word_datas
        
if __name__ == "__main__":
    # Delete the database file if it exists
    import os
    if os.path.exists("dictionary.db"):
        os.remove("dictionary.db")
    
    # Test the database
    db = DictionaryDB()
    db.create_db()
    db.add_word(WordData("hello", [{"text": "həˈləʊ", "audio": "https://api.dictionaryapi.dev/media/pronunciations/en/hello-au.mp3"}], "Old English", [Meaning("interjection", "used as a greeting or to begin a phone conversation.", "Hello there, Katie!")]))
    print(db.get_words())
    db.remove_word("hello")
    print(db.get_words())
    db.close()