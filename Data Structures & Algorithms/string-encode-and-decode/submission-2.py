class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            encoded_string += str(len(string))
            encoded_string += "!"
            encoded_string += string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        pointer = 0
        decoded_strings = list()

        while pointer < len(s):
            start_num = pointer
            while s[pointer] != "!":
                pointer +=1
            string_length = int(s[start_num:pointer])
            decoded_strings.append(s[pointer+1:pointer+1+string_length])
            pointer = pointer + string_length + 1

        return decoded_strings