audiovis

A simple audio visualizer built with Python, using **matplotlib** for rendering and the **Fast Fourier Transform (FFT)** for frequency analysis.

Generates a bar-style visualization of the frequency spectrum of input `.wav` files.

---

### Install

Clone the repo and set up dependencies:

```bash
git clone https://github.com/RynSingleton/audiovis.git
cd audiovis
pip install -r requirements.txt
```

or install manually:

```bash
pip install numpy matplotlib soundfile
```

---

### Usage

Run the program with:

```bash
python main.py
```

The program will prompt you for an input audio file:

```
Input filename: wav_sample.wav
```

It will then process the file, compute FFT data for each chunk, and display a frequency bar visualization.
A GIF animation (`visuals.gif`) will also be saved to the project directory.

---

### Example output

For a sample 1 kHz tone, the visualizer produces an animated bar chart where a single frequency band dominates.
The frame-by-frame update is handled by `matplotlib.animation.FuncAnimation`.

---

### Project structure

```
audio_processor.py   - loads audio and computes FFT magnitudes
visualizer.py        - handles matplotlib rendering and animation
main.py              - entry point for running the visualizer
requirements.txt     - dependencies
```

---

### Requirements

* Python 3.8+
* numpy
* matplotlib
* soundfile

Tested on Linux and Windows.

---

### Development

```bash
make clean    # remove visuals and cache
make run      # launch the visualizer
make help     # list available targets
```

---

### License

MIT
