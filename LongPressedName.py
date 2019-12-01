class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i_typed = 0
        i_name = 0
        if not name and typed:
            return False
        if name and not typed:
            return False

        while i_typed < len(typed) and i_name < len(name):
            len_of_char = 1
            while i_name < len(name) - 1:
                if name[i_name] == name[i_name + 1]:
                    i_name += 1
                    len_of_char += 1
                else:
                    break

            len_of_typed_char = 1
            while i_typed < len(typed) - 1:
                if typed[i_typed] == typed[i_typed + 1]:
                    i_typed += 1
                    len_of_typed_char += 1
                else:
                    break

            if len_of_typed_char < len_of_char or typed[i_typed] != name[i_name]:
                return False

            i_name += 1
            i_typed += 1

        if i_typed < len(typed) or i_name < len(name):
            return False
        return True

