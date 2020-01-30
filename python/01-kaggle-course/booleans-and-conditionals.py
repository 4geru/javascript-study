# ==== Booleans ====
x = True
print(x)
print(type(x))

# ==== Comparison Operations ====
def can_run_for_president(age):
    if(age < 0):
      raise ValueError("age must be grater than 0")
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must "have attained to the Age of thirty-five Years"
    return age >= 35

print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 34-year-old run for president?", can_run_for_president(34))
print("Can a 35-year-old run for president?", can_run_for_president(35))
print("Can a 45-year-old run for president?", can_run_for_president(45))
try:
  print("Can a -1-year-old run for president?", can_run_for_president(-1))
except ValueError as e:
  print(">> Error", e)

print("3.0 == 3 is", 3.0 == 3)
print("'3' == 3 is", '3' == 3)

def is_odd(n):
    return (n % 2) == 1

print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))

# ==== Combining Boolean Values ====
def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35)

print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))


def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)
inspect(-15)

# ==== Boolean conversion ====

print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool(""))

if 0:
    print(0)
elif "spam":
    print("spam")

def quiz_message(grade):
    if grade < 50:
        outcome = 'failed'
    else:
        outcome = 'passed'
    print('You', outcome, 'the quiz with a grade of', grade)

quiz_message(80)
quiz_message(30)

def quiz_message(grade):
    outcome = 'failed' if grade < 50 else 'passed'
    print('You', outcome, 'the quiz with a grade of', grade)

quiz_message(45)