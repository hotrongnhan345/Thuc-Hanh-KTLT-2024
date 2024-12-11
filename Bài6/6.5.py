print("Sinh Viên: Hồ Trọng Nhân")
print("MSSV: 235752021610123")
class ReverseWords:
    def _init_(self, input_string):
        self.input_string = input_string
    def reverse(self):
        words = self.input_string.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
if _name_ == "_main_":
   input_string =  'hello .py'
   reverser = ReverseWords(input_string)
   reverded_string = reverder.reverse()
   print(f"Chuỗi dảo ngược: '(reversed_steing)'")
