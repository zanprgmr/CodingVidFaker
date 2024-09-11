import argparse
import random
import time
import keyboard


# 0 -> Character by character
# 1 -> Word by word
# 2 -> Just lines
def open_file(file_dir, mode=0):
    try:
        with open(file_dir, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_dir}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    content = content.replace("    ", "\t")

    if mode == 1:
        content = content.replace("\n", " \n ").split(" ")
        content = [word + " " if word != "\n" else word for word in content]
    elif mode == 2:
        content = [line + "\n" for line in content.splitlines()]

    return content


def start_faking(content, wait_time):
    time1, time2 = wait_time[0], wait_time[1]

    for char in content:
        sleep_time = random.uniform(time1, time2)
        print(sleep_time)
        time.sleep(sleep_time)
        keyboard.write(char)


def main():
    parser = argparse.ArgumentParser(description="A script that simulates writing, perfect for faking typing in "
                                                 "coding videos.")
    parser.add_argument("input_file", type=str, help="Directory where the script is going to get the text/code")

    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument("-n", "--normal_mode", action="store_true", help="Writes character by character (default)")
    mode_group.add_argument("-w", "--word_mode", action="store_true", help="Writes word by word")
    mode_group.add_argument("-l", "--line_mode", action="store_true", help="Writes line by line")

    parser.add_argument("-k", "--key", type=str, default="F12", help="Key to start the macro (default: F12)")
    parser.add_argument("-t", "--time", type=str, help="A tuple containing the wait times in seconds. Example: '(2,1)'"
                        "NOTE: It must be written inside quotes like a string")

    args = parser.parse_args()

    input_file = args.input_file
    mode = 1 if args.word_mode else 2 if args.line_mode else 0
    activation_key = args.key

    print(f"Press '{activation_key}' to start typing...")
    keyboard.wait(activation_key)

    print("Typing will start in 3 seconds...")
    time.sleep(3)

    if args.time:
        try:
            wait_time = tuple(map(float, args.time.strip('()').split(',')))
        except ValueError:
            print("Invalid tuple format. Use format like '(2,1)'")
            return
    else:
        wait_time = (0.2, 0.005) if mode == 0 else (0.4, 0.01) if mode == 1 else (2.0, 1.0)

    content = open_file(input_file, mode)
    start_faking(content, wait_time)


if __name__ == "__main__":
    main()
