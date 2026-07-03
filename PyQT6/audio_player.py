from collections.abc import Callable, Iterable

from playsound3 import playsound
import threading

def playurl(url: str, f: Callable | None = None, args: Iterable = ()) -> None:
    if callable(f):
        thread = threading.Thread(target=play_sound_wait, args=(url, f, args))
        thread.start()
    else:
        thread = threading.Thread(target=playsound, args=(url,))
        thread.start()

def play_sound_wait(url: str, f: Callable, args: Iterable = ()):
    playsound(url)
    f(*args)


if __name__ == "__main__":
    playurl("https://api.dictionaryapi.dev/media/pronunciations/en/hello-au.mp3")