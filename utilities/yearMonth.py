from datetime import date
from dateutil.relativedelta import relativedelta


class YearMonth:
    @staticmethod
    def get_year_month(self, month_increment):
        today = date.today()
        year_month_day = today + relativedelta(months=+month_increment)
        year_month_day_tostring = str(year_month_day)
        year_month = year_month_day_tostring[:7]
        return year_month
