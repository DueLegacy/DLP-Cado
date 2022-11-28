import subprocess

test_input_1 = 20337000
test_input_2 = 20337200

process_1 = subprocess.run(
    ["python", "./input.py", f"{test_input_1}"], capture_output=True)
check_result_1= int(process_1.stdout.decode('utf-8').strip('\n'))
assert(check_result_1 == 3849968029612505341)
process_2 = subprocess.run(
    ["python", "./input.py", f"{test_input_2}"], capture_output=True)
check_result_2= int(process_2.stdout.decode('utf-8').strip('\n'))
assert(check_result_2 == 5149236749789271487)

print("Test Passed")