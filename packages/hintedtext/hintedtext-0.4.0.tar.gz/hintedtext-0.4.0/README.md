# Hinted Text 
Hinted text widget for tkinter.

This custom `HintedText` class inherits from `tk.Text` and adds a hint parameter in the constructor. The `clear_hint` method is bound to the `<FocusIn>` event and will clear the hint text if the widget has focus and the text is the same as the hint. The `add_hint` method is bound to the `<FocusOut>` event and will add the hint text back if the widget loses focus and the text is empty.



# Installation

```bash
pip install hintedtext
```

# Usage

```py
import tkinter as tk
from hintedtext import HintedText

root = tk.Tk()
text = HintedText(root, hint="Enter your text here")
text.pack()
root.mainloop()
```
