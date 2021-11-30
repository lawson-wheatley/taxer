import random


def randomize(length):
    """
    :param lenn:
    :return list of ages between 0-100:
    """
    people = []
    for i in range(length):
        people.append(random.randint(0, 100))
    return people


def taxpeople(people):
    """
    :param people:
    :return taxes:
    """
    taxer = []
    for person in people:  # Traverses list
        taxer.append(tax(person))  # Applies tax
    return taxer


def tax(personage):
    """
    :param personage:
    :return tax:
    """
    tax = 0  # No need for check between 0-20
    if 20 < personage <= 60:  # Checks if person age is between 20 and 60
        tax = 10
    elif 60 < personage <= 100:  # Checks if person age is between 60 and 100
        tax = 5
    return tax


def run():
    q = input("Do you want a random data set (y/n)? ").lower()
    people = []
    if q == 'y':
        length = int(input("How many people are you taxing? "))
        people = randomize(length)
    elif q == 'n':
        people = list(map(int, input("Please enter in the dataset(ex: 0,2,7,24,63 no spaces): ").split(",")))
    people_names = input("What are the names of the people you're taxing (John,Joe etc. no spaces)? ").split(",")
    taxes = taxpeople(people)
    for i in range(len(people)):
        print(people_names[i] + ", " + str(people[i]) + ", has $" + str(taxes[i]) + " in taxes.")


run()
