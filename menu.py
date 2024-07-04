import cmd
import os
import subprocess


class CLIMenu(cmd.Cmd):
    intro = "Welcome to the CLI Menu. Type help or ? to list commands.\n"
    prompt = "(CLI Menu) "

    def do_file_manager(self, arg):
        """Run the File Manager"""
        print("Starting File Manager...")
        try:
            subprocess.run(["python", "file_manager.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running File Manager: {e}")
        except FileNotFoundError:
            print("Error: file_manager.py not found")

    def do_midjourney(self, arg):
        """Run CLI App 2"""
        print("Running MidJourney...")
        try:
            subprocess.run(["python", "midjourney_cli.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running MidJourney: {e}")
        except FileNotFoundError:
            print("Error: midjourney_cli.py not found")
        # Add your code to run CLI App 2 here

    def do_show_image(self, arg):
        """Run CLI App 3"""
        print("Show Image...")
        try:
            subprocess.run(["python", "image.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running Image: {e}")
        except FileNotFoundError:
            print("Error: image.py not found")

    def do_ask_gpt4o(self, arg):
        """Ask a question"""
        try:
            subprocess.run(["python", "ask_rich.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running Ask Rich: {e}")

    def do_prompt_toolkit(self, arg):
        """Ask a question"""
        try:
            subprocess.run(["python", "promt_cli.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running Ask Rich: {e}")

    def do_progress_bar(self, arg):
        """Run the Progress Bars"""
        try:
            subprocess.run(["python", "progress_bar.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running Ask Rich: {e}")

    def do_snake(self, arg):
        """Run the Snake Game"""
        try:
            subprocess.run(["python", "snake.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running Ask Rich: {e}")

    def do_plot(self, arg):
        """Show the Plot"""
        try:
            subprocess.run(["python", "plots_termplotlib.py", "show-plot"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running Ask Rich: {e}")

    def do_hist(self, arg):
        """Show the Plot"""
        try:
            subprocess.run(["python", "plots_termplotlib.py", "show-histogram"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running Ask Rich: {e}")

    def do_exit(self, arg):
        """Exit the program"""
        print("Goodbye!")
        return True


if __name__ == '__main__':
    CLIMenu().cmdloop()
