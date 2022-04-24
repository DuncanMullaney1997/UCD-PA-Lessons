# # Open "alice.txt" and assign the file to "file"
# with open('alice.txt') as file:
#   text = file.read()
#
# n = 0
# for word in text.split():
#   if word.lower() in ['cat', 'cats']:
#     n += 1
#
# print('Lewis Carroll uses the word "cat" {} times'.format(n))
# *
# ----------------------------------------------------------------
# image = get_image_from_instagram()
#
# # Time how long process_with_numpy(image) takes to run
# with timer():
#   print('Numpy version')
#   process_with_numpy(image)
#
# # Time how long process_with_pytorch(image) takes to run
# with timer():
#   print('Pytorch version')
#   process_with_pytorch(image)
#   *
# ----------------------------------------------------------------
# # Add a decorator that will make timer() a context manager
# @contextlib.contextmanager
# def timer():
#   """Time the execution of a context block.
#
#   Yields:
#     None
#   """
#   start = time.time()
#   # Send control back to the context block
#   yield
#   end = time.time()
#   print('Elapsed: {:.2f}s'.format(end - start))
#
# with timer():
#   print('This should take approximately 0.25 seconds')
#   time.sleep(0.25)
#   *
# ----------------------------------------------------------------
# @contextlib.contextmanager
# def open_read_only(filename):
#   """Open a file in read-only mode.
#
#   Args:
#     filename (str): The location of the file to read
#
#   Yields:
#     file object
#   """
#   read_only_file = open(filename, mode='r')
#   # Yield read_only_file so it can be assigned to my_file
#   yield read_only_file
#   # Close read_only_file
#   read_only_file.close()
#
# with open_read_only('my_file.txt') as my_file:
#   print(my_file.read())
#   *
# ----------------------------------------------------------------
# # Use the "stock('NVDA')" context manager
# # and assign the result to the variable "nvda"
# with stock('NVDA') as nvda:
#   # Open "NVDA.txt" for writing as f_out
#   with open('NVDA.txt', 'w') as f_out:
#     for _ in range(10):
#       value = nvda.price()
#       print('Logging ${:.2f} for NVDA'.format(value))
#       f_out.write('{:.2f}\n'.format(value))
# *
# Super stock scraping! Now you can monitor the NVIDIA stock price and
# decide when is the exact right time to buy. Nesting context managers
# like this allows you to connect to the stock market (the CONNECT/DISCONNECT
# pattern) and write to a file (the OPEN/CLOSE pattern) at the same time.
# ----------------------------------------------------------------
# def in_dir(directory):
#   """Change current working directory to `directory`,
#   allow the user to run some code, and change back.
#
#   Args:
#     directory (str): The path to a directory to work in.
#   """
#   current_dir = os.getcwd()
#   os.chdir(directory)
#
#   # Add code that lets you handle errors
#   try:
#     yield
#   # Ensure the directory is reset,
#   # whether there was an error or not
#   finally:
#     os.chdir(current_dir)
#       *

# Excellent error handling! Now, even if someone writes buggy code when
# using your context manager, you will be sure to change the current
# working directory back to what it was when they called in_dir().
# This is important to do because your users might be relying on
# their working directory being what it was when they started the
# script. in_dir() is a great example of the CHANGE/RESET pattern
# that indicates you should use a context manager.
# ----------------------------------------------------------------