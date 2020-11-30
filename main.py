from ssa import SSA

def main():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    while True:
        year_of_birth = input('Enter year of birth, or press enter to exit: ')
        if not year_of_birth:
            break

        try:
            year_of_birth = int(year_of_birth)
        except ValueError:
            print('Invalid input.')
            continue

        if year_of_birth >= 1900 and year_of_birth <= 2020:
            while True:
                try:
                    month_of_birth = int(input('Enter month of birth: '))
                    if month_of_birth not in range(1, 13):
                        raise ValueError
                    break
                except ValueError:
                    print('Invalid input.')

            ssa = SSA(year_of_birth, month_of_birth)
            retirement_age, retirement_age_months  = ssa.calculate_retirement_age()
            retirement_year, retirement_month = ssa.calculate_retirement_date()
            print(f'Your full retirement age is {retirement_age} and {retirement_age_months} months\nThis will be in {months[retirement_month-1]} of {retirement_year}')
        else:
            print('Year of birth must be 1900 or greater, up to the current year.')
            continue

if __name__ == '__main__':
    main()