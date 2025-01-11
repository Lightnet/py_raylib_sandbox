# https://www.youtube.com/shorts/n-Rf3EJ_WaU
def my_decorator(func):
  def wrapper():
    print(f"Running {func.__name__}")
    func()
    print("Complete")
  return wrapper

@my_decorator
def do_this():
  print('Doing This')

@my_decorator
def do_that():
  print('Doing That')

do_this()
do_that()

#x = 1

# def plus_one():
#   global x
#   x += 1
#   while True:
#     print("x:", x)
#     x += 1
#     if x > 10:
#       break
    
# plus_one()

def counter_test():
  x = 0
  #print("x:", x)
  while True:
    print("x:", x)
    x += 1
    if x > 10:
      break

counter_test()