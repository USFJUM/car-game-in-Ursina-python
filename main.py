#>>>>>>>>>>>>   How to play <<<<<<<<<<<

#>>>>>>>>   'press >w< and >s<  to move 
#>>>>>>>>   press >a< and >d< to turn right left  
#>>>>>>>>   press >e< to get car'#



from ursina import Entity,Ursina,color,Sky,window,camera,Audio,Text,held_keys,math
import random as rdm
import win32com.client.dynamic as max



kim=max.Dispatch('SAPI.SpVoice')

kim.Voice = kim.GetVoices().Item(1)
#kim.Speak(text)

print('>>>>>ooo>>>>>',kim.Voice)

app=Ursina()


window.fullscreen=0


ground=Entity(model='plane',scale=(10000,1,10000),collider='mesh',texture='grass',texture_scale=(500,500),color=color.rgb(10,60,10))


roud=Entity(model='A80.obj',scale=(8,1,8),z=-500,y=-5,color=color.rgb(122,40,200),x=-500)
roud1=Entity(model='A80.obj',scale=(8,1,8),z=-970,y=-5,color=color.rgb(122,40,200),x=-930)
roud=Entity(model='A80.obj',scale=(8,1,8),z=-1530,y=-5,color=color.rgb(122,40,200),x=-1500)
roud1=Entity(model='A80.obj',scale=(8,1,8),z=-2000,y=-5,color=color.rgb(122,40,200),x=-2000)
asj=Sky(color=color.rgb(40,0,80))
wall1=Entity(model='cube',y=17,scale=(.2,20,40),texture='oh.mp4',collider='mesh',x=0,color=color.rgb(100,100,100),z=-15,rotation_y=45)
wall2=Entity(model='cube',y=10,z=0,scale=(.2,10,35),texture='kiku.mp4',collider='mesh',x=1500,color=color.rgb(100,100,100))
#www0=Entity(model='cube',z=-30.2,scale=(30000,10,.2),texture='grass',color=color.rgb(255,128,20),collider='mesh')
#www1=Entity(model='cube',z=.2,scale=(30000,10,.2),texture='grass',color=color.rgb(255,128,20),collider='mesh')
######################################################################
ground2=Entity(model='plane',y=.3,scale=(10000,1,20),collider='mesh',texture='grass',texture_scale=1,color=color.rgb(30,30,40))
line=-2000
lll=Entity(model='cube',y=1,scale=(2,.5,1),x=line)
while line<10000:
    lll=Entity(model='cube',y=.32,scale=(8,.1,.5),x=line,z=3.45)
    line=line+20
line=-2000
while line<10000:
    lll=Entity(model='cube',y=.32,scale=(8,.1,.5),x=line,z=-3.45)
    line=line+20

lll=Entity(model='cube',y=.32,scale=(100000,.5,1),z=-10,color=color.rgb(128,128,20))
lll=Entity(model='cube',y=.32,scale=(100000,.5,1),z=10,color=color.rgb(150,140,20))
line=-2000
###########################################################################


'''ground2=Entity(model='plane',y=.3,scale=(10000,1,20),z=-30,collider='mesh',texture='grass',texture_scale=1,color=color.rgb(30,30,40))
line=-2000
lll=Entity(model='cube',y=1,scale=(2,.5,1),x=line)
while line<10000:
    lll=Entity(model='cube',y=.32,scale=(8,.1,.5),x=line,z=3.45-30)
    line=line+20
line=-2000
while line<10000:
    lll=Entity(model='cube',y=.32,scale=(8,.1,.5),x=line,z=-3.45-30)
    line=line+20

lll=Entity(model='cube',y=.32,scale=(100000,.5,1),z=-10-30,color=color.rgb(128,128,20))
lll=Entity(model='cube',y=.32,scale=(100000,.5,1),z=10-30,color=color.rgb(150,140,20))
line=-2000'''
##########################################  sonic  #######################################################################
while line<10000:
    ccc=rdm.randint(1,4)
    sonic=Entity(model='hh.obj',scale=(1,ccc,2*ccc),y=-.5,z=20,x=line,rotation_y=90,color=color.rgb(40*ccc,10*ccc,80*ccc))
    line=line+20


