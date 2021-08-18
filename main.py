import sys
from argparse import ArgumentParser
from os.path import isfile,isdir,basename,join as join_paths,abspath,dirname
from os import walk,system ,remove, getcwd,listdir
from typing import List
import xml.etree.ElementTree as ET
from threading import Thread
from apk import Apk
from settings import Settings
from model.file import File


from model.smali_codes import SmaliCodes
class ApkLogger:
    """
    Class Apk Logger
    """
    DEFAULT_THREADS = 4
    PROGRESS        = 0
    def __init__(self,apk_path:str,
                 package_name,patch):
        # Load Settings
        self.settings = Settings()
        self.is_decompiled:boot = None
        self.files: List[str] = []

        #apk path
        if(isfile(apk_path) and apk_path.endswith(".apk")):
            self.apk = Apk(apk_path=apk_path)
            self.apk.decompile(None)
            self.apk_path = self.apk.get_sources_path()
            self.is_decompiled = True

        elif(isdir(apk_path)):
            self.apk_path = apk_path

        else:
            sys.exit("provided apk path not valid apk file or apk decompiled path --- run again with valid args")
        #Patch
        if patch:
            self.patch = patch
        else:
            sys.exit("patch is required to patch the apk ")

        #Package Name
        if package_name:
            self.package_name = package_name
        else:
            try:
                self.package_name = self.apk.get_package_name()
            except:
                sys.exit("Package Name required(If directory given) --- run again with -p <package_name>")

        # Get All files in list
        self.getfiles(self.apk_path)



    def run(self):
        """
        To Do all work
        :return: None
        """
        self.inject_logging_text_file()
        #Starts thread (Default 4)

        # Taken From:- https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
        files_es = [self.files[i:i + self.DEFAULT_THREADS] for i in range(0, len(self.files), self.DEFAULT_THREADS)]
        ######################################################################################################################

        threads:List[Thread] = []
        for files in files_es:
            thread = Thread(target=self._run,args=(files,),daemon=True)
            threads.append(thread)
            thread.start()
            thread.join()


    def inject_logging_text_file(self):
        """
        Inject logging.smali file in root of sources

        :return: None
        """
        # paste logging.java to root dir
        if not isfile(join_paths(self.apk_path,"logging.smali")):
            if not self.is_decompiled:
                # need find app sources path
                for root, dir, files in walk(self.apk_path, topdown=True):
                    for file in files:
                        if basename(file).endswith(".smali"):
                            with open(join_paths(root, file), 'r') as smali_file:
                                for line in smali_file.read().splitlines():
                                    if line.startswith(".class"):
                                        smali_file_path = line.split().pop().replace("L", "").replace(";", "")
                                        pwd = dirname(smali_file_path)  # pwd from root of app
            else:
                pwd = self.package_name.replace(".","/")

            if pwd:
                with open(join_paths(self.apk_path, "logging.smali"), 'w') as logging_file:
                    logging_file.write(SmaliCodes.smali_file
                                       .replace(SmaliCodes.package_name, self.package_name.replace(".", "/")))


    def _run(self,files:List[str]):
        """
        All modding work
        :param files: List of files that needs to Mod
        :return:
        """
        if self.patch == "log_method":
            for file_path in files:
                with open(file_path, "r") as file_o:
                    file = File(file_o.read())

                file.do_method_log(package_name=self.package_name)
                with open(file_path,'w') as file_o:
                    file_o.write(file.__str__())




    def getfiles(self,path):
        """
        Get all paths of files in a list
        :param path: path of root dir
        :return:
        """
        if isdir(path):
            for root, dirs, files in walk(path, topdown=True):
                for file in files:
                    file_path = join_paths(root, file)
                    if basename(file).endswith(".smali"):
                        self.files.append(file_path)



if __name__ == '__main__':
    argparser = ArgumentParser()
    argparser.add_argument("-i", "--input",
                           required=True,
                           help="Path to apk file or decompiled apk folder")
    argparser.add_argument("-p", "--package_name",
                           required=False,
                           help="Package name of ApK(No need if pass apk root dir as input)")
    argparser.add_argument("-patch", "--patch",
                           required=True,
                           help="log_method---> to log every method apk")

    args = vars(argparser.parse_args())

    apklogger = ApkLogger(apk_path=abspath(args["input"]),
                          package_name =args["package_name"],
                          patch = args["patch"])

    apklogger.run()

