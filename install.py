import sys, subprocess

#Used for installing any missing packages

def main():
    print('hello')
    #Get the list on current package on system
    reqs = subprocess.check_output([sys.executable, '-m', 'pip','freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    #Another way to install packages but the one on the bottom is faster
    #subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirments.txt"])

    #Get the packages required for the project using the provided TXT file created by us
    required = []
    with open("requirement.txt","r") as file:
        for package in file:
            required.append(package.split("==")[0])

    #Looping over the packages to see which ones are missing and install them
    for package in required:
        if package not in installed_packages:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])



main()



