

# try:
#     num = int(input("Enter The number"))
# except ValueError:
#     print("That is not a valid number")
# else:
#     print("You entered number {num}")
# finally:
#     print("Excution Complete")


def safe_devision(a,b):

    try:
        result  =a/b
    except ZeroDivisionError:
        print("Can not be devided by zero")
        return None
    except TypeError:
        print("Invalid Input Types")
        return None
    else:
        return result
    finally:
        print("Devision Attempt Finished")

safe =safe_devision(10,2)
safe1 =safe_devision(10,"gashaw")
print(safe)
