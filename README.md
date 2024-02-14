# Install

### Executable
1. Download the appropriate **game-of-life.zip** file based on your operating system
2. Extract the zip
3. Run the executable file

### Source Code
1. Install the dependencies: [Python3](https://www.python.org/downloads/) [Python Raylib](https://pypi.org/project/raylib/) [PyInstaller](https://pyinstaller.org/en/stable/)
2. Run `git clone https://github.com/ansel64/game-of-life.git` on your CLI
3. In the source code directory, run `pyinstaller game-of-life.py --onefile --windowed`
5. Your executable file is now in the `dist/` directory

# Notes

- Running the executable file might take a while to load
- As of now, the simulation is set to default parameters and cannot be changed
- To close or reset the simulation, quit the app or press ESC
- For macos users, you might need to go to `System Settings -> Privacy & Security`, scroll down and click "Open Anyway" to run the executable file
- If you're downloading the source, your Python LSP might throw errors regarding Raylib's color constants. This is a false positive and can be safely ignored
- Ask any question/help or report bugs in [Github Issues page](https://github.com/ansel64/game-of-life/issues)
