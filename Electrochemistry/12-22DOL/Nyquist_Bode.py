import json
import numpy as np

import matplotlib.pyplot as plt

# Load data from JSON file
with open(r'E:\code\github_clone\Mycode\Electrochemistry\12-22DOL\changed_data.json', 'r') as file:
    data = json.load(file)

# Extract data
freq = np.array(data["freq/Hz"], dtype=float)
Re_Z = np.array(data["Re(Z)/Ohm"], dtype=float)
Im_Z = np.array(data["-Im(Z)/Ohm"], dtype=float)
Z_magnitude = np.array(data["|Z|/Ohm"], dtype=float)
phase_Z = np.array(data["Phase(Z)/deg"], dtype=float)

# Nyquist plot
plt.figure()
plt.plot(Re_Z, Im_Z, 'o-')
plt.xlabel('Re(Z) [Ohm]')
plt.ylabel('-Im(Z) [Ohm]')
plt.title('Nyquist Plot')
plt.grid(True)
plt.show()

# Bode plot
fig, ax1 = plt.subplots()

ax1.set_xscale('log')
ax1.plot(freq, Z_magnitude, 'b-')
ax1.set_xlabel('Frequency [Hz]')
ax1.set_ylabel('|Z| [Ohm]', color='b')
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(freq, phase_Z, 'r-')
ax2.set_ylabel('Phase(Z) [deg]', color='r')

plt.title('Bode Plot')
plt.show()