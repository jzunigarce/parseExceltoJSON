from PyInquirer import prompt, Separator
from config.styles import get_styles

def make_question(name='default', message='Enter a text'):
    question = [
        {
            'type': 'input',
            'name': name,
            'message': message
        }
    ]

    return prompt(question, style=get_styles())

def make_selection(name='default', message='Select options', options=[], separator='= Select option ='):
    options.insert(0, Separator(separator))
    question = [
        {
            'type': 'checkbox',
            'name': name,                
            'message': message,
            'choices': options,
            'validate': lambda answer: 'You muest choose at least one' if len(answer) == 0 else true
        }
    ]
    return prompt(question, style=get_styles())

def make_confirm(name='default', message='Do you want to continue?', default=False):
    question = [
        {
            'type': 'confirm',
            'message': message,
            'name': name,
            'default': default
        }
    ]
    return prompt(question, style=get_styles())

def make_list(name='default', message='What do you want to do?', options=[]):
    question = [
        {
            'type': 'list',
            'name': name,
            'message': message,
            'choices': options
        }
    ]
    return prompt(question, style=get_styles())

