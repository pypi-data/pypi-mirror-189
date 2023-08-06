
# PyAMS
PyAMS: Python for Analog and Mixed Signals

<h1 align="center">
    <a href="https://www.pyams.org"><img src="https://pyams.org/logo.png" width="175px" alt="PyAMS"></a>
</h1>

---

<p align="center">
 
 <a href="#News">
    <img src="https://img.shields.io/badge/Version-0.0.1-blue" alt="V 0.0.1">
 </a>
  <a href="#Installation">
      <img src="https://img.shields.io/badge/Python->=3-blue" alt="Python 3+">
  </a>
    
  <a href="https://github.com/d-fathi/PyAMS/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/License-Free-blue" alt="Free">
  </a>
</p>


**************
What is PyAMS?
**************

PyAMS is  used to simplify modeling analog elements and simulate electronic circuit using Python
The objectives of PyAMS is:

*	Creating new PyAMS models of electrical elements by using Python language;
*	Simulating the circuit in the selected mode of operation;
*	Presenting simulation results in a dedicated waveform editor;
*   Simulating the circuit by AppPyAMS commands;
*   PyAMS used Python3+ and works on  Linux, Windows, and OSX.
*   **Licensed under:** PyAMS is free to use. No license is necessary .


## News

What is changed in versions

V  0.0.1
--------
Date 03-02-2023: PyAMS 0.0.1

* Update pin shape (type dot/clk)
* New shape: polygon
* Element's identifier by id.
* Simulator Options:
    * Convergence:
         * ABSTOL: the absolute current or flow tolerance.
         * VNTOL: the absolute voltage or potontial tolerance.
         * RELTOL: the relative voltage(potontial) and current(flow) tolerances.
         * ITL1: the maximum number of iterations the Newton-Raphon method.
    * Interactive:
         * Interval: interval of simulation in miliseconds.
* New analog elements:
    * Diode (Semiconductor library).
    * Diode Zener (Semiconductor library).
    * Diode bridge (Semiconductor library).
    * Voltmeter (Multimeter library).
    * Ammeter (Multimeter library).
	

## Note of installation

*   install PyAMS using pip: **pip install PyAMS-lib**.