##########################################################################################################################
ww1=Entity(model='cube',y=7,scale=(1,1,40),texture='grass',collider='mesh',
             x=0,color=color.rgb(50,10,40),z=-15,rotation_y=45)
ww1=Entity(model='cube',y=27,scale=(1,1,40),texture='grass',collider='mesh',
             x=0,color=color.rgb(50,10,40),z=-15,rotation_y=45)
ww1=Entity(model='cube',y=3.5,scale=(1,7,10),texture='grass',collider='mesh',
             x=0,color=color.rgb(50,10,40),z=-15,rotation_y=45)
##########################################################################################################################

car=Entity(
    model='car',texture='shore',scale=(2.5,2.5,2.5),color=color.rgb(40,20,120),rotation_y=-90,y=1.22,z=-10,x=0
)

i=0




ILI=Audio('oh.mp4', pitch=1, loop=True, autoplay=True,volume=0)
knok=Audio('kiku.mp4',pitch=1, loop=True, autoplay=True,volume=0)
kok=Audio('ss.mp3',pitch=1, loop=True, autoplay=True,volume=.15)
camera.x=-1000


def update():
  
    car.rotation_y=-90
    car.rotation_z=0

    if abs(camera.x)>-500 and  abs(camera.x)<500:
        ILI.volume=abs(20/(camera.x+20))
    else :
        ILI.volume=0
    if abs(camera.x)>1000 and  abs(camera.x)<2000:
        knok.volume=abs(10/(camera.x-1500))
    else :
        knok.volume=0
    '''if camera.z>=10:
        car.rotation_y=car.rotation_y+10
        car.rotation_z=car.rotation_z+10
        camera.z=camera.z-.1


    else:
        car.rotation_y=-90
        car.rotation_z=0
    if camera.z>=10 and camera.z<=10.1:
        kim.speak(', , latteshof albanat')
    if camera.rotation_z>0:
        camera.rotation_z=camera.rotation_z-1
    if camera.rotation_z<0:
        camera.rotation_z=camera.rotation_z+1
    if camera.rotation_x>0:
        camera.rotation_x=camera.rotation_x-.2
    if camera.rotation_x<0:
        camera.rotation_x=camera.rotation_x+.2'''       
    if held_keys['e'] and car.parent!=camera.ui:
        car.parent=camera.ui
        car.scale=(.5)
        car.y=-.3
        car.z=20


    
    if held_keys['w']:
        if car.parent!=camera.ui:
            camera.x=camera.x+.7*math.sin(3.14*camera.rotation_y/180)
            camera.z=camera.z+.7*math.cos(3.14*camera.rotation_y/180)
            #camera.y=camera.y-10*math.sin(3.14*camera.rotation_x/180)
            camera.y=.3*abs(math.sin(.35*(camera.x+camera.z)))+1
        else:
            camera.x=camera.x+5*math.sin(3.14*camera.rotation_y/180)
            camera.z=camera.z+5*math.cos(3.14*camera.rotation_y/180)
    if held_keys['s']:
        if car.parent!=camera.ui:
            camera.x=camera.x-1*math.sin(3.14*camera.rotation_y/180)
            camera.z=camera.z-1*math.cos(3.14*camera.rotation_y/180)
            camera.y=.5*abs(math.sin(.3*(camera.x+camera.z)))+1
        else:
            camera.x=camera.x-5*math.sin(3.14*camera.rotation_y/180)
            camera.z=camera.z-5*math.cos(3.14*camera.rotation_y/180)
    if held_keys['8']:
        camera.rotation_x=camera.rotation_x+.3
    if held_keys['2']:
        camera.rotation_x=camera.rotation_x-.3
    if held_keys['d'] :
        camera.rotation_y=camera.rotation_y+2

        car.rotation_y=-75
        car.rotation_z=-5
    elif held_keys['a'] :
        camera.rotation_y=camera.rotation_y-2

        car.rotation_y=-105
        car.rotation_z=-5
    else:
        pass
        car.rotation_y=-90
        car.rotation_z=0
    if held_keys['i']:
        camera.y=camera.y+1
    if held_keys['k']:
        camera.y=camera.y-1
    if held_keys['6']:
        camera.rotation_z=camera.rotation_z+1
    if held_keys['4']:
        camera.rotation_z=camera.rotation_z-1


    
app.run()
