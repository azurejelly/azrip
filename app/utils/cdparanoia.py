from subprocess import Popen, PIPE, STDOUT

def spawn(args):
    process = Popen(["cdparanoia", *args], stdout=PIPE, stderr=PIPE, text=True, bufsize=1)