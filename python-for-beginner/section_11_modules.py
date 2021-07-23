"""
#Python modules are files with extension .py
import module_name
module_name.method_name()

# import one sing method name
from module_name import method_name method_name()

# import attibute from other modules
from module_name import method_name
from module_name import method_name1, method_nameN
"""

# Don't do this!
from time import *

def main():
    import abc
    from time import asctime
    print(asctime())
    print('-' * 10)

    # import multiple methods
    from time import asctime, sleep
    print(asctime())
    sleep(1)
    print(asctime())
    print('-' * 10)

    # Check inside a module
    import time
    print('method & propertes inside time module: {}'.format(dir(time)))
    print('-' * 10)

    # Module search path
    """sys.path - returns the search path for modules."""
    import sys
    def show_system_path():
        for path in sys.path:
            print(path)
    show_system_path()
    print('-' * 10)

    # Add custom system path - like adding library in Java
    sys.path.append('/Users/jason/python')
    show_system_path()
    print('-' * 10)

    # PYTHONPATH environment variable
    """
    Mac/Linux:
    PYTHONPATH=path1:pathN

    Windows:
    PYTHONPATH=path1;pathN
    """

    # Recommendation
    """
    Check what Python provided
    https://docs.python.org/3/library/
    """
    # Example of using existed modules - sys
    import sys
    file_name = 'test.txt'
    try:
        with open(file_name) as test_file:
            for line in test_file:
                print(line)
    except Exception as ex:
        print('Could not open {}. More details: {}'.format(file_name, ex))
        # sys.exit(1)
    print('-' * 10)

    # Importing other custom modules
    """
    Pattern:
    from folder import file
    """
    from say_hi_modules import say_hi
    say_hi.say_hi()

    from say_hi_modules import say_hi_2
    say_hi_2.say_hi()
    print('-' * 10)
    """
    Unexpected print function are executed by say_hi_2 because
    the print method is put in the file
    """
    """
    To fix the above behavior of say_hi_2 module
    We create the say_hi_3 with a little improvement
    """
    from say_hi_modules import say_hi_3
    say_hi_3.say_hi()
    print('-' * 10)

    # Exercise
    import section_3_string_and_variables as section_3
    section_3.exec_exercise3()
    section_3.cat_say('Pet me and I will purr.')
    section_3.cat_say('Feed me.')
    section_3.cat_say('Pet me.')
    section_3.cat_say('Purr. Purr.')

if __name__ == '__main__':
    main()