import os
import configparser
from exception.MyCustomException import MyCustomException
from constants.FrameworkConstants import FrameworkConstants

config = configparser.RawConfigParser()
file_path = os.path.join(FrameworkConstants.PROJECT_ROOT, "Configuration", "config.ini")
config.read(file_path)

class ReadConfig():

    @staticmethod
    def getProperty(section, option):
        section_value = section.value
        option_value = option.value
        try:
            value = config.get(section_value, option_value)
            print(value)
            return value
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            raise MyCustomException(f"Property '{option}' in section '{section}' is not found. Please check the config file.") from e


