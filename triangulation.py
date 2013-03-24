import numpy

def triangulation():
    #inputs 
    uc = input('Enter the camera pixel size(m) : ')
    fc = input('Enter the camera lens focal length(m) : ')
    ratio = input('Enter the projector throw ratio(%): ')
    rp = input('Enter the x-resolution of the projector(pixels): ')
    throw = input('Enter the minimum throw distance of projector(m) ')
    tri = input('Enter the triangulation angle(degrees) ')
    #conveting from percent to decimal
    ratio = ratio/100.0
    #converting to radians
    thetao = (tri*numpy.pi)/180
    maxres = throw/(ratio*rp)
    zc = fc*(maxres/uc)
    zp = maxres*ratio*rp  
    #Calculating the distance between camera and projector
    D = .254/numpy.tan((numpy.pi/2.0)-thetao)
    zcreal = .254/numpy.sin((numpy.pi/2.0)-thetao)
    if zcreal > zc:
        print(error)
    else:
        #Output distances
        print
        print('Distance from projector to target: ' +str(zp) + ' meters')
        print('Distance between camera and projector: ' +str(D) + ' meters')
    
    
    
