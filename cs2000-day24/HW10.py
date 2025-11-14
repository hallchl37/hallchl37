def lemonade_stand_1(cups_sold):
    """
    Stand 1: Buys 16 fl oz bottles at $2 each, sells 4 fl oz cups at $1 each.

    Args:
    cups_sold: Amount of cups sold

    Returns:
    Total profit

    """
bottles_needed = (cups_sold + 3) // 4
if cups_sold % 4 != 0:
    bottles_needed = cups_sold // 4 + 1
else:
    bottles_needed = cups_sold // 4

    cost = bottles_needed * 2
    revenue = cups_sold * 1
    profit = revenue - cost

    return profit

def lemonade-stand_2(cups_sold):
"""
Stand 2: Buys 640 fl oz (5 gallon) container at $20, sells 4 fl oz cups at $0.75 each.
Stops when they run out (max 160 cups from 640 oz).

Args:
cups_sold: Amount of cups attempted to be sold

Returns:
Total profit
"""

max_cups = 640 // 4

actual_cups_sold = min(cups_sold, max_cups)
cost = 20
revenue = actual_cups_sold * 0.75
profit = revenue - cost

return profit

def which_stand-better(cups_sold):
"""
Determines which stand makes more profit for a given number of cups.

Args:
cups_sold: Amount of cups sold

Returns:
1 if stand 1 is better, 2 if stand 2 is better, if tied 0
"""
profit_1 = lemonade_stand_1(cups_sold)
profit_2 = lemonade_stand_2(cups_sold)

if profit_1 > profit_2:
    return 1
elif profit_2 > profit_1:
    return 2
else:
    return 0

def tick(time_str):
    """
    Advances time by one second in HH::MM::SS formatting.

    Args:
    time_str: Time string in format "HH:MM:SS"

    Returns:
    New time string one second later
    """
    parts = tine_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])

    seconds += 1

    if seconds >= 60:
        seconds = 0
        minutes += 1

    if minutes >= 60:
        minutes = 0
        minutes += 1
    
    if hours >= 24:
        hours = 0
    
    return f "{hours:02d}:{minutes:02d}:{seconds:02d}"

    def add-prefix(prefix, string_list):
    """
    Adds a prefix to each string in the list.

    Args:
    prefix: String to add to the front
    string_list: List of strings

    Returns:
    List of strings with prefix added
    """
    return [prefix + s for s in string_list]

def remove_odd_length_strings(string_list):
    """
    Filters out strings with an odd length.

    Args:
    string_list: List of strings

    Returns:
    List containing only strings with an even length
    """
    return [s for s in string_list len(s) % 2 == 0]

x = 10

def change_x():
    global x
    x = 50

    change_x()
    print(x)

if __name__ == "__main__":
    print("=== Problem 1 Tests===")
    print(f"Stand 1, 10 cups: ${lemonade_stand_1(10)}")
    print(f"Stand 1, 20 cup: ${lemonade_stand_1(20)}")
    print(f"Stand 2, 10 cups: $"{lemonade_stand_2(20)})
    print(f"Stand 2, 100 cups: ${lemonade_stand_2(100)}")
    print(f"Stand 2, 200 cups: ${lemonade_stand_2(200)}")
    print(f"Better stand for 50 cups: {which_stand_better(50)}")

print("\n=== Problem 2 Test===")
print(f"tick('23:59:59') = {tick('23:59:59')}")

print("\n=== Problem 3 Test ===")
print(f"add_prefix('pre_', ['fix', 'test']) = {add_prefix('pre_', ['fix', 'test'])}")

print("\n=== Problem 4 Test ===")
print(f"remove_odd_length_strings(['a', 'ab', 'abc', 'abcd']) = {remove_odd_length_strings(['a', 'ab', 'abc', 'abcd'])}")