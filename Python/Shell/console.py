#!/usr/bin/python3

from cmd import Cmd

class myPromt(Cmd):
    
    def do_hello(self, args):
        """ Says Hello. If you provide a name, it will greet with it. """
        if len(args) == 0:
            name = 'Stranger'
        else:
            name = args

        print("Hello, {}".format(name))
    
    def do_quit(self, args):
        """ Quits the program """
        print("Quitting")
        raise SystemExit

if __name__ == '__main__':
    prompt = myPromt()
    prompt.prompt = '(open_hub)'
    prompt.cmdloop('Starting Point...')