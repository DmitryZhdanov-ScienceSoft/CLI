from  import prompt
from prompt_toolkit.completion import WordCompleter


def main():
    commands = WordCompleter(['start', 'stop', 'status', 'exit'], ignore_case=True)

    while True:
        command = prompt('> ', completer=commands)
        if command == 'exit':
            break
        elif command == 'start':
            print("Starting...")
        elif command == 'stop':
            print("Stopping...")
        elif command == 'status':
            print("Status: OK")
        else:
            print(f"Unknown command: {command}")


if __name__ == '__main__':
    main()
