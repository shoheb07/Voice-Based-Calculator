def calculate(command):
    command = command.lower()

    command = command.replace("plus", "+")
    command = command.replace("minus", "-")
    command = command.replace("multiplied by", "*")
    command = command.replace("times", "*")
    command = command.replace("divided by", "/")

    try:
        result = eval(command)
        return result
    except:
        return "Invalid expression"
