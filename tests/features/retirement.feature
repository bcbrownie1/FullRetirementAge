Feature: SSA Retirement Calculator
    I'm getting pretty old. I want to find out when I can start drawing my retirement benefits from the Social Security Administration.

    Scenario Outline: Calculate retirement age
        Given a birthyear "<birthyear>" and birthmonth "<birthmonth>" are entered
        When the retirement age is calculated
        Then my retirement age will be "<retirementageyear>" years and "<retirementagemonth>" months

        Examples:
        | birthyear | birthmonth | retirementageyear | retirementagemonth |
        | 2001      | 7          | 67                | 0                  |
        | 1900      | 1          | 65                | 0                  |
        | 1938      | 1          | 65                | 2                  |
        | 1939      | 1          | 65                | 4                  |
        | 1940      | 1          | 65                | 6                  |
        | 1941      | 1          | 65                | 8                  |
        | 1942      | 1          | 65                | 10                 |
        | 1943      | 1          | 66                | 0                  |
        | 1954      | 1          | 66                | 0                  |
        | 1955      | 1          | 66                | 2                  |
        | 1956      | 1          | 66                | 4                  |
        | 1957      | 1          | 66                | 6                  |
        | 1958      | 1          | 66                | 8                  |
        | 1959      | 1          | 66                | 10                 |
        | 2020      | 1          | 67                | 0                  |

    Scenario Outline: Calculate retirement date
        Given a birthyear "<birthyear>" and birthmonth "<birthmonth>" are entered
        When the retirement age is calculated
        And the retirement date is calculated
        Then my retirement date will be in the month "<retirementmonth>" of year "<retirementyear>"

        Examples:
        | birthyear | birthmonth | retirementyear | retirementmonth |
        | 2001      | 7          | 2068           | 7               |
        | 1900      | 1          | 1965           | 1               |
        | 1938      | 1          | 2003           | 3               |
        | 1939      | 1          | 2004           | 5               |
        | 1940      | 1          | 2005           | 7               |
        | 1941      | 1          | 2006           | 9               |
        | 1942      | 1          | 2007           | 11              |
        | 1943      | 1          | 2009           | 1               |
        | 1954      | 1          | 2020           | 1               |
        | 1955      | 1          | 2021           | 3               |
        | 1956      | 1          | 2022           | 5               |
        | 1957      | 1          | 2023           | 7               |
        | 1958      | 1          | 2024           | 9               |
        | 1959      | 1          | 2025           | 11              |
        | 2020      | 1          | 2087           | 1               |

    Scenario Outline: Invalid retirement age
        Given a birthyear "<birthyear>" and birthmonth "<birthmonth>" are entered
        Then the program will raise an error
        
        Examples:
        | birthyear | birthmonth |
        | 1899      | 0          |
        | 2021      | 13         |