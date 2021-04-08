# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt, Separator, style_from_dict, Token
from .config.styles import get_styles

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
    
    def make_question(name='default', message='Enter a text'):
        questions = [
            {
                'type': 'input',
                'name': name,
                'message': message
            }
        ]

        answer = prompt(question, style=self.get_styles())

