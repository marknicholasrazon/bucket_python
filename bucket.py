from colorama import Fore, Style
import os
import time
import pyttsx3
import mysql.connector

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_table(header, data):
    print('-' * 50)
    print(f'| {Fore.BLUE}{header:<48}{Style.RESET_ALL} |')
    print('-' * 50)
    for line in data:
        print(f'| {line:<48} |')
    print('-' * 50)
    time.sleep(1)

def bucket_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    num_buckets = max_value - min_value + 1
    buckets = [[] for _ in range(num_buckets)]

    # Place elements into buckets
    for item in arr:
        index = item - min_value
        buckets[index].append(item)

    # Sort each bucket and visualize the process
    operations = 0  # Initialize the number of operations
    for i, bucket in enumerate(buckets):
        sorted_bucket = sorted(bucket)
        operations += len(bucket)**2  # Counting operations (number of elements squared)
        print_table(f'Bucket {i}', [f'{sorted_bucket}'])

    # Concatenate sorted buckets to get the final result
    sorted_data = []
    for bucket in buckets:
        sorted_data.extend(bucket)

    return sorted_data, operations

def analyze_time_complexity(input_data, sorted_data, operations, elapsed_time):
    n = len(input_data)
    if operations < n: 
        return "Best Case"
    elif operations > n**2: 
        return "Worst Case"
    else:
        if elapsed_time < 1:  
            return "Best Case"
        elif elapsed_time > 10:  
            return "Worst Case"
        else:
            return "Average Case"
        
# Speak
introduction = "What is bucket sort?"
intro_say = "Bucket sort is a comparison-based sorting algorithm that distributes the elements into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm."
intro_presentation = "\nHere's a visual presentation how bucket sort works"
intro_step1 = "Let's say we have the following list of numbers:"
intro_step1_visual1 = "[0.32, 0.45, 0.12, 0.67, 0.88, 0.01, 0.56, 0.71, 0.85, 0.23]"
intro_step2 = "Distribute elements into buckets:"
intro_step2_visual1 = "Bucket 0: [0.01]"
intro_step2_visual2 = "Bucket 1: [0.12]"
intro_step2_visual3 = "Bucket 2: [0.23]"
intro_step2_visual4 = "Bucket 3: [0.32]"
intro_step2_visual5 = "Bucket 4: [0.45]"
intro_step2_visual6 = "Bucket 5: [0.56]"
intro_step2_visual7 = "Bucket 6: [0.67]"
intro_step2_visual8 = "Bucket 7: [0.71]"
intro_step2_visual9 = "Bucket 8: [0.88, 0.85]"
intro_step3 = "Sort each bucket individually, here they are already sorted."
intro_step3_visual1 = "Bucket 0: [0.01]"
intro_step3_visual2 = "Bucket 1: [0.12]"
intro_step3_visual3 = "Bucket 2: [0.23]"
intro_step3_visual4 = "Bucket 3: [0.32]"
intro_step3_visual5 = "Bucket 4: [0.45]"
intro_step3_visual6 = "Bucket 5: [0.56]"
intro_step3_visual7 = "Bucket 6: [0.67]"
intro_step3_visual8 = "Bucket 7: [0.71]"
intro_step3_visual9 = "Bucket 8: [0.85, 0.88]"
intro_step4 = "Concatenate the sorted buckets:"
intro_step4_visual1 = "[0.01, 0.12, 0.23, 0.32, 0.45, 0.56, 0.67, 0.71, 0.85, 0.88]"
intro_final = "Here's how we implement bucket sort in our data"

clear_console()

time.sleep(1)
engine = pyttsx3.init()

engine.say(introduction)
print(Fore.YELLOW + introduction + Style.RESET_ALL)
engine.runAndWait()

time.sleep(1)

engine.say(intro_say)
print(intro_say)
engine.runAndWait()

time.sleep(1)

engine.say(intro_presentation)
print(Fore.YELLOW + intro_presentation + Style.RESET_ALL)
engine.runAndWait()

time.sleep(1)

engine.say(intro_step1)
print(intro_step1)
engine.runAndWait()

time.sleep(1)

