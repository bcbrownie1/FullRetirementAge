# coding=utf-8
"""SSA Retirement Calculator feature tests."""

import pytest
from ssa import SSA
from pytest_bdd import (
    parsers,
    given,
    scenarios,
    then,
    when,
)

CONVERTERS = {
    'birthyear' : int,
    'birthmonth' : int,
    'retirementageyear': int,
    'retirementagemonth': int,
    'retirementyear': int,
    'retirementmonth': int,
}

scenarios('../features/retirement.feature', example_converters=CONVERTERS)


@given('a birthyear "<birthyear>" and birthmonth "<birthmonth>" are entered', target_fixture="calculator")
def calculator(birthyear, birthmonth):
    return SSA(birthyear, birthmonth)


@when('the retirement age is calculated')
def the_retirement_age_is_calculated(calculator):
    calculator.calculate_retirement_age()
    

@when('the retirement date is calculated')
def the_retirement_date_is_calculated(calculator):
    calculator.calculate_retirement_date()


@then('my retirement age will be "<retirementageyear>" years and "<retirementagemonth>" months')
def my_retirement_age_will_be_retirementageyear_years_and_retirementagemonth_months(calculator, retirementageyear, retirementagemonth):
    assert calculator.retirement_age_year == retirementageyear and calculator.retirement_age_month == retirementagemonth


@then('my retirement date will be in the month "<retirementmonth>" of year "<retirementyear>"')
def my_retirement_date_will_be_in_the_month_retirementyear_of_year_retirementmonth(calculator, retirementmonth, retirementyear):
    assert calculator.retirement_year == retirementyear and calculator.retirement_month == retirementmonth


@then('the program will raise an error')
def the_program_will_raise_an_error(calculator):
    with pytest.raises(ValueError):
        calculator.calculate_retirement_age()

