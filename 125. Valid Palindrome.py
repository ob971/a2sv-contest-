def isPalindrome(self, s: str) -> bool:
            new=("",join(i for i in s if i.isnlum())).lower()



            return new==new[::-1]

            
