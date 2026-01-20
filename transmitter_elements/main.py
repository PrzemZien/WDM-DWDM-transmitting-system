import nazca as nc
import nazca.geometries as shape
import nazca.demofab as demo
from frame import *
from modulator import *
from laser_dbr import *
from AWG_BB import *

lasers_list = []
north_lasers_list = []
south_lasers_list = []
power_div_list = []
north_pads_list = []
south_pads_list = []
# importy elementów

#   kwadrat
make_frame_function(-750,1e4-750,1e4-750)

#   8 laserów DBR
for i in range(8):
    if(i>3):
        laser_dbr = laser(i).put(-400 + (i-2) * 700, 2000 + i * 800)
        north_lasers_list.append((laser_dbr))
        lasers_list.append(laser_dbr)
    else:
        laser_dbr = laser(i).put(2900 - i * 700, 2000 + i * 800)
        south_lasers_list.append((laser_dbr))
        lasers_list.append(laser_dbr)

#   8 modulatorów elektroabsrobcyjnych
for i in range(8):
    if(i<=4):
        power_div = modulator(i).put(3900 - i*200, 1600 + i * 800)
    else:
        power_div = modulator(i).put(2900+i*120,1600+i*800)
    power_div_list.append(power_div)

#   demulitplekser AWG
awg = demux().put(7900,5200)

#   connections between modulators and lasers
for i in range(8):
    demo.shallow.sbend_p2p(lasers_list[i].pin['output'], power_div_list[i].pin['input']).put()

for i in range(8):
    demo.shallow.sbend_p2p(power_div_list[i].pin['output'],awg.pin[f'a{i}']).put()

#connections to pads
demo.shallow.strt(length=890.66).put(awg.pin['b0'])

for i in range(8):
    pin = lasers_list[i].pin['input']

    start_pin = nc.Pin(
        name=f'start_{i}',
        xs=pin.xs,
        width=pin.width
    ).put(0, pin.y, 180)  # 180° → kierunek w prawo

    demo.shallow.strt_p2p(start_pin, pin).put()

for laser_idx, laser in enumerate(lasers_list):
    is_top_edge = laser_idx > 3
    for laser_idx, laser in enumerate(lasers_list):
        is_top_edge = laser_idx > 3
        if is_top_edge:
            # Górna grupa (laser_idx 4..7)
            target_y = (1e4 - 750) - 200  # górna krawędź
            pad_angle = 90
            local_idx = laser_idx - 4  # od 0 do 3
            pin_order = ['c0', 'c2', 'c1', 'c3']  # kolejność pinów

            for pin_idx, pinname in enumerate(pin_order):
                target_x = 910 + (local_idx * 4 + pin_idx) * 200
                pad = demo.pad_dc().put(target_x, target_y, pad_angle)
                demo.metaldc.sbend_p2p(
                    laser.pin[pinname],
                    pad.pin['c0'],
                    Lstart=pin_idx * 50 + 100
                ).put()

        else:
            # Dolna grupa (laser_idx 0..3)
            target_y = 900  # dolna krawędź
            pad_angle = 270
            local_idx = 3 - laser_idx  # odliczamy od 3 do 0
            pin_order = ['c0', 'c2', 'c1', 'c3']  # kolejność pinów

            for pin_idx, pinname in enumerate(pin_order):
                target_x = 910 + (local_idx * 4 + pin_idx) * 200
                pad = demo.pad_dc().put(target_x, target_y, pad_angle)
                demo.metaldc.sbend_p2p(
                    laser.pin[pinname].move(0, 0, 180),  # odwrócenie pinów dolnej grupy
                    pad.pin['c0'],
                    Lstart=pin_idx * 50 + 100
                ).put()

#pady do modulatorów
# --- GÓRNA GRUPA -------------------------------------------------
top_mods = power_div_list[4:8]  # 4 górne modulatory
target_y = (1e4 - 750) - 200
pad_angle = 90

# ---- c1 (pierwsze 4 pady) ----
for i, power_div in enumerate(top_mods):
    pad = demo.pad_dc().put(5000 + i * 200, target_y, pad_angle)
    demo.metaldc.sbend_p2p(
        power_div.pin['c1'],
        pad.pin['c0'],
        Lstart=100
    ).put()

# ---- c2 (kolejne 4 pady) ----
for i, power_div in enumerate(top_mods):
    pad = demo.pad_dc().put(5000 + (i + 4) * 200, target_y, pad_angle)
    demo.metaldc.sbend_p2p(
        power_div.pin['c2'].move(0, 0, 180),
        pad.pin['c0'],
        Lstart=100
    ).put()


# --- DOLNA GRUPA -------------------------------------------------
bot_mods = power_div_list[:4]  # 4 dolne modulatory
target_y = 900
pad_angle = 270

# ---- c1 (pierwsze 4 pady) ----
for i, power_div in enumerate(reversed(bot_mods)):
    pad = demo.pad_dc().put(5000 + i * 200, target_y, pad_angle)
    demo.metaldc.sbend_p2p(
        power_div.pin['c1'].move(0, 0, 180),
        pad.pin['c0'],
        Lstart=100
    ).put()

# ---- c2 (kolejne 4 pady) ----
for i, power_div in enumerate(reversed(bot_mods)):
    pad = demo.pad_dc().put(5000 + (i + 4) * 200, target_y, pad_angle)
    demo.metaldc.sbend_p2p(
        power_div.pin['c2'],
        pad.pin['c0'],
        Lstart=100
    ).put()


#wykonanie pliku gds
nc.export_gds(filename="uklad_nadawczy")