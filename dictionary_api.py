from dataclasses import dataclass

import requests

@dataclass
class Meaning:
    part_of_speech: str
    definition: str
    example: str

    def __repr__(self) -> str:
        return f"""{self.part_of_speech}
{self.definition}
{self.example}"""

@dataclass
class WordData:
    word: str
    phonetics: list[dict] # dict can have text and possibly audio in the form of a url
    origin: str
    meanings: list[Meaning]

    def __repr__(self) -> str:
        return f"""{self.word}
{'\n'.join([p["text"] if "text" in self.phonetics[0] else "" for p in self.phonetics])}

{'\n\n'.join([str(meaning) for meaning in self.meanings])}
"""
    def get_audio_url(self) -> str:
        url = ""
        for p in self.phonetics:
            if "audio" in p:
                url = p["audio"]
                break

        return url

class DictionaryAPI:

    def __init__(self):
        self.endpoint = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    def get_word_data(self, word: str) -> WordData | str:
        with requests.get(self.endpoint + word) as response:
            body = response.json()
            if type(body) == dict and "title" in body:
                return f"Word {word.strip()} not found"
            
            word_json = body[0]
            # Get meanings
            meanings = []
            json_meanings = word_json["meanings"]
            for meaning in json_meanings:
                pos = meaning["partOfSpeech"]
                definition = meaning["definitions"][0]["definition"]
                example = "No Example Found"
                if "example" in meaning["definitions"][0]:
                    example = meaning["definitions"][0]["example"]
                meanings.append(Meaning(pos, definition, example))
            
            return WordData(word_json["word"], word_json["phonetics"], word_json["origin"] if "origin" in word_json else "No Origin Found", meanings)
        
if __name__ == "__main__":
    dict_API = DictionaryAPI()
    word = dict_API.get_word_data("hello")
    print(word)
