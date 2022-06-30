import collections
import re

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#
# RegEx can be used to check if a string contains the specified search pattern

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])


class Scanner:

    def __init__(self, input):
        self.tokens = []
        self.current_token_number = 0
        for token in self.tokenize(input):
            self.tokens.append(token)

    def tokenize(self, input_string):
        keywords = {"voltagesource", "voltageprobe", "currentsource", "currentprobe", "resistor", "capacitor",
                    "inductor", "diode", "begin", "end", "gnd"}
        token_specification = [
            ('SCIENCE', r'[\+\-]?[0-9]+(\.[0-9]+)?e[\+\-]?[0-9]+'),
            ('FLOAT', r'[\+\-]?[0-9]+\.[0-9]+'),
            ('INT', r'[\+\-]?[0-9]+'),
            ('EQ', r'='),
            ('ID', r'\w+'),
            ('NEWLINE', r'\n'),
            ('SKIP', r'[ \t]'),
            ('COMMA', r'\,'),
            ('CONNECT', r'--'),
            ('OP_BR1', r'\('),
            ('CLOSE_BR1', r'\)'),
            ('OP_BR2', r'\['),
            ('CLOSE_BR2', r'\]'),
            ('COMMENT', r'\#.*\n'),
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in
                             token_specification)  # tworzysz grupowanie nazwa/para i tworzysz z tego krotke tym bedzie sie wyszukiwalo slowa dostajemy pattern
        get_token = re.compile(tok_regex).match  # dostajemy object do matchingu w sumie tu nazywamy tylko funkcje
        line_number = 1
        current_position = line_start = 0
        match = get_token(input_string)  # jezeli od poczatku stringa cos sie matchuje wzraca matchObject inaczej none
        while match is not None:  # wszytsko ma sie zmatchowac inaczej rip
            type = match.lastgroup  # nazwa ostatniej grupy
            if type == 'NEWLINE':
                line_start = current_position
                line_number += 1
                value = match.group(type)
                yield Token(type, value, line_number, match.start() - line_start)
            elif type == 'COMMENT':
                if self.tokens[self.current_token_number - 1].type != 'NEWLINE':
                    type = 'NEWLINE'
                    line_number += 1
                    value = match.group(type)
                    yield Token(type, value, line_number, match.start() - line_start)
                else:
                    type = 'SKIP'
            elif type != 'SKIP':
                value = match.group(type)
                if type == 'ID' and value in keywords:
                    type = value
                yield Token(type, value, line_number, match.start() - line_start)
            current_position = match.end()
            match = get_token(input_string, current_position)
        if current_position != len(input_string):
            raise RuntimeError('Error: Unexpected character %r on line %d' % \
                               (input_string[current_position], line_number))
        yield Token('EOF', '', line_number, current_position - line_start)

    def next_token(self):
        self.current_token_number += 1
        if self.current_token_number - 1 < len(self.tokens):
            return self.tokens[self.current_token_number - 1]
        else:
            raise RuntimeError('Error: No more tokens')
