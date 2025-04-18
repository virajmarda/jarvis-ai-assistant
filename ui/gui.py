import tkinter as tk
from tkinter import scrolledtext
from core import voice, gpt_engine, commands
import threading

def launch_gui():
    window = tk.Tk()
    window.title("Jarvis AI")
    window.configure(bg="#1c1c1c")
    window.geometry("600x500")

    output_box = scrolledtext.ScrolledText(window, bg="#2e2e2e", fg="white", font=("Consolas", 12))
    output_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def update_output(text):
        output_box.insert(tk.END, f"> {text}\n")
        output_box.yview(tk.END)

    def handle_input():
        command = entry.get()
        update_output(f"You: {command}")
        entry.delete(0, tk.END)
        response = commands.run_command(command)
        if "not recognised" in response:
            response = gpt_engine.ask_gpt(command)
        update_output(f"Jarvis: {response}")

    def start_listening():
        update_output("🎙 Voice input active...")
        def threaded_listen():
            command = voice.listen()
            update_output(f"You: {command}")
            response = commands.run_command(command)
            if "not recognised" in response:
                response = gpt_engine.ask_gpt(command)
            update_output(f"Jarvis: {response}")
        threading.Thread(target=threaded_listen).start()

    entry = tk.Entry(window, font=("Consolas", 12), bg="#2e2e2e", fg="white")
    entry.pack(fill=tk.X, padx=10, pady=5)
    entry.bind("<Return>", lambda e: handle_input())

    button_frame = tk.Frame(window, bg="#1c1c1c")
    button_frame.pack(pady=10)

    btn_voice = tk.Button(button_frame, text="🎤 Voice", command=start_listening, bg="#444", fg="white")
    btn_voice.pack(side=tk.LEFT, padx=10)

    btn_send = tk.Button(button_frame, text="➤ Send", command=handle_input, bg="#444", fg="white")
    btn_send.pack(side=tk.LEFT, padx=10)

    window.mainloop()
