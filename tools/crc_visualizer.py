import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox

# Ensure project root is on sys.path so `encoder` package can be imported
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from encoder.CRC import crc_compute, crc_encode, crc_check, modulo2_division_steps


class CRCVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CRC Visualizer")
        self.geometry("700x520")

        main = ttk.Frame(self, padding=12)
        main.pack(fill=tk.BOTH, expand=True)

        # Input
        row = ttk.Frame(main)
        row.pack(fill=tk.X, pady=6)
        ttk.Label(row, text="Binary data:").pack(side=tk.LEFT)
        self.data_var = tk.StringVar()
        self.entry = ttk.Entry(row, textvariable=self.data_var, width=60)
        self.entry.pack(side=tk.LEFT, padx=8)
        self.entry.bind('<KeyRelease>', self._on_input_change)

        ttk.Label(row, text="Generator poly:").pack(side=tk.LEFT, padx=(12,0))
        self.poly_var = tk.StringVar(value="1101")
        self.poly_entry = ttk.Entry(row, textvariable=self.poly_var, width=8)
        self.poly_entry.pack(side=tk.LEFT, padx=6)

        # Controls
        ctl = ttk.Frame(main)
        ctl.pack(fill=tk.X, pady=6)
        self.start_btn = ttk.Button(ctl, text="Start Visualization", command=self.start)
        self.start_btn.pack(side=tk.LEFT)
        self.clear_btn = ttk.Button(ctl, text="Clear Log", command=self.clear_log)
        self.clear_btn.pack(side=tk.LEFT, padx=6)

        self.status_label = ttk.Label(main, text="Enter binary data (0/1).")
        self.status_label.pack(fill=tk.X, pady=(4,8))

        # Visualization area: two boxes side-by-side
        vis = ttk.Frame(main)
        vis.pack(fill=tk.BOTH, expand=False)

        left_frame = ttk.LabelFrame(vis, text='Current window')
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0,6))
        self.left_box = tk.Text(left_frame, height=8, wrap=tk.NONE)
        self.left_box.pack(fill=tk.BOTH, expand=True)
        self.left_box.config(state=tk.DISABLED)

        right_frame = ttk.LabelFrame(vis, text='Working register')
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.right_box = tk.Text(right_frame, height=8, wrap=tk.NONE)
        self.right_box.pack(fill=tk.BOTH, expand=True)
        self.right_box.config(state=tk.DISABLED)

        # Log area
        self.log = tk.Text(main, height=12, wrap=tk.NONE)
        self.log.pack(fill=tk.BOTH, expand=True)
        self.log.config(state=tk.DISABLED)

        # Validation
        self._validate_input()

    def _on_input_change(self, event=None):
        self._validate_input()

    def _validate_input(self):
        s = self.data_var.get()
        valid = all(ch in '01' for ch in s) and len(s) > 0
        if not s:
            self.status_label.config(text="Input is empty.")
            self.start_btn.config(state=tk.DISABLED)
            return
        if not all(ch in '01' for ch in s):
            self.status_label.config(text="Invalid character detected — only 0 and 1 allowed.")
            self.start_btn.config(state=tk.DISABLED)
            return
        # poly validation
        p = self.poly_var.get()
        if not p or not all(ch in '01' for ch in p) or p[0] != '1':
            self.status_label.config(text="Generator polynomial invalid. Must be binary and start with '1'.")
            self.start_btn.config(state=tk.DISABLED)
            return
        self.status_label.config(text="Input valid. Ready to start.")
        self.start_btn.config(state=tk.NORMAL)

    def append_log(self, text: str):
        self.log.config(state=tk.NORMAL)
        self.log.insert(tk.END, text + "\n")
        self.log.see(tk.END)
        self.log.config(state=tk.DISABLED)

    def clear_log(self):
        self.log.config(state=tk.NORMAL)
        self.log.delete('1.0', tk.END)
        self.log.config(state=tk.DISABLED)

    def start(self):
        # Called from UI thread; run sequence using after to avoid blocking
        data = self.data_var.get()
        poly = self.poly_var.get()
        self.start_btn.config(state=tk.DISABLED)
        self.clear_btn.config(state=tk.DISABLED)
        self.append_log("--- CRC Visualization Started ---")
        self.append_log(f"Original data: {data}")
        self.append_log(f"Generator polynomial: {poly}")

        # Step 1: Encode (animate modulo-2 division step-by-step)
        self.append_log("Encoding: computing CRC remainder (step-by-step)...")
        # initialize animation iterator and start
        self._start_division_animation(data, poly, callback=lambda remainder: self._after_encoding(data, remainder, poly))

    def _transmit_stage(self, encoded, poly):
        self.append_log("Transmitting data... (3 seconds)")
        # Could add bit flip here to simulate error; for now assume clean
        self.after(3000, lambda: self._receive_stage(encoded, poly))

    def _receive_stage(self, encoded, poly):
        self.append_log("Receiving data, performing CRC check (step-by-step)...")
        self._start_division_animation(encoded, poly, callback=self._after_receive)

    def _after_receive(self, remainder):
        self.append_log(f"Received remainder: {remainder}")
        valid = all(bit == '0' for bit in remainder)
        conclusion = "No error detected — data is correct." if valid else "Error detected — data is corrupted."
        self.append_log(conclusion)
        messagebox.showinfo("CRC Result", conclusion)
        self.append_log("--- Visualization Completed ---")
        self.start_btn.config(state=tk.NORMAL)
        self.clear_btn.config(state=tk.NORMAL)

    def _after_encoding(self, data, remainder, poly):
        self.append_log(f"Remainder (CRC): {remainder}")
        encoded = data + remainder
        self.append_log(f"Encoded data (data + CRC): {encoded}")
        # schedule transmit after 3s
        self.after(3000, lambda: self._transmit_stage(encoded, poly))

    def _division_steps(self, data: str, poly: str):
        # Backwards-compat: keep unused
        r = len(poly) - 1
        padded = data + '0' * r
        arr = list(padded)
        poly_list = list(poly)
        for i in range(len(arr) - r):
            if arr[i] == '1':
                for j in range(len(poly_list)):
                    arr[i + j] = '1' if arr[i + j] != poly_list[j] else '0'
        remainder = ''.join(arr[-r:]) if r > 0 else ''
        return [], remainder

    # --- Animated division implementation ---
    def _start_division_animation(self, data: str, poly: str, callback):
        # Use encoder.CRC.modulo2_division_steps generator to get correct states
        self._div_iter = modulo2_division_steps(data, poly)
        self._div_callback = callback
        self._per_step_delay = 500
        # clear boxes
        self.left_box.config(state=tk.NORMAL)
        self.left_box.delete('1.0', tk.END)
        self.left_box.config(state=tk.DISABLED)
        self.right_box.config(state=tk.NORMAL)
        self.right_box.delete('1.0', tk.END)
        self.right_box.config(state=tk.DISABLED)
        # start animation
        self.after(100, self._division_animation_step)

    def _update_visual(self):
        s = self._div_state
        arr = s['arr']
        i = s['i']
        poly_len = len(s['poly_list'])
        window = ''.join(arr[i:i+poly_len]) if i < len(arr) else ''

        self.left_box.config(state=tk.NORMAL)
        self.left_box.delete('1.0', tk.END)
        self.left_box.insert(tk.END, f"Window (pos {i}): {window}\n")
        self.left_box.config(state=tk.DISABLED)

        self.right_box.config(state=tk.NORMAL)
        self.right_box.delete('1.0', tk.END)
        self.right_box.insert(tk.END, ''.join(arr))
        self.right_box.config(state=tk.DISABLED)

    def _division_animation_step(self):
        try:
            item = next(self._div_iter)
        except StopIteration:
            # no more steps, compute remainder via crc_compute to be safe
            remainder = ''
            try:
                remainder = crc_compute(self.data_var.get(), self.poly_var.get())
            except Exception:
                remainder = ''
            cb = self._div_callback
            if cb:
                cb(remainder)
            return

        # item is (i, j, state) or ('remainder', remainder)
        if isinstance(item, tuple) and item[0] == 'remainder':
            remainder = item[1]
            # final callback
            cb = self._div_callback
            if cb:
                cb(remainder)
            return

        i, j, state = item
        # update visual boxes
        # window string
        poly_len = len(self.poly_var.get())
        window = state[i:i+poly_len] if i < len(state) else ''
        self.left_box.config(state=tk.NORMAL)
        self.left_box.delete('1.0', tk.END)
        self.left_box.insert(tk.END, f"Window (pos {i}): {window}\n")
        self.left_box.config(state=tk.DISABLED)

        self.right_box.config(state=tk.NORMAL)
        self.right_box.delete('1.0', tk.END)
        # highlight the window portion by surrounding with brackets for clarity
        display = state[:i] + '[' + state[i:i+poly_len] + ']' + state[i+poly_len:]
        self.right_box.insert(tk.END, display)
        self.right_box.config(state=tk.DISABLED)

        # log a concise step
        if j is None:
            self.append_log(f"Window {i}: skipped / boundary -> {state}")
        else:
            self.append_log(f"Window {i}, xor bit {j}: {state}")

        # schedule next animation step
        self.after(self._per_step_delay, self._division_animation_step)


def main():
    app = CRCVisualizer()
    app.mainloop()


if __name__ == '__main__':
    main()
