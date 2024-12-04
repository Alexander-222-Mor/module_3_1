calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return len(string), string.lower(), string.upper()
def in_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if i.lower() == string.lower():
            return True
    return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(in_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(in_contains('cycle', ['recycling', 'cyclic']))
print(calls)


