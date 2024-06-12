import subprocess

def test_code_formatting():
    with open('calc_functions.py') as file:
        code = file.read()
    formatted_code = subprocess.check_output(['black', '-', '--quiet', '-'], input=code.encode()).decode()
    assert code == formatted_code