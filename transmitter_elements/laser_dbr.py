import nazca as nc
import nazca.demofab as demo


def calc_soa(n):
    result = 550 + 20*n
    return result


def laser(laser_number):
    with (nc.Cell(name=f'laser_{laser_number}') as laser):
        # sekcja wejsciowa
        iso = demo.isolation_act(length=20)
        input = demo.s2a().put()
        iso.put()
        dbr_1 = demo.dbr(length=450).put()
        phase = demo.phase_shifter(length=50).put()
        iso.put()
        soa = demo.soa(length=calc_soa(laser_number)).put()
        iso.put()
        dbr_2 = demo.dbr(length=70).put()
        out = demo.a2s().put()

        #pads for input and output of laser
        nc.Pin('output',pin=out.pin['b0']).put()
        nc.Pin('input',pin=input.pin['a0']).put()

        #pads for laser building blocks
        nc.Pin('c0',pin=dbr_1.pin['c0']).put(angle=180)
        nc.Pin('c1',pin=soa.pin['c0']).put(angle=180)
        nc.Pin('c2',pin=phase.pin['c0']).put(angle=180)
        nc.Pin('c3',pin=dbr_2.pin['c0']).put(angle=180)


    return laser