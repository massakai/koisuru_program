import tkinter
import tkinter.font
import tkinter.ttk
from typing import NoReturn

from noby.unmo import Unmo
from noby.canvas import NobyCanvas, SpeechBubble


class NobyForm(tkinter.Tk):
    def __init__(self):
        super().__init__()

        # ノビィ生成
        self.noby = Unmo('noby')

        # ウインドウタイトル
        self.title(f'Unmo System : #{self.noby.name}')

        # フォントの準備
        self.font = tkinter.font.Font(family='MS Pゴシック', size=12)

        # メニュー
        self.responder_option_checked = tkinter.BooleanVar()
        self.responder_option_checked.set(False)
        menu_bar = self.create_menu_bar()
        self.config(menu=menu_bar)

        # アニメーション領域
        self.noby_canvas = NobyCanvas(master=self, width=290, height=190)
        self.noby_canvas.place(x=15, y=15)  # 左上の座標を指定

        # 応答メッセージ表示領域
        self.response_area = SpeechBubble(master=self, width=300, height=135)
        self.response_area.place(x=10, y=220)
        self.response_area.draw_bubble()

        # 対話ログ領域
        self.log_area = LogArea(master=self, borderwidth=2)
        self.log_area.place(x=320, y=10, width=305, height=350)

        # 入力領域
        self.message = tkinter.StringVar()
        self.input_area = tkinter.ttk.Entry(master=self, textvariable=self.message)
        self.input_area.place(x=10, y=380, width=525, height=20)
        self.input_area.bind('<Return>', self.input_area_enter)
        talk_button = tkinter.ttk.Button(master=self, text='話す', command=self.talk_button_clicked)
        talk_button.place(x=545, y=380, width=80, height=20)

        # フォーカスを入力領域へ
        self.input_area.focus_set()

    def create_menu_bar(self) -> tkinter.Menu:
        menu_bar = tkinter.Menu(self)

        # ファイル
        file_menu = tkinter.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='終了', command=self.exit_clicked, accelerator="Ctrl+X")
        self.bind_all("<Control-x>", quit)

        # オプション
        option_menu = tkinter.Menu(menu_bar, tearoff=0)
        # チェックボタン
        option_menu.add_checkbutton(label='Responderを表示', variable=self.responder_option_checked, accelerator="Ctrl+R")
        # ショートカットでトグルする
        self.bind_all("<Control-r>", self.response_option_clicked)

        # Macを使っているのでacceleratorが効いているかわからない
        menu_bar.add_cascade(label='ファイル', menu=file_menu, accelerator="Ctrl+F")
        menu_bar.add_cascade(label='オプション', menu=option_menu, accelerator="Ctrl+O")

        return menu_bar

    def input_area_enter(self, _) -> None:
        self.talk()

    def talk_button_clicked(self) -> None:
        self.talk()

    @staticmethod
    def exit_clicked(_):
        quit()

    def response_option_clicked(self, _):
        self.responder_option_checked.set(not self.responder_option_checked.get())

    def talk(self) -> None:
        data = self.message.get()
        # なにも入力されていなければスキップ
        if data == '':
            return

        response = self.noby.dialogue(data)

        self.response_area.update_text(response, self.font)
        self.log_area.put_log('> ' + data)
        self.log_area.put_log(self.prompt() + response)
        self.message.set('')

        self.input_area.focus_set()

    def prompt(self) -> str:
        if self.responder_option_checked.get():
            return f'{self.noby.name}:{self.noby.responder_name()}>'
        else:
            return f'{self.noby.name}>'


class LogArea(tkinter.ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text = tkinter.Text(master=self)
        self.text.configure(state='disabled')

        self.scrollbar = tkinter.ttk.Scrollbar(
            master=self,
            orient=tkinter.VERTICAL,
            command=self.text.yview)

        self.text.config(yscrollcommand=self.scrollbar.set)
        self.text.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        self.scrollbar.grid(column=1, row=0, sticky=(tkinter.N, tkinter.S))
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def put_log(self, log: str) -> None:
        self.text.configure(state='normal')
        self.text.insert('end', log + '\n')
        self.text.configure(state='disabled')
        self.text.see('end')  # 一番下までスクロールする


def main() -> NoReturn:
    app = NobyForm()
    app.minsize(640, 420)
    app.maxsize(640, 420)
    app.mainloop()


if __name__ == '__main__':
    main()
