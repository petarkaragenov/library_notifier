from datetime import datetime, timedelta


class BookDates:
    def __init__(self, dates):
        self.datetimes = [datetime.strptime(date, "%d.%m.%Y").replace(hour=23, minute=59, second=59) for date in dates]
        self.today = datetime.now()
        self.rented = {}

    def populate_rented(self):
        for entry in self.datetimes:
            days = int((entry - self.today).days)
            if days in self.rented:
                self.rented[days] += 1
            else:
                self.rented[days] = 1

    def check_if_plural(self, expiring_soon):
        if self.rented[expiring_soon] == 1:
            return ("is", "")
        else:
            return ("are", "s")

    def make_warning(self):
        self.populate_rented()

        expiring_soon = sorted(self.rented)[0]
        be, s = self.check_if_plural(expiring_soon)
        warning = f"There {be} {self.rented[expiring_soon]} book{s} to be extended by "

        if expiring_soon == 0:
            warning += "today"
        elif expiring_soon == 1:
            warning += "tomorrow"
        else: 
            warning += (self.today + timedelta(expiring_soon)).strftime("%A, %d.%m.%y")
        
        return warning
