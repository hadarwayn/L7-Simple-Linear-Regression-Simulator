This project is a Python script that demonstrates a fundamental machine learning concept: finding the "line of best fit" for a set of data. It works by:

1.  Generating a cloud of random data points around a hidden straight line.
2.  Making hundreds of random guesses for the line's equation (`Y = aX + b`).
3.  Calculating the error for each guess to see how "wrong" it is.
4.  Identifying the best guess (the one with the lowest error) and displaying it.

This approach simulates how a machine "learns" by iteratively trying solutions and selecting the one that performs best.



## 🚀 How to Run

Follow these steps to run the simulator on your own machine.

### Prerequisites

You'll need Python 3 and the following packages installed:

-   NumPy
-   Matplotlib

If you are on a Debian/Ubuntu-based system (like WSL), you can install them with:
```bash
sudo apt update
sudo apt install python3-numpy python3-matplotlib
