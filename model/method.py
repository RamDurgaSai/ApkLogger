from typing import List


class Method():

    def __init__(self,
                 raw_code:str):
        self.locals:int = 0
        self.raw_code:str = raw_code
        self.code:List[str] = []
        self.body:List[str] = []


        self.parse()


    def parse(self):
        """
        To parse all Method Body
        :return: None
        """
        self.code = self.raw_code.splitlines()
        for line in self.code:
            if line.startswith(".method"):
                self.signature_line = self.code[0]
            elif line.startswith("    .locals"):
                self.locals = int(self.code[1].split()[1])
            else:
                self.body.append(line)




    def __str__(self):
        """
        All method body as String
        :return: str
        """

        return "".join((
            self.signature_line,"\n",
            "    .locals ",str(self.locals),"\n",
            "\n".join([str(line) for line in self.body])
        ))

    def add_line(self, string , position):
        self.body.insert(position,string)

