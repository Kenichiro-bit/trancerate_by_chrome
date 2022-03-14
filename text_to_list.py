original_file = "./result.txt"
text_list = []

class text_input_to_list:
    def __init__(self):
        self.file = open(original_file, encoding="utf-8")
        self.line = self.file.readlines()

    def get_text(self):
        for i in range(len(self.line)):
            self.line[i] = self.line[i].replace("\n", "")
            if self.line[i] == "":
                pass
            else:
                text_list.append(self.line[i])

            # text_list[i].replace('\n', '')

a = text_input_to_list()
b = a.get_text()

print(text_list)