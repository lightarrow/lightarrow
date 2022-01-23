from stack import Stack

def match_symbols(symbol_str):
    symbol_pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    openers = symbol_pairs.keys()
    my_stack = Stack()
    index = 0
    while index < len(symbol_str):
        symbol = symbol_str[index]
        if symbol in openers:
            my_stack.push(symbol)
        else:
            # symbol is closer

            # if the stack is empty the symbols are not balanced.
            if my_stack.is_empty():
                return False
            # if there are still item in the Stack, check for a mis-match
            else:
                top_item = my_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False
        index += 1
    if my_stack.is_empty():
        return True
