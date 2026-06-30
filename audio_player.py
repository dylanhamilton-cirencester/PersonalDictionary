from playsound3 import playsound
import threading

def playurl(url: str) -> None:
    thread = threading.Thread(target=playsound, args=(url,))
    thread.start()


if __name__ == "__main__":
    playurl("https://api.dictionaryapi.dev/media/pronunciations/en/hello-au.mp3")