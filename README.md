![Sense HAT](https://user-images.githubusercontent.com/16626308/41469297-f47957ec-70ac-11e8-8c75-29812fb4ada0.png)

SenseOUT
========
Sense HAT’s LED display as Linux FIFO file.

## Description
The project has a Python 3 program that reads data from a Linux FIFO file and prints them to Sense HAT’s LED display.
Reading from normal file or other device file is also supported.

The project is made just for fun and is shouldn't have any useful value. If you find it, please let me know.

## Usage
The project works only on Raspberry Pi with attached Sense HAT and installed Python. It was tested on Raspberry Pi 3, but it should also works on other versions of Raspberry Pi.

First, you should clone the project:
```bash
git clone  https://github.com/filips123/SenseOUT.git # Clone the project
cd SenseOUT # Go to project directory
```

Then you should create a new Linux FIFO file:
```bash
mkfifo sensehat # Create a new FIFO file
```

The default input file is `sensehat`. To change it, pass file name as first program argument:
```bash
python3 handler.py /path/to/file # Use custom file
```

You could run the program in the background:
```bash
python3 handler.py & # Run the program in the background
```

Then you could write data to the file and they will be displayed on Sense HAT’s LED display:
```bash
echo "ABC" > sensehat # Display output only on Sense HAT’s LED display
# OR #
echo "ABC" | tee sensehat # Display output on Sense HAT’s LED and in terminal
```

You could also display commands outputs, but you shouldn't use the commands with a lot of output:
```bash
ls | tee sensehat # Display content of directory on Sense HAT’s LED and in terminal
```

## License
This project is licensed under the GNU General Public License v3. See the [LICENSE](https://github.com/filips123/SenseOUT/blob/master/LICENSE) file for details.
