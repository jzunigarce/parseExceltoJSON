# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt, Separator, style_from_dict, Token
from os import path

class UIMenu:
    def __init__(self):
        self.draw()

    def draw(self):
        print("🚀 xlsx to JSON converter")
        self.menu()
    #def ():
    #    pass

    def menu(self):
        questions = [
            {
                'type': 'input',
                'name': 'path',
                'message': 'Enter filename or dir'
            }
        ]

        answers = prompt(questions, style=self.get_styles())
        path = answers['path']
        print(path)
        if self.is_dir(path):
            print("Es directorio")
        elif self.is_file(path):
            print("Es archivo")
        else:
            print("Error en el archivo")

        questions = [
            {
                'type': 'checkbox',
                'name': 'worksheets',
                'message': "Worksheets",
                'choices': [
                    Separator('= Select worksheets ='),
                    {
                        'name': 'Ham'
                    },
                    {
                        'name': 'Ground meat'
                    },
                ],
                'Validate': lambda answer: 'You muest choose at least one' if len(answer) == 0 else true
            }
        ]

        answers = prompt(questions, style=self.get_styles())
        pprint(answers)

    def is_dir(self, dirname):
        return path.isdir(dirname)

    def is_file(self, filename):
        return path.isfile(filename)

    def get_styles(self):
        custom_style = style_from_dict({
            Token.Separator: '#66a6c3 bold',
            Token.QuestionMark: '#ff0000 bold',
            Token.Selected: '#cc5454',  # default
            Token.Pointer: '#673ab7 bold',
            Token.Instruction: 'bold',  # default
            Token.Answer: '#66a6c3 bold',
            Token.Question: 'bold',
        })

        return custom_style
