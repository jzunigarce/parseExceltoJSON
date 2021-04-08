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

