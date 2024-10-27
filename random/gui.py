import tkinter as tk
import tkinter.scrolledtext as st
import io
import contextlib


class ExecutorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Executor GUI")
        self.geometry("600x400")

        # Input text area
        self.input_text = st.ScrolledText(self, wrap=tk.WORD, width=60, height=10)
        self.input_text.pack(pady=10)

        # Execute button
        self.execute_button = tk.Button(self, text="Execute", command=self.execute_code)
        self.execute_button.pack(pady=5)

        # Output text area
        self.output_text = st.ScrolledText(self, wrap=tk.WORD, width=60, height=10, state=tk.DISABLED)
        self.output_text.pack(pady=10)

    def execute_code(self):
        # Get the code from the input text area
        code = self.input_text.get("1.0", tk.END)

        # Redirect stdout and stderr
        output = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            try:
                exec(code, globals())
            except Exception as e:
                print(e)

        # Display the output
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, output.getvalue())
        self.output_text.config(state=tk.DISABLED)
        output.close()


if __name__ == "__main__":
    app = ExecutorGUI()
    app.mainloop()
