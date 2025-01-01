import time
import threading


numbers = [1, 2, 3]

# Without multithreading
# def square(nums):
#   for n in nums:
#     time.sleep(0.2)
#     print("square--->", n*n)

# def cube(nums):
#   for n in nums:
#     time.sleep(0.2)
#     print("Cube----->", n*n*n)  

# if __name__ == "__main__":
#   start_time = time.time()

#   square(numbers)
#   cube(numbers)

#   print("Completed in: ", time.time() - start_time)



# With multithreading
def square(nums):
  for n in nums:
    time.sleep(0.2)
    print("square--->", n*n)

def cube(nums):
  for n in nums:
    time.sleep(0.2)
    print("Cube----->", n*n*n)


if __name__ == "__main__":
  start_time = time.time()

  thread_1 = threading.Thread(target=square, args=(numbers,))
  thread_2 = threading.Thread(target=cube, args=(numbers,))

  thread_1.start()
  thread_2.start()

  thread_1.join()
  thread_2.join()

  print("Completed in: ", time.time() - start_time)