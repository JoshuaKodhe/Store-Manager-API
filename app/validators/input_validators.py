class InputValidator:
    @staticmethod
    def valid_string(user_input):
        if isinstance(user_input, str):
            return user_input
        return False

    @staticmethod
    def valid_number(user_input):
        if isinstance(user_input, (int, float)):
            if user_input >= 1:
                return user_input
        return False
