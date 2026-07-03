import configparser

config = configparser.RawConfigParser()
config.read('C:\\Users\\dmana\\OneDrive\\Desktop\\Selenium\\My_Project_class_June\\configurations\\config.ini')

class ReadConfig:

    @staticmethod
    def get_base_url():
        base_url = config.get('common info', 'url')
        return base_url

    @staticmethod
    def get_username():
        username = config.get('common info', 'email')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
    #
    @staticmethod
    def get_invalid_username():
        username = config.get('common info', 'email12')
        return username

    @staticmethod
    def get_invalid_password():
        password = config.get('common info', 'password12')
        return password
