from django.shortcuts import render

# my views are here.

history = []


def index_view(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        # Turning string to list of numbers
        list_of_numbers = [int(i) for i in list(request.POST.get('input_number'))]
        result = checking_numbers(list_of_numbers)
        history.append(result)
        context = {
            'number': result
        }
        return render(request, 'index.html', context)


def history_view(request):
    list_of_tuples = []
    for item in enumerate(history, start=1):
        list_of_tuples.append(item)
    context = {
        'results': list_of_tuples,
    }
    return render(request, 'history.html', context)


def checking_numbers(guess_numbers):
    fixed_numbers = [5, 1, 2, 9]
    if len(guess_numbers) > len(fixed_numbers):
        return "Too many numbers"
    elif len(guess_numbers) < len(fixed_numbers):
        return "Not enough numbers"
    else:
        if len(fixed_numbers) != len(set(guess_numbers)):
            return "There shouldn't be any duplicates"
        else:
            bulls = 0
            cows = 0
            for num in range(len(fixed_numbers)):
                if guess_numbers[num] == fixed_numbers[num]:
                    bulls += 1
                elif guess_numbers[num] in fixed_numbers:
                    cows += 1
            if bulls == len(fixed_numbers):
                return "You won!"
            else:
                return f"You have got {bulls} 'Bulls' and {cows} 'Cows'"






