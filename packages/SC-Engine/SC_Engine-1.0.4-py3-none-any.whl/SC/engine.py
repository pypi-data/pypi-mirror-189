import math

def rotate(pixel_coor:[int,int],degrees:int,rotate_coor:[int,int])->[int,int]:
  """
  pixel_coor  ->  The pixel coordinates
  degrees     ->  The amount of degrees to rotate the pixel to the right around the rotate coordinates
  rotate_coor ->  The coordinates of the point to rotate the pixel around
  """
  
  px , py = pixel_coor
  rx , ry = rotate_coor
  dx , dy = abs(px-rx), abs(py-ry)
  
  a = degrees-math.atan2(dy,dx)*180/pi
  r = math.sqrt(dx**2+dy**2)

  px , py = rx , ry

  for todo in range(round(r)):
    px , py = px+math.sin(math.radians(a)) , py+math.cos(math.radians(a))

  return [round(px) , round(py)]