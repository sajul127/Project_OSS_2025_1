import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기 + 팁 계산기")
        self.root.geometry("300x500")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 배열
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['Tip', '=']
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

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "에러"
        elif char == 'Tip':
            self.show_tip_window()
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def show_tip_window(self):
        try:
            base_amount = float(self.expression)
        except:
            self.expression = "숫자 입력 필요"
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)
            return

        tip_window = tk.Toplevel(self.root)
        tip_window.title("팁 비율 입력")
        tip_window.geometry("250x150")

        tk.Label(tip_window, text="팁 비율 (%)", font=("Arial", 12)).pack(pady=5)
        tip_entry = tk.Entry(tip_window, font=("Arial", 14), justify="center")
        tip_entry.pack(pady=5)

        result_label = tk.Label(tip_window, text="", font=("Arial", 12))
        result_label.pack(pady=5)

        def calculate_tip():
            try:
                percent = float(tip_entry.get())
                tip = base_amount * percent / 100
                total = base_amount + tip
                result_label.config(text=f"팁: {tip:.2f}원\n총합: {total:.2f}원")
                self.expression = str(total)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, self.expression)
            except:
                result_label.config(text="숫자 입력 오류")

        tk.Button(tip_window, text="계산", command=calculate_tip).pack(pady=5)