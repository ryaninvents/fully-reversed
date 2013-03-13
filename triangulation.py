import numpy

def triangulation():
    #inputs 
    uc = input('Enter the camera pixel size(m) : ')
    fc = input('Enter the camera lens focal length(m) : ')
    ratio = input('Enter the projector throw ratio(%): ')
    rp = input('Enter the x-resolution of the projector(pixels): ')
    throw = input('Enter the minimum throw distance of projector(m) ')
    x = input('Enter the desired spatial resolution(m) ')
    tri = input('Enter the triangulation angle(degrees) ')
    #conveting from percent to decimal
    ratio = ratio/100.0
    #converting to radians
    thetao = (tri*numpy.pi)/180
    zc = fc*(x/uc)
    zp = x*ratio*rp
    #Checking if the distance from object to projector is less than the minimum
    #throw distance
    if zp < throw:
        #Output min spatial resolution
        print
        print('Desired spatial resolution is not atainable with selected projector')
        maxres = throw/(ratio*rp)
        print('The smallest attainable spatial resolution is ' + str(maxres) + ' meters/pixel')

    else:
        #Calculating the distance between camera and projector
        D = (zc**2 + zp**2 - zc*zc*numpy.cos(thetao))**0.5
        #Output distances
        print
        print('Distance from projector to target: ' +str(zp) + ' meters')
        print('Distance from camera to target: ' +str(zc) + ' meters')
        print('Distance between camera and projector: ' +str(D) + ' meters')
        
        
        
    
    