print("\n")
print(intro_step1_visual1)

time.sleep(1)

engine.say(intro_step2)
print("\n")
print(Fore.YELLOW + intro_step2 + Style.RESET_ALL)
engine.runAndWait()

time.sleep(1)

print("\n")
print(intro_step2_visual1)
time.sleep(0.5)
print(intro_step2_visual2)
time.sleep(0.5)
print(intro_step2_visual3)
time.sleep(0.5)
print(intro_step2_visual4)
time.sleep(0.5)
print(intro_step2_visual5)
time.sleep(0.5)
print(intro_step2_visual6)
time.sleep(0.5)
print(intro_step2_visual7)
time.sleep(0.5)
print(intro_step2_visual8)
time.sleep(0.5)
print(intro_step2_visual9)

time.sleep(1)

engine.say(intro_step3)
print("\n")
print(Fore.YELLOW + intro_step3 + Style.RESET_ALL)
engine.runAndWait()

time.sleep(1)

print("\n")
print(intro_step3_visual1)
time.sleep(0.5)
print(intro_step3_visual2)
time.sleep(0.5)
print(intro_step3_visual3)
time.sleep(0.5)
print(intro_step3_visual4)
time.sleep(0.5)
print(intro_step3_visual5)
time.sleep(0.5)
print(intro_step3_visual6)
time.sleep(0.5)
print(intro_step3_visual7)
time.sleep(0.5)
print(intro_step3_visual8)
time.sleep(0.5)
print(intro_step3_visual9)

time.sleep(1)

engine.say(intro_step4)
print("\n")
print(Fore.YELLOW + intro_step4 + Style.RESET_ALL)
engine.runAndWait()

time.sleep(1)

print(Fore.GREEN + intro_step4_visual1 + Style.RESET_ALL)

time.sleep(1)

engine.say(intro_final)
print("\n")
print(Fore.YELLOW + intro_final + Style.RESET_ALL)
engine.runAndWait()

# Connect to your database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python'
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define and execute your SQL query
query = "SELECT * FROM product ORDER BY rand()"
cursor.execute(query)

# Fetch the data
data = cursor.fetchall()

# Close the cursor and connection
cursor.close()
conn.close()

# Extract the price with index 4 as input data for bucket sort
input_data = [row[0] for row in data]

# Example usage:
print('-' * 50)
print(f'| {Fore.GREEN}Original data: {input_data}{" " * 24}{Style.RESET_ALL}|')
print('-' * 50)
time.sleep(3)
start_time = time.time()
sorted_data, operations = bucket_sort(input_data)
end_time = time.time()
elapsed_time = end_time - start_time
time.sleep(3)
print('-' * 50)
print(f'| {Fore.YELLOW}Sorted data: {sorted_data}{" " * 26}{Style.RESET_ALL}|')
print('-' * 50)

time.sleep(3)

# Analysis
n = len(input_data)
print(f"{Fore.YELLOW}Number of elements (n):{Style.RESET_ALL} {n}")
print(f"{Fore.YELLOW}Elapsed Time:{Style.RESET_ALL} {elapsed_time} seconds")
print(f"{Fore.YELLOW}Time Complexity Case:{Style.RESET_ALL} {analyze_time_complexity(input_data, sorted_data, operations, elapsed_time)}")
print(f"{Fore.YELLOW}Average Case:{Style.RESET_ALL} O(n^2) [In this case, as elements are distributed uniformly]")
print(f"{Fore.YELLOW}Best Case:{Style.RESET_ALL} O(n) [When all elements are already sorted in buckets]")
print(f"{Fore.YELLOW}Worst Case:{Style.RESET_ALL} O(n^2) [When all elements go to a single bucket]")
print(f"{Fore.YELLOW}Number of Operations:{Style.RESET_ALL} {operations}")
print(f"{Fore.YELLOW}Space Complexity:{Style.RESET_ALL} O(n+k) [n for the input list, k for the number of buckets]")
time.sleep(1)
engine.say("The time complexity case of the program is " + analyze_time_complexity(input_data, sorted_data, operations, elapsed_time))
engine.runAndWait()
