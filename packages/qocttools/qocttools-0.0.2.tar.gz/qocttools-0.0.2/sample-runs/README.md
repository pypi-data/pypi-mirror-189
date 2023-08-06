
Significant preliminary runs, fully documented so that they can be
easily replicated.

Subdirectories:

## model

model.ipynb: Construction of the model described in [Jenkins et al., PRB
95, 064423 (2017)].  In particular, Fig. 3 (b) is replicated. This is
a plot of the eigenvalues of the Hamiltonian model vs. the magnitude
of an external magnetic field.


## pipulse

pipulse.ipynb: pi-pulse study for the GdW30 system: creation of transitions
using the pi-pulse concept, demostrating how this is an approximation,
and how it is better at lower amplitudes and longer times.


## propagators

propagators.ipynb: Time benchmarks for the propagation methods.


## gradient

gradient.ipynb: Check on the accuracy on the computation of the gradient of a
control target functional, using the QOCT formula.


## gradient-dissipation

gradient.ipynb: Check on the accuracy on the computation of the gradient of a
control target functional, using the QOCT formula. Added dissipation terms.


## qoctbasic

7.ipynb: Example of optimization with QOCT, for a state-to-state transition,
and for a gate optimization.


## qocttoffoli

Calculation with qutip of the design of a Toffoli gate on the GdW30 system.


## dissipation

Calculation of a Rabi pulses on the GdW30 system, to be compared with the
experimental results provided by F. Luis. It contains calculations
performed with and without dissipation terms.


