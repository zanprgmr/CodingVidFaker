
# CodingVidFaker

CodingVidFaker is a Python script designed to simulate typing for coding videos. It helps create realistic typing effects by faking keystrokes at adjustable speeds and modes. Ideal for use in video tutorials, presentations, and coding demonstrations.

## Features

- **Modes**: Choose between character-by-character, word-by-word, or line-by-line typing.
- **Adjustable Timing**: Customize the wait time between keystrokes.
- **Activation Key**: Start the typing simulation with a customizable activation key.

## Installation

1. Clone the repository:

   `git clone https://github.com/yourusername/CodingVidFaker.git`

2. Navigate to the project directory:

   `cd CodingVidFaker`

3. Install the required library:

   `pip install keyboard`

## Usage

Run the script with the following command:

   `python coding_vid_faker.py [options] <input_file>`

### Arguments

- `input_file`: The path to the file containing the text/code to be faked.

### Options

- `-n`, `--normal_mode`: Write character by character (default).
- `-w`, `--word_mode`: Write word by word.
- `-l`, `--line_mode`: Write line by line.
- `-k`, `--key`: Key to start the macro (default: F12).
- `-t`, `--time`: A tuple containing the wait times in seconds. Example: `"(2,1)"`.

### Example

To simulate typing a file named `example_code.py` in character-by-character mode with default timings, use:

   `python coding_vid_faker.py example_code.py`

To write word by word and start the macro with the `F12` key, use:

   `python coding_vid_faker.py example_code.py -w -k F11`

To specify custom timing between keystrokes, use:

   `python coding_vid_faker.py example_code.py -t (1.0,0.1)`

## Dependencies

- `keyboard`

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contributing

Feel free to submit issues and pull requests. Contributions are welcome!
