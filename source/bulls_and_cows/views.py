from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, 'index.html')




class CheckNum:
    def __init__(self, guess_list: list) -> list:
        self.guess_list = guess_list
        self.fixed_list = [5, 1, 2, 9]

    def check_for_big_num(self):
        for number in self.guess_list:
            if number > 9 or number < 0:
                return "Number cannot be higher than 9 or less than 0"

    def check_lenght(self):
        if len(self.guess_list) > len(self.fixed_list):
            return "Too many numbers"
        elif len(self.guess_list) < len(self.fixed_list):
            return "Not enough numbers"

    def check_for_duplicates(self):
        if len(self.fixed_list) != len(set(self.guess_list)):
            return "There shouldn't be any duplicates"

    def validate(self):
        message = None
        if self.check_lenght():
            message = self.check_lenght()
        elif self.check_for_big_num():
            message = self.check_for_big_num()
        elif self.check_for_duplicates():
            message = self.check_for_duplicates()
        return message

    def finding_bulls(self):
        if not self.check_for_big_num() and not self.check_lenght() and not self.check_for_duplicates():
            bulls = 0
            cows = 0
            for num in range(len(self.fixed_list)):
                if self.guess_list[num] == self.fixed_list[num]:
                    bulls += 1
                elif self.guess_list[num] in self.fixed_list:
                    cows += 1
            if bulls == len(self.fixed_list):
                return "You won!"
            else:
                return f"You have got {bulls} 'Bulls' and {cows} 'Cows'"
