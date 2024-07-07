calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    print((len(string), string.upper(), string.lower()))

def is_contains(string, list_to_search):
    count_calls()
    to_search = False
    for i in list_to_search:
        i = i.lower()
        if string.lower() in i:
            to_search = True
            break
    return to_search

string_info('Capybara')
string_info('Armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)