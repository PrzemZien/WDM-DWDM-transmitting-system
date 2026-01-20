import nazca as nc
import sprzegacz
import nazca.demofab as demo

def modulator(power_divider_number):
    with nc.Cell(name=f'power_divider_{power_divider_number}') as power_divider:
        # first splitter 2200,400 , -180
        split_1 = sprzegacz.mmi(offset=100).put(1000, 400, 0)

        # phase modulators

        # calculation of lenght of phase modulator
        phase_mod_length = 800 + 70 * power_divider_number

        # phase modulator
        top_phase_modulator = demo.eopm_dc(length=phase_mod_length, pads=False, sep=10).put(1700, 550)

        # second phase modulator
        bot_phase_modulator = demo.eopm_dc(length=phase_mod_length, pads=False, sep=10).put(1700, 250, flip=True)

        # second splitter
        split_2 = sprzegacz.mmi(offset=100).put(3600, 400, -180)

        # connections
        demo.shallow.sbend_p2p(split_1.pin['b0'], top_phase_modulator.pin['a0']).put()
        demo.shallow.sbend_p2p(split_1.pin['b1'], bot_phase_modulator.pin['a0']).put()
        demo.shallow.sbend_p2p(split_2.pin['b1'], top_phase_modulator.pin['b0']).put()
        demo.shallow.sbend_p2p(split_2.pin['b0'], bot_phase_modulator.pin['b0']).put()

        #Input and Output
        nc.Pin('input',pin=split_1.pin['a0']).put()
        nc.Pin('output',pin=split_2.pin['a0']).put()
        #pady
        nc.Pin('c1',pin=top_phase_modulator.pin['c0']).put()
        nc.Pin('c2',pin=bot_phase_modulator.pin['c1']).put()

    return power_divider