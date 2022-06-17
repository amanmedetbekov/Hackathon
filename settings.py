class Settings:
    TOKEN = 'Bearer keyZZzXXQRlBtj3D0'
    TABLE_NAME = 'cars'


    def get_url(self):
        return f'https://api.airtable.com/v0/appIEWFojbyFd9TwK/{self.TABLE_NAME}/'

settings = Settings()


# URL = '?maxRecords=3&view=Grid%20view'

