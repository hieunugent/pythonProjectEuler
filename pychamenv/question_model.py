class Question:
    def __init__(self, q_text, q_awnser):
        self.text = q_text
        self.awnser = q_awnser

new_q = Question("are you Ok?", "True")
print(new_q)