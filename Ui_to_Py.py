import fnmatch
import os

Current_Directory = os.path.dirname(os.path.realpath(__file__))

try:
    def find(pattern, path):
        result = []
        for root, _, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        return result


    search_result = find('*.ui', Current_Directory)

    if search_result:
        try:
            search_result = search_result[0].replace(f"{Current_Directory}\\", "")
            os.system(f'cmd /c "pyuic5 -x {search_result} -o New_python_file.py"')
            print("\nDescription: (.ui) file converted to (.py) successfully")
        except:
            print("\nDescription: can't convert (.ui) file to (.py)")
    else:
        print("\nDescription: (.ui) file not exist")
except:
    print("\nDescription: can't search for (.ui) file")

input("Press enter to exit...")
