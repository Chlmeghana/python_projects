class ClipboardManager:
    def __init__(self):
        self.copied_texts = []

    def copy_text(self, text):
        self.copied_texts.append(text)

    def display_history(self):
        print("Copied Texts History:")
        for idx, text in enumerate(self.copied_texts, start=1):
            print(f"{idx}. {text}")

# Example Usage
clipboard = ClipboardManager()

while True:
    new_text = input("Copy a new text (or 'q' to quit): ")
    
    if new_text.lower() == 'q':
        break
    
    clipboard.copy_text(new_text)
    clipboard.display_history()
