def validate_brackets(string):
    stack = []
    opening_bracket_types = ['(', '[', '{']
    closing_bracket_types = [')', ']', '}']

    # Define a helper function to check if two brackets are a valid pair
    def is_valid_pair(opening_bracket, closing_bracket):
        pairs = {')': '(', ']': '[', '}': '{'}
        return pairs.get(closing_bracket) == opening_bracket

    for char in string:
        if char in opening_bracket_types:
            stack.append(char)
        elif char in closing_bracket_types:
            if not stack:
                return False
            opening_bracket = stack.pop()
            if not is_valid_pair(opening_bracket, char):
                return False

    return len(stack) == 0
