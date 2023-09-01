class CascadingPalindrome:

    def __init__(self, components):
        """initialize the cascading palindrome class"""
        self.components = components
        self.pallindrome = self.check_cascading_pallindrome()
        print(self.pallindrome)


    def is_pallindrome(self,string):
        """a method to check if an object is pallindrome"""
        return string == string[::-1]
        # print(string[0],"\n")
        # print(string[:-1])
        # if string[0] == string[:-1]:
        #
        #     if string == string[::-1]:
        #         return True
        #     else:
        #         return False
        # else:
        #     return False

    def check_cascading_pallindrome(self):
        try:
            if not isinstance(self.components, str):
                raise ValueError("Parameter must be a string")

            lists = self.components.split()
            pallindrome_output = []

            for list in lists:
                if self.is_pallindrome(list):
                    pallindrome_output.append(list)

            #print(pallindrome_output)
            return " ".join(pallindrome_output)

            print(list)
        except ValueError:
            print("Input must be a string")



CascadingPalindrome("1230321 09234 0124210")
CascadingPalindrome(8877)
CascadingPalindrome("JAmes")
CascadingPalindrome("121")
CascadingPalindrome("abcba 567765 455")



