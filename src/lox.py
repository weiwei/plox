import sys
import warnings




class Lox:
    had_error = False

    def main(self, args: list[str]):
        if len(args) > 1:
            print("Usage: plox [script]")
            sys.exit(64)
        elif len(args) == 1:
            self.run_file(args[0])
        else:
            self.run_prompt()


    def run_file(self, path: str):
        with open(path) as f:
            content = f.read()
            self.run(content)
            if self.had_error:
                sys.exit(65)


    def run_prompt(self):
        while True:
            line = input("> ")
            if (line == None):
                break
            self.run(line)
            self.had_error = False


    def run(self, source: str):
        scanner = Scanner(source)
        tokens =scanner.scan_tokens()
        for token in tokens:
            print(token)


    def error(self, line: int, message: str):
        self.report(line, "", message)


    def report(self, line: int, where: str, message: str):
        warnings.warn(f"[line {line} ] Error {where}: {message}")


if __name__ == "__main__":
    lox = Lox()
    lox.main(sys.argv)
