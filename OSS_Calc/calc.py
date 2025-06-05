import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.is_dark_mode = False  # 다크모드 상태 저장
        self.expression = ""

        # 다크모드 토글 버튼
        self.toggle_button = tk.Button(root, text="다크모드", command=self.toggle_theme)
        self.toggle_button.pack(fill="x")

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        self.button_refs = []  # 버튼들을 리스트에 저장해서 나중에 스타일 바꿈
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")
                self.button_refs.append(btn)

        self.apply_theme()  # 초기 테마 적용

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.toggle_button.config(text="라이트모드" if self.is_dark_mode else "다크모드")
        self.apply_theme()

    def apply_theme(self):
        if self.is_dark_mode:
            bg_color = "#2e2e2e"
            fg_color = "#ffffff"
            btn_bg = "#444444"
            btn_fg = "#ffffff"
        else:
            bg_color = "#f0f0f0"
            fg_color = "#000000"
            btn_bg = "#ffffff"
            btn_fg = "#000000"

        self.root.configure(bg=bg_color)
        self.entry.configure(bg=btn_bg, fg=fg_color, insertbackground=fg_color)
        self.toggle_button.configure(bg=btn_bg, fg=btn_fg)

        for btn in self.button_refs:
            btn.configure(bg=btn_bg, fg=btn_fg)