import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기 + 데이터 단위 변환기")
        self.root.geometry("320x600")

        self.expression = ""

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        self.button_refs = []

        # ✅ log 버튼 제거된 버튼 배열
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=',]
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both", padx=2)
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")
                self.button_refs.append(btn)

        # 데이터 단위 변환기 UI
        tk.Label(root, text="데이터 단위 변환기", font=("Arial", 14, "bold")).pack(pady=5)

        self.data_input = tk.Entry(root, font=("Arial", 18), justify="right")
        self.data_input.pack(fill="both", padx=10, pady=5)

        unit_frame = tk.Frame(root)
        unit_frame.pack(pady=5)

        self.from_unit = tk.StringVar(value="Byte")
        self.to_unit = tk.StringVar(value="KB")

        from_menu = tk.OptionMenu(unit_frame, self.from_unit, "Byte", "KB", "MB", "GB")
        to_menu = tk.OptionMenu(unit_frame, self.to_unit, "Byte", "KB", "MB", "GB")
        from_menu.pack(side="left", padx=10)
        to_menu.pack(side="left", padx=10)

        convert_btn = tk.Button(root, text="변환", font=("Arial", 16), command=self.convert_data)
        convert_btn.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 16))
        self.result_label.pack(pady=5)

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

    def convert_data(self):
        try:
            value = float(self.data_input.get())
            from_u = self.from_unit.get()
            to_u = self.to_unit.get()

            units = {
                "Byte": 1,
                "KB": 1024,
                "MB": 1024 ** 2,
                "GB": 1024 ** 3
            }

            result = value * units[from_u] / units[to_u]
            self.result_label.config(text=f"{result:.4f} {to_u}")
        except:
            self.result_label.config(text="변환 오류")