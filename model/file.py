import re
from .field import Field
from .method import Method
from typing import List
from .smali_codes import SmaliCodes


class File():
    """
    Class File
        File Class provides to manipulate smali file
    """

    def __init__(self, raw_code):

        self.raw_code: str = raw_code
        self.file_path: str
        self.code: List[str] = []
        self.fields: List[Field] = []
        self.methods: List[Method] = []
        self.parse()

    def do_method_log(self,package_name:str):
        """
        To Do Method Log for all methods in File
        :param package_name: package name for application
        :return: None
        """
        if "." in package_name:
            package_name = package_name.replace(".","/")
        for method in self.methods:
            if "abstract" in method.signature_line:
                #An abstract method cannot have any instructions
                #contructor
                return
            log_string: str = " ".join(
                ("From file", str(self.file_path), " invoking Method:- ", str(method.signature_line.split().pop())))

            method.add_line(SmaliCodes.log_method.replace("log_string", log_string)
                            .replace(SmaliCodes.package_name, package_name), 0)
            if method.locals < 1:
                method.locals +=1


    def parse(self):
        """
        To parse text in smali file
        :return: None
        """
        code: List[str] = self.raw_code.splitlines()
        i = 0
        while (i < len(code)):
            line = code[i]
            if code[i].startswith(".method"):
                # method starts with line i
                for j in range(i, len(code) + 1):
                    if code[j].startswith(".end method"):
                        # Methods ends with line j
                        method_code = "\n".join([str(line) for line in code[i:j + 1]])
                        i = j + 1
                        method = Method(method_code)
                        self.code.append(method)
                        self.methods.append(method)
                        break



            elif line.startswith(".class"):

                self.file_path = line.split().pop()
                self.code.append(line)

            elif line.startswith(".field"):
                # field found
                field = Field(line)
                self.fields.append(field)
                self.code.append(field)
            else:
                self.code.append(line)

            i += 1

    def __str__(self) -> str:
        """
        All content as string
        :return: All file as string format
        """
        return "\n".join([str(obj) for obj in self.code])
