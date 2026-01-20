import nazca.geometries as shape
import nazca as nc

#Frame
def make_frame_function(u_sizew, u_sizel, u_sizeh):
    boundaries = nc.Polygon(layer=11, points=shape.frame(sizew=u_sizew, sizel=u_sizel, sizeh=u_sizeh))
    boundaries.put()


