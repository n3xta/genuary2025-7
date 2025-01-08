import random
import time
import sys
import math

RESET = "\033[0m"
RED   = "\033[31m"
GREEN = "\033[32m"
YELLOW= "\033[33m"
BLUE  = "\033[34m"
MAG   = "\033[35m"
CYAN  = "\033[36m"
WHITE = "\033[37m"

def ansi(code: str):
    sys.stdout.write(code)
    sys.stdout.flush()

def scene_one(rows=20, cols=50):
    background_chars = ['.', ',', ':', '`', '*', '+']
    pattern = []
    for _ in range(rows):
        row_chars = []
        for _ in range(cols):
            char = random.choice(background_chars)
            if random.random() < 0.1:  # ~10% chance to color
                color = random.choice([RED, GREEN, YELLOW, BLUE, MAG, CYAN])
                row_chars.append(color + char + RESET)
            else:
                row_chars.append(char)
        pattern.append(row_chars)
    return pattern

def scene_two(rows=20, cols=50):
    pattern = []
    for r in range(rows):
        row_chars = []
        for c in range(cols):
            wave_val = math.sin((c + time.time() * 3) / 4.0) 
            wave_offset = int((wave_val + 1) * (rows // 4))
            if r == wave_offset:
                row_chars.append(MAG + '~' + RESET)
            else:
                row_chars.append('*' if random.random() < 0.02 else ' ')
        pattern.append(row_chars)
    return pattern

def scene_three(rows=20, cols=50):
    pattern = []
    for _ in range(rows):
        row_chars = []
        for _ in range(cols):
            rand_val = random.random()
            if rand_val < 0.02:
                # A bright star
                row_chars.append(WHITE + '*' + RESET)
            elif rand_val < 0.06:
                # A dim star
                row_chars.append('.')
            else:
                # Empty space
                row_chars.append(' ')
        pattern.append(row_chars)
    return pattern

def embed_word_in_pattern(pattern, word="N3XTA", color=CYAN):

    rows = len(pattern)
    if rows == 0:
        return
    cols = len(pattern[0])

    row_offset = rows // 2
    col_offset = (cols - len(word)) // 2

    colored_word = color + word + RESET
    w_idx = 0
    for ch in colored_word:
        if col_offset + w_idx < cols:
            pattern[row_offset][col_offset + w_idx] = ch
            w_idx += 1

def print_pattern(pattern):

    for row in pattern:
        print("".join(row))

def main_animation():
    ansi("\033[?25l")
    scene_duration = 4
    start_time = time.time()
    scene_index = 0
    scene_functions = [scene_one, scene_two, scene_three]
    rows, cols = 20, 50

    try:
        while True:
            ansi("\033[2J")
            ansi("\033[H")

            current_time = time.time()
            elapsed = current_time - start_time
            if elapsed > scene_duration:
                scene_index = (scene_index + 1) % len(scene_functions)
                start_time = current_time

            current_scene_fn = scene_functions[scene_index]
            ascii_pattern = current_scene_fn(rows, cols)

            if scene_index == 0:
                embed_word_in_pattern(ascii_pattern, "N3XTA", color=GREEN)
            elif scene_index == 1:
                embed_word_in_pattern(ascii_pattern, "N3XTA", color=YELLOW)
            else:
                embed_word_in_pattern(ascii_pattern, "N3XTA", color=RED)

            print_pattern(ascii_pattern)

            time.sleep(0.1)
    finally:
        ansi("\033[?25h")

if __name__ == "__main__":
    main_animation()
