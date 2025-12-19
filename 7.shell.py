import subprocess
import os
import sys

def run_shell():
    while True:
        try:
            cmd_input = input("$ ").strip()
            
            if not cmd_input:
                continue
            if cmd_input.lower() in ["exit", "quit"]:
                break
                
            if "|" in cmd_input:
                commands = cmd_input.split("|")
                processes = []
                for i, cmd in enumerate(commands):
                    args = cmd.strip().split()
                    if i == 0:
                        p = subprocess.Popen(args, stdout=subprocess.PIPE, text=True)
                    elif i == len(commands) - 1:
                        p = subprocess.Popen(args, stdin=processes[-1].stdout, text=True)
                    else:
                        p = subprocess.Popen(args, stdin=processes[-1].stdout, stdout=subprocess.PIPE, text=True)
                    processes.append(p)
                
                for p in processes[:-1]:
                    p.stdout.close()
                
                out, err = processes[-1].communicate()
                if out:
                    print(out, end="")
                continue

            args = cmd_input.split()
            stdin = None
            stdout = None

            if ">" in args:
                idx = args.index(">")
                stdout = open(args[idx + 1], "w")
                args = args[:idx]

            if "<" in args:
                idx = args.index("<")
                stdin = open(args[idx + 1], "r")
                args = args[:idx]

            subprocess.run(args, stdin=stdin, stdout=stdout)
            
            if stdin: stdin.close()
            if stdout: stdout.close()

        except FileNotFoundError:
            print(f"Command not found: {cmd_input}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_shell()