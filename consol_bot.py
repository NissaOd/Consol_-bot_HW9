DB = {}

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Wrong Index"
        except KeyError:
            return "Wrong Key"
        except ValueError:
            return "Wrong Value"
        except TypeError:
            return "Wrong Type"
    return wrapper

@input_error
def greeting(*args):
    return "How can I help you?"

@input_error
def exit(*args):
    return "Good bye!"

@input_error
def add(*args):
    name = args[0]
    name = name.title()
    phone = args[1]
    DB[name] = phone
    return f'Contact {name} add successful'

@input_error
def change(*args):
    name = args[0]
    name = name.title()
    phone = args[1]
    for k in DB.keys():
        if k == name:
                DB[name] = phone
                return f'Contact {name} was changed successful'
    return f'Contact {name} not found'

@input_error
def phone(*args):
    name = args[0]
    t_name = name.title()
    for k in DB.keys():
        if k == t_name:
            return f'Contact {k}: {DB[k]}'

@input_error
def show_all(*args):
    lst = ['{:^10}:{:>10}'.format(k,v) for k,v in DB.items()]
    return "\n".join(lst)
    


COMMANDS = {exit:["exit", ".", "bye"], add:["add", "добавь", "додай"], show_all:["show all", "show"],
            greeting:['hello', 'hi', 'Привет'], change:['change', 'изменить'], phone:['phone', 'телефон']}


def parse_command(user_input:str):
    for k,v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(" ")

@input_error
def main():
    while True:
        user_input = input(">>>")
        result, data = parse_command(user_input)
        print(result(*data))
        if result is exit:
            break
        #else:
        #    print('Unknown command! Enter again!\n') 


if __name__ == "__main__":
    main()