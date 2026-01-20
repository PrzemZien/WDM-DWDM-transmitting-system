import nazca as nd
import nazca.geometries as shape
import nazca.demofab as demo

def demux():
    GDS_width=1209.339
    GDS_height=1619.376
    GDS_input_height=(249.888+246.888)/2
    GDS_output_offset=(39.921+36.921)/2
    GDS_output_space=30

    with nd.Cell(name='demux') as dmx:
        # load GDS BB
        awg = nd.load_gds(
            filename='AWG_topo.gds'
        )
        awg.put(1210, 0, -180, flip = True) 
        for i in range(8):
            nd.Pin('a{}'.format(i), width=2).put(0, (GDS_output_offset+i*GDS_output_space)-(GDS_height/2), 180)

        nd.Pin('b0', width=2).put(GDS_width,  GDS_input_height-(GDS_height/2),0)       

        nd.put_stub()
        nd.put_boundingbox('org', length=GDS_width, width=GDS_height)
    return dmx

demux().put()

nd.export_gds(filename='AWG_BB')

