import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nLies, tell me lies, baby, tell me how you hate me", 0.13),
        ("Hate me, hate me, still tryna replace me", 0.10),
        ("Chase me, chase me, tell me how you hate me?", 0.12),
        ("Erase me, 'rase me, wish you never dated me", 0.12),
        ("\nLies, tell me lies, baby, tell me how you hate me", 0.13)
    ]
    delays = [8.5, 12.4, 16.2, 19.8, 23.7]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
