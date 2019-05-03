def fizzbuzz(numero):
    resto3 = (numero % 3)
    resto5 = (numero % 5)

    if (resto3 == 0) and (resto5 == 0):
        return "FizzBuzz"
    elif (resto3 == 0) and (resto5 != 0):
        return "Fizz"
    elif (resto5 == 0) and (resto3 != 0):
        return "Buzz"
    else:
        return numero