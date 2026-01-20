import nazca as nc
import nazca.demofab as demo

def mmi(offset=40,):
    with nc.Cell(name='MMI_1x2') as mmi_1x2:
        mmi1 = demo.mmi1x2_sh().put()
        elm1 = demo.shallow.strt(length=50).put(mmi1.pin['a0'])
        elm2 = demo.shallow.sbend(offset=offset).put(mmi1.pin['b0'])
        elm3 = demo.shallow.sbend(offset=-offset).put(mmi1.pin['b1'])

        nc.Pin('a0', pin=elm1.pin['b0']).put()
        nc.Pin('b0', pin=elm2.pin['b0']).put()
        nc.Pin('b1',pin=elm3.pin['b0']).put()

    return mmi_1x2