"""
Kata: Number of People in the Bus

Description:
Given a list of bus stops represented as pairs of integers,
the first value indicates the number of people getting on
the bus and the second value indicates the number getting off.

Return the number of people remaining on the bus after
the final stop.

Concepts practiced:
- Iterating through lists
- Working with tuples
- Accumulators
- Basic arithmetic operations

Notes:
Practicing how to iterate through structured data
and update a running total.
"""

def number(bus_stops):
    number_of_people = 0
    for i in bus_stops:
        number_of_people += i[0]
        number_of_people -= i[1]
    return number_of_people


# Example usage
if __name__ == "__main__":
    print(number([(10, 0), (3, 5), (2, 1)]))  # 9
