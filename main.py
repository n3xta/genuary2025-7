import random
import time
import sys

def ansi(code: str):
    """Utility to write ANSI escape codes and flush output."""
    sys.stdout.write(code)
    sys.stdout.flush()

def generate_ascii_pattern(rows=20, cols=50):
    """
    Generates a 2D list (rows x cols) of random ASCII characters 
    to form a pixel-like background.
    """
    background_chars = ['.', ',', ':', ';', '`', '*', '+']
    pattern = [
        [random.choice(background_chars) for _ in range(cols)]
        for _ in range(rows)
    ]
    return pattern

def embed_word_in_pattern(pattern, word="n3xta"):
    """
    Embeds 'word' in the center of 'pattern'.
    """
    rows = len(pattern)
    cols = len(pattern[0]) if rows > 0 else 0

    # Calculate starting offset for center placement
    row_offset = rows // 2
    col_offset = (cols - len(word)) // 2

    for i, char in enumerate(word):
        if 0 <= row_offset < rows and 0 <= col_offset + i < cols:
            pattern[row_offset][col_offset + i] = char

def print_pattern(pattern):
    """
    Prints the 2D 'pattern' to the terminal.
    """
    for row in pattern:
        print("".join(row))

def main_animation():
    # Hide the cursor
    ansi("\033[?25l")

    try:
        while True:
            # Clear the screen and move cursor to top-left
            ansi("\033[2J")
            ansi("\033[H")

            # 1) Generate a random pattern
            ascii_pattern = generate_ascii_pattern(rows=20, cols=50)

            # 2) Embed the word "n3xta" in the center
            embed_word_in_pattern(ascii_pattern, word="n3xta")

            # 3) Print the pattern
            print_pattern(ascii_pattern)

            # 4) Pause briefly before the next "frame"
            time.sleep(0.2)
    finally:
        # Show the cursor again on exit
        ansi("\033[?25h")

if __name__ == "__main__":
    main_animation()
