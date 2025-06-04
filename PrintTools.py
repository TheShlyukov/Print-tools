import time
import sys
import random

class PrintTools:
    COLOR_CODES = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }

    @staticmethod
    def _color_text(text, color):
        if not color:
            return text
        code = PrintTools.COLOR_CODES.get(color.lower())
        if not code:
            raise ValueError(f"Unsupported color: {color}")
        return f"{code}{text}{PrintTools.COLOR_CODES['reset']}"

    @staticmethod
    def withDelay(text, delay, color=None):
        """
        Prints the given text after a delay in seconds.
        Delay can be a float or int.
        Optional color parameter to color the entire text.
        """
        try:
            delay = float(delay)
            if delay < 0:
                raise ValueError("Delay must be non-negative")
        except Exception as e:
            raise ValueError(f"Invalid delay value: {delay}") from e
        time.sleep(delay)
        print(PrintTools._color_text(text, color))

    @staticmethod
    def byLetter(text, delay, color=None):
        """
        Prints the text letter by letter with a delay between each letter.
        Delay should be a non-negative float or int representing seconds.
        Optional color parameter to color the entire text or a list of colors for each character.
        """
        try:
            delay = float(delay)
            if delay < 0:
                raise ValueError("Delay must be non-negative")
        except Exception as e:
            raise ValueError(f"Invalid delay value: {delay}") from e

        if isinstance(color, list):
            if len(color) != len(text):
                raise ValueError("Length of color list must match length of text")
            for l, c in zip(text, color):
                sys.stdout.write(PrintTools._color_text(l, c))
                sys.stdout.flush()
                time.sleep(delay)
        else:
            colored_text = PrintTools._color_text(text, color)
            for l in colored_text:
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(delay)
        print("")

    @staticmethod
    def typeEmulate(text, speed, color=None):
        """
        Emulates typing of the text at the given speed in words per minute (wpm).
        Speed should be a positive number.
        Optional color parameter to color the entire text or a list of colors for each character.
        """
        try:
            speed = float(speed)
            if speed <= 0:
                raise ValueError("Speed must be positive")
        except Exception as e:
            raise ValueError(f"Invalid speed value: {speed}") from e

        if isinstance(color, list):
            if len(color) != len(text):
                raise ValueError("Length of color list must match length of text")
            for l, c in zip(text, color):
                sys.stdout.write(PrintTools._color_text(l, c))
                sys.stdout.flush()
                time.sleep(random.random() * 10.0 / speed)
        else:
            colored_text = PrintTools._color_text(text, color)
            for l in colored_text:
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(random.random() * 10.0 / speed)
        print("")

    @staticmethod
    def p(lines, color=None):
        """
        Prints the given number of empty lines.
        Lines should be a non-negative integer or string convertible to int.
        Optional color parameter to color the empty lines (applies to newline characters).
        """
        if lines == "":
            print(PrintTools._color_text("", color))
            return
        try:
            count = int(lines)
            if count < 0:
                raise ValueError("Lines must be non-negative")
        except Exception as e:
            raise ValueError(f"Invalid lines value: {lines}") from e
        for _ in range(count):
            print(PrintTools._color_text("", color))

    @staticmethod
    def printCentered(text, width, color=None):
        """
        Prints the text centered within the given width.
        Width should be a positive integer.
        Optional color parameter to color the entire text.
        """
        try:
            width = int(width)
            if width <= 0:
                raise ValueError("Width must be positive")
        except Exception as e:
            raise ValueError(f"Invalid width value: {width}") from e
        print(PrintTools._color_text(text.center(width), color))

    @staticmethod
    def printWithBorder(text, border_char='*', color=None):
        """
        Prints the text surrounded by a border made of the specified character.
        Border_char should be a single character string.
        Optional color parameter to color the entire border and text.
        """
        if not isinstance(border_char, str) or len(border_char) != 1:
            raise ValueError("border_char must be a single character string")
        length = len(text) + 4
        border_line = border_char * length
        middle_line = f"{border_char} {text} {border_char}"
        print(PrintTools._color_text(border_line, color))
        print(PrintTools._color_text(middle_line, color))
        print(PrintTools._color_text(border_line, color))

    @staticmethod
    def printRepeated(text, times, delay=0, color=None):
        """
        Prints the text multiple times with an optional delay between prints.
        Times should be a non-negative integer.
        Delay should be a non-negative float or int.
        Optional color parameter to color the entire text.
        """
        try:
            times = int(times)
            if times < 0:
                raise ValueError("Times must be non-negative")
            delay = float(delay)
            if delay < 0:
                raise ValueError("Delay must be non-negative")
        except Exception as e:
            raise ValueError(f"Invalid times or delay value: times={times}, delay={delay}") from e
        for _ in range(times):
            print(PrintTools._color_text(text, color))
            time.sleep(delay)

    @staticmethod
    def printProgressBar(progress, total, length=40, color=None):
        """
        Prints a progress bar to the console.
        Progress and total should be non-negative numbers with progress <= total.
        Length is the length of the progress bar in characters.
        Optional color parameter to color the filled part of the bar.
        """
        try:
            progress = float(progress)
            total = float(total)
            length = int(length)
            if progress < 0 or total <= 0 or progress > total or length <= 0:
                raise ValueError("Invalid progress, total or length values")
        except Exception as e:
            raise ValueError(f"Invalid progress, total or length values: progress={progress}, total={total}, length={length}") from e
        filled_length = int(length * progress // total)
        bar_filled = '█' * filled_length
        bar_empty = '-' * (length - filled_length)
        bar = PrintTools._color_text(bar_filled, color) + bar_empty
        print(f"\r|{bar}| {progress:.1f}/{total}", end='\r')
        if progress == total:
            print("")


if __name__ == "__main__":
    # Basic functionality tests
    PrintTools.byLetter("hello, world!", 0.1)
    PrintTools.p(3)
    PrintTools.typeEmulate("Heeeey fjsadhgfljkdsagvjkdsfhgfui;ehufk;ehf", 50)
    PrintTools.withDelay('the end', 2)

    # Color tests
    PrintTools.withDelay("Colored text", 0, color="red")
    PrintTools.byLetter("Colored", 0, color="green")
    PrintTools.byLetter("Colored", 0, color=["red"]*7)
    PrintTools.typeEmulate("Colored", 100, color="blue")
    PrintTools.typeEmulate("Colored", 100, color=["yellow"]*7)
    PrintTools.p(2, color="cyan")
    PrintTools.printCentered("Centered", 20, color="magenta")
    PrintTools.printWithBorder("Bordered", border_char="#", color="yellow")
    PrintTools.printRepeated("Repeated", 2, 0, color="red")
    PrintTools.printProgressBar(5, 10, color="green")
