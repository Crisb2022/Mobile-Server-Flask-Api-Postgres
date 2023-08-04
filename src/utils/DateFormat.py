import datetime

class DateFormat():
    @classmethod # Podemos usarlo sin instanciar
    def convert_date(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')