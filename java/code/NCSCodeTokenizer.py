from .code_tokenizer import CodeTokenizer
from .simple_tokenizer import SimpleTokenizer

class NCSCodeTokenizer:
    def __init__(self):
        self.simple_tokenizer = SimpleTokenizer()
        self.code_tokenizer = CodeTokenizer()
    def tokenize(self, code):
        tokens = [x[0] for x in self.simple_tokenizer.tokenize(code).data]
        tokens = [x[0] for x in self.code_tokenizer.tokenize(" ".join(tokens)).data]
        return tokens
