import random
from enum import Enum
from pathlib import Path
from threading import Thread
from time import sleep
from tkinter import Canvas, Text, NW
from tkinter.font import Font
from typing import NoReturn, Optional

from PIL import Image, ImageTk

import noby


class PatternName(Enum):
    NORMAL = 'normal'
    BLINK = 'blink'
    LOOK_AROUND = 'lookaround'


class NobyCanvas(Canvas):

    def __init__(self, *args, **kwargs) -> NoReturn:
        super().__init__(*args, **kwargs)

        # load bitmaps
        self.patterns = {
            PatternName.NORMAL: Normal(PatternName.NORMAL),
            PatternName.BLINK: Blink(PatternName.BLINK),
            PatternName.LOOK_AROUND: LookAround(PatternName.LOOK_AROUND)}

        self.current_pattern = self.patterns[PatternName.NORMAL]

        # プログラムが終了するようにデーモンフラグをセットする
        self.draw_thread = Thread(target=self.draw_bitmaps, daemon=True)
        self.before_destroy = True
        self.draw_thread.start()

    def draw_bitmaps(self) -> NoReturn:
        while True:
            # 大体100ミリ秒間隔で更新する
            image_tk = self.current_pattern.next_bitmap()
            if image_tk is None:
                self.change_pattern(self.current_pattern.next_pattern())
                continue
            self.create_image(0, 0, image=image_tk, anchor=NW)
            sleep(0.1)

    def change_pattern(self, pattern_name: PatternName) -> None:
        next_pattern = self.patterns[pattern_name]

        # パターンの変更がなければ何もしない
        if self.current_pattern is next_pattern:
            return

        next_pattern.reset()
        self.current_pattern = next_pattern


class Pattern:
    def __init__(self, pattern_name: PatternName):
        dir_path = Path(noby.__path__[0]) / 'bmps' / pattern_name.value
        self._bitmaps = [
            ImageTk.PhotoImage(Image.open(open(bmp_path, 'rb')))
            for bmp_path in sorted(dir_path.glob("*.bmp"))]
        self._index = 0
        self._loop = 0

    def next_bitmap(self) -> Optional[ImageTk.PhotoImage]:
        try:
            bitmap = self._bitmaps[self._index]
            self._index += 1
        except IndexError:
            self._loop += 1
            self._index = 0
            return None

        return bitmap

    def next_pattern(self) -> NoReturn:
        raise NotImplementedError()

    def reset(self) -> None:
        self._index = 0
        self._loop = 0


class Normal(Pattern):
    def next_pattern(self) -> PatternName:
        if self._loop <= 20:
            return PatternName.NORMAL

        rand = random.randrange(10)
        if rand in (0, 1, 2, 3):
            return PatternName.BLINK
        elif rand in (4, 5):
            return PatternName.LOOK_AROUND
        else:
            return PatternName.NORMAL


class Blink(Pattern):
    def next_pattern(self) -> PatternName:
        if self._loop < 2:
            return PatternName.BLINK
        return PatternName.NORMAL


class LookAround(Pattern):
    def next_pattern(self) -> PatternName:
        return PatternName.NORMAL


class SpeechBubble(Canvas):
    def __init__(self, *args, **kwargs) -> NoReturn:
        super().__init__(*args, **kwargs)
        self.text = Text(master=self)
        self.text.configure(state='disabled')
        self.text.place(x=10, y=20, width=280, height=110)

    def draw_bubble(self):
        self.create_polygon(
            5, 15,
            20, 15,
            30, 5,
            40, 15,
            300, 15,
            300, 135,
            5, 135,
            outline='black',
            fill=self.master['background'],
        )

    def update_text(self, text: str, font: Font) -> None:
        self.text.configure(state='normal', font=font)
        self.text.replace('1.0', 'end', text)
        self.text.configure(state='disabled')
