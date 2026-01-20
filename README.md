# WDM Transmitter Layout Documentation

## 1.1 Forbidden Area and Chip Template

The first step involved creating a file that defines the **forbidden area** as well as the **chip boundary frame**.  
The frame is generated using the `make_frame_function()` located in `frame.py`.

![Figure 1 – Complete WDM transmitter layout](./images/figure1_wdm_layout.png)

---

## 1.2 DBR Laser

Next, a **DBR (Distributed Bragg Reflector) laser** was implemented.  
The DBR laser consists of:

- Two Bragg gratings  
- A phase shifter  
- A power amplifier  
- Input and output sections  

Two functions were created for this module:

1. `calc_soa()`: calculates the **length of the section** based on the laser number using the formula:  
2. `Laser()`: generates the **DBR laser element**

All functions are implemented in `laser_dbr.py`.

![Figure 2 – DBR Laser. Left: output to system, Right: input from AWG](./images/figure2_dbr_laser.png)

---

## 1.3 Mach-Zehnder Modulator

The next component added to the layout is the **Mach-Zehnder Modulator (MZM)**.  

Steps involved:

1. **Power splitters (MMI 1x2)** were implemented via the function `mmi()` in `sprzegacz.py`.  
2. **Modulator creation** was implemented using the `modulator()` function.

This resulted in a fully implemented Mach-Zehnder modulator.

![Figure 3 – Mach-Zehnder Modulator](./images/figure3_mzm.png)

---

## 1.4 AWG Demultiplexer Block

After placing the **demultiplexer (AWG)** in the north and south parts of the layout:

- Electrical contacts were added and connected to various parts of the laser  
- Optical ports were added: input ports and a single output port

![Figure 4 – AWG placed near the forbidden band](./images/figure4_awg.png)


