class SSA:
    def __init__(self, year_of_birth = 0, month_of_birth = 0):
        self.__year_of_birth = year_of_birth
        self.__month_of_birth = month_of_birth
        self.__retirement_age = 0
        self.__retirement_age_months = 0
        self.__retirement_year = 0
        self.__retirement_month = 0

    @property
    def year_of_birth(self):
        return self.__year_of_birth

    @year_of_birth.setter
    def year_of_birth(self, year_of_birth):
        self.__year_of_birth = year_of_birth

    @property
    def month_of_birth(self):
        return self.__month_of_birth
    
    @month_of_birth.setter
    def month_of_birth(self, month_of_birth):
        self.__month_of_birth = month_of_birth

    @property
    def retirement_age_year(self):
        return self.__retirement_age

    @property
    def retirement_age_month(self):
        return self.__retirement_age_months

    @property
    def retirement_year(self):
        return self.__retirement_year

    @property
    def retirement_month(self):
        return self.__retirement_month

    def calculate_retirement_age(self):
        if self.year_of_birth < 1900 or self.year_of_birth > 2020:
            raise ValueError('Year of birth must be greater than 1899 or less than 2021.')
        if self.month_of_birth not in range(1, 13):
            raise ValueError('Month of birth must be between 1 and 12.')

        if self.year_of_birth <= 1937:
            self.__retirement_age = 65
            self.__retirement_age_months = 0
        elif self.year_of_birth == 1938:
            self.__retirement_age = 65
            self.__retirement_age_months = 2
        elif self.year_of_birth == 1939:
            self.__retirement_age = 65
            self.__retirement_age_months = 4
        elif self.year_of_birth == 1940:
            self.__retirement_age = 65
            self.__retirement_age_months = 6
        elif self.year_of_birth == 1941:
            self.__retirement_age = 65
            self.__retirement_age_months = 8
        elif self.year_of_birth == 1942:
            self.__retirement_age = 65
            self.__retirement_age_months = 10
        elif self.year_of_birth >= 1939 and self.year_of_birth <= 1954:
            self.__retirement_age = 66
            self.__retirement_age_months = 0
        elif self.year_of_birth == 1955:
            self.__retirement_age = 66
            self.__retirement_age_months = 2
        elif self.__year_of_birth == 1956:
            self.__retirement_age = 66
            self.__retirement_age_months = 4
        elif self.year_of_birth == 1957:
            self.__retirement_age = 66
            self.__retirement_age_months = 6
        elif self.year_of_birth == 1958:
            self.__retirement_age = 66
            self.__retirement_age_months = 8
        elif self.year_of_birth == 1959:
            self.__retirement_age = 66
            self.__retirement_age_months = 10
        elif self.year_of_birth >= 1960:
            self.__retirement_age = 67
            self.__retirement_age_months = 0

        return self.retirement_age_year, self.retirement_age_month

    def calculate_retirement_date(self):
        self.__retirement_year = self.retirement_age_year + self.year_of_birth
        self.__retirement_month = self.retirement_age_month + self.month_of_birth

        while self.retirement_month > 12:
            self.__retirement_month -= 12
            self.__retirement_year + 1

        return self.retirement_year, self.retirement_month