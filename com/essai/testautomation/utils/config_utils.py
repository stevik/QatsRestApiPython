import configparser


def get_property(file_name, property_name, section_name="DEFAULT"):
    config = configparser.ConfigParser()
    config.read(file_name)
    return config.get(section_name, property_name)
