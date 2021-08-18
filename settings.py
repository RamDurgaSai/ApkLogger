import json


class Settings:

    def __init__(self):
        self.load_setting()

    def load_setting(self):
        with open("config.json", "r", encoding="utf-8") as config_file:
            settings = json.load(config_file)

        if settings["java_path"]:
            self.java_path = settings["java_path"]
        if settings["apkTool_path"]:
            self.apkTool_path = settings["apkTool_path"]
        if settings["uberApkSigner_path"]:
            self.signer_path = settings["uberApkSigner_path"]
            signature = settings["signature"]
            self.keystore_path = signature["keystore_path"]
            self.keystore_password = signature["keystore_password"]
            self.keystore_alias = signature["alias"]
            self.keystore_alias_password = signature["alias_password"]
            self.zip_align = signature["zip_align"]
