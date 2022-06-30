class Parser2:

    ##### Parser header #####
    def __init__(self, scanner):
        self.next_token = scanner.next_token
        self.token = self.next_token()

    def take_token(self, token_type):
        if self.token.type != token_type:
            self.error("Expected token: %s at line : %d" % (token_type, self.token.line))
        if token_type != 'EOF':
            self.token = self.next_token()

    def error(self, msg):
        raise RuntimeError('Parser error, %s' % msg)

    ##### Parser body #####

    # Starting symbol
    # program -> BEGIN inicialization NEWLINE command END EOF
    def program(self):
        # find word begin
        if self.token.type != 'begin':
            self.token = self.next_token()
            if self.token.type == 'EOF':
                self.error("No begin symbol")
            self.program()
        elif self.token.type == 'begin':
            self.take_token('begin')
            self.take_token('NEWLINE')
            self.initialization()
            self.take_token('NEWLINE')
            self.command()
            self.take_token('end')
            # self.take_token('NEWLINE')
            # self.take_token('EOF')
            print('PARSER SUCCES')
        else:
            self.error("Epsilon not allowed")

    # inicialization -> ID EQ typ NEWLINE inicialization
    # initialization -> eps
    def initialization(self):
        if self.token.type == 'ID':
            self.take_token('ID')
            self.take_token('EQ')
            self.typ()
            self.take_token('NEWLINE')
            self.initialization()
        else:
            pass

    def typ(self):
        # typ -> voltagesourceinicialization
        if self.token.type == 'voltagesource':
            self.voltagesourceinicialization()

        # typ -> voltageprobeinicialization
        if self.token.type == 'voltageprobe':
            self.voltageprobeinicialization()

        # typ -> currentsourceinicialization
        if self.token.type == 'currentsource':
            self.currentsourceinicialization()

        # typ -> currentprobeinicialization
        if self.token.type == 'currentprobe':
            self.currentprobeinicialization()

            # typ -> resistorinicialization
        if self.token.type == 'resistor':
            self.resistorinicialization()

        # typ -> capacitorinicialization)
        if self.token.type == 'capacitor':
            self.capacitorinicialization()

            # typ -> inductorinicialization
        if self.token.type == 'inductor':
            self.inductorinicialization()

        # typ -> diodeinicialization
        if self.token.type == 'diode':
            self.diodeinicialization()

    # voltagesourceinicialization ->voltagesource(number)
    # voltagesourceinicialization -> voltagesource()
    def voltagesourceinicialization(self):
        self.take_token('voltagesource')
        self.take_token('OP_BR1')
        if self.token.type == 'INT' or self.token.type == 'FLOAT' or self.token.type == 'SCIENCE':
            self.number()
        if self.token.type == 'CLOSE_BR1':
            self.take_token('CLOSE_BR1')
        else:
            self.error("Expected value or null at voltagesource")
        print("voltagesource OK")

    # voltageprobeinicialization -> voltageprobe()
    def voltageprobeinicialization(self):
        self.take_token('voltageprobe')
        self.take_token('OP_BR1')
        if self.token.type == 'CLOSE_BR1':
            self.take_token('CLOSE_BR1')
        else:
            self.error("voltageprobe cant have parameters")
        print('voltageprobe OK')

    # currentsourceinicialization -> currentsource(number)
    # currentsourceinicialization -> currentsource()
    def currentsourceinicialization(self):
        self.take_token('currentsource')
        self.take_token('OP_BR1')
        if self.token.type == 'INT' or self.token.type == 'FLOAT' or self.token.type == 'SCIENCE':
            self.number()
        if self.token.type == 'CLOSE_BR1':
            self.take_token('CLOSE_BR1')
        else:
            self.error("Expected value or null at currentsource")
        print("currentsource OK")

    # currentprobeinicialization -> currentprobe()
    def currentprobeinicialization(self):
        self.take_token('currentprobe')
        self.take_token('OP_BR1')
        if self.token.type == 'CLOSE_BR1':
            self.take_token('CLOSE_BR1')
        else:
            self.error("currentprobe cant have parameters")
        print('currentprobe OK')

    # resistorinicialization -> resistor(number)
    def resistorinicialization(self):
        self.take_token('resistor')
        self.take_token('OP_BR1')
        self.number()
        self.take_token('CLOSE_BR1')
        print("resistor OK")

    # capacitorinicialization -> capacitor(number)
    def capacitorinicialization(self):
        self.take_token('capacitor')
        self.take_token('OP_BR1')
        self.number()
        self.take_token('CLOSE_BR1')
        print("capacitor OK")

    # inductorinicialization -> inductor(number)
    def inductorinicialization(self):
        self.take_token('inductor')
        self.take_token('OP_BR1')
        self.number()
        self.take_token('CLOSE_BR1')
        print("inductor OK")

    # diodeinicialization -> diode(parameters)
    def diodeinicialization(self):
        self.take_token('diode')
        self.take_token('OP_BR1')
        self.parameters()
        self.take_token('CLOSE_BR1')
        print('dioda ok')

    # number -> INT
    # number -> FLOAT
    # number -> SCIENCE
    def number(self):
        if self.token.type == 'INT':
            self.take_token('INT')
        elif self.token.type == 'FLOAT':
            self.take_token('FLOAT')
        elif self.token.type == 'SCIENCE':
            self.take_token('SCIENCE')
        else:
            self.error("Expect value")

    # parameters -> ID EQ number nextpar
    def parameters(self):
        if self.token.type == 'ID':
            self.take_token('ID')
            self.take_token('EQ')
            self.number()
            self.nextpar()
        else:
            pass

    # nextpar -> COMA ID EQ number nextpar
    # nextpar -> eps
    def nextpar(self):
        if self.token.type == 'COMMA':
            self.take_token('COMMA')
            self.take_token('ID')
            self.take_token('EQ')
            self.number()
            self.nextpar()
        else:
            pass

    # comand -> ID[INT] connect comand
    # comand -> GND connect comand
    # comand -> eps
    def command(self):
        if self.token.type == 'ID':
            self.take_token('ID')
            self.take_token('OP_BR2')
            self.take_token('INT')
            self.take_token('CLOSE_BR2')
            self.connect()
            self.command()
        elif self.token.type == 'gnd':
            self.take_token('gnd')
            self.connect()
            self.command()
        elif self.token.type == 'NEWLINE':
            self.take_token('NEWLINE')
            self.command()
        else:
            pass

        # connect -> -- ID[INT] connect
        # connect -> -- GND connect
        # connect -> eps

    def connect(self):

        if self.token.type == 'CONNECT':
            self.take_token('CONNECT')
            if self.token.type == 'ID':
                self.take_token('ID')
                self.take_token('OP_BR2')
                self.take_token('INT')
                self.take_token('CLOSE_BR2')
                self.connect()
            elif self.token.type == 'gnd':
                self.take_token('gnd')
                self.connect()
            else:
                print('connenct something')
        if self.token.type == 'NEWLINE':
            self.take_token('NEWLINE')
            print('connect OK')
