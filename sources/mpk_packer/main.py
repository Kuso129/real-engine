from image import*
from mpk_file import*

class Packeger:
    def __init__(self):
        self.run()

    def run(self):
        reference_name = input('Please enter the name of config file for pack... ')
        print('Pack creation process...')

        mpk_exmple = MPKFileBuilder(reference_name)
        print(f"Pack {mpk_exmple.parameters['name']} is creted :).")

        while(True):
            c = input()
            if c == 'quit' or c == 'exit':
                exit()


if __name__ == '__main__':
    app = Packeger()
