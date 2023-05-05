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


ground=Entity(model='plane',scale=(10000,1,10000),collider='mesh',texture='grass',texture_scale=(5000,5000),color=color.rgb(10,60,10))


sky=Sky(color=color.rgb(80,30,160),texter='myimage.png',texture_scale=(3))
wall1=Entity(model='cube',y=17,scale=(.2,20,40),texture='kiku.mp4',collider='mesh',x=0,color=color.rgb(100,100,100),z=-15,rotation_y=45)
wall2=Entity(model='cube',y=30,z=-15,scale=(.2,40,25),texture='kiku.mp4',rotation_y=45,collider='mesh',x=1520,color=color.rgb(200,200,200))

######################################################################
ground2=Entity(model='plane',y=.3,scale=(10000,1,10),collider='mesh',texture='grass',texture_scale=1,color=color.rgb(30,30,40))
line=-2000
lll=Entity(model='cube',y=1,scale=(2,.5,1),x=line)
while line<5000:
    lll=Entity(model='cube',y=.32,scale=(8,.1,.5),x=line,z=1.7)
    line=line+20
line=-2000
while line<5000:
    lll=Entity(model='cube',y=.32,scale=(8,.1,.5),x=line,z=-1.7)
    line=line+20


line=-2000
###########################################################################
sun=Entity(model='sphere',scale=(450),color=color.rgb(200,200,60),texture='grass',rotation_x=0,texture_scale=(2,2))





###########################################################################


myimgs=['bb.jpg','bb1.jpg','bb2.jpg']
while line<5000:
    texttt=rdm.choice(myimgs)
    ccc=rdm.randint(1,4)
    ccc1=rdm.choice(['-1','1'])
    ccc1=int(ccc1)
    sonic=Entity(model='hh.obj',scale=(6,5+4,8+3*ccc),y=-1.5,z=+30+30*ccc,x=line,texture=texttt,texture_scale=(5,5),rotation_y=90,
                 color=color.rgb(40*ccc,40*ccc,80*ccc))
    line=line+60

line=-1000
myimgs=['bb.jpg','bb1.jpg','bb2.jpg']
while line<5000:
    texttt=rdm.choice(myimgs)
    ccc=rdm.randint(1,4)
    ccc1=rdm.choice(['-1','1'])
    ccc1=int(ccc1)
    sonic=Entity(model='hh.obj',scale=(6,5+4,8+3*ccc),y=-1.5,z=-30-30*ccc,x=line,texture=texttt,texture_scale=(5,5),rotation_y=90,
                 color=color.rgb(40*ccc,80*ccc,80*ccc))
    line=line+60


##########################################################################################################################
ww1=Entity(model='cube',y=7,scale=(1,1,40),texture='grass',collider='mesh',
             x=0,color=color.rgb(50,10,40),z=-15,rotation_y=45)
ww1=Entity(model='cube',y=27,scale=(1,1,40),texture='grass',collider='mesh',
             x=0,color=color.rgb(50,10,40),z=-15,rotation_y=45)
ww1=Entity(model='cube',y=3.5,scale=(1,7,10),texture='grass',collider='mesh',
             x=0,color=color.rgb(50,10,40),z=-15,rotation_y=45)


ww1=Entity(model='cube',y=10,scale=(1,1,30),texture='grass',collider='mesh',
             x=1520,color=color.rgb(50,10,40),z=-15,rotation_y=45)
ww1=Entity(model='cube',y=50,scale=(1,1,30),texture='grass',collider='mesh',
             x=1520,color=color.rgb(50,10,40),z=-15,rotation_y=45)
ww1=Entity(model='cube',y=5,scale=(1,10,5),texture='grass',collider='mesh',
             x=1520,color=color.rgb(50,10,40),z=-15,rotation_y=45)
##########################################################################################################################

car=Entity(
    model='car',texture='shore',scale=(2.5,2.5,2.5),color=color.rgb(60,30,120),rotation_y=-90,y=1.22,z=-10,x=0
)

i=0
car1=Entity(
    model='car',texture='shore',scale=(1.1,1.1,1.1),color=color.rgb(255,200,120),rotation_y=0,y=.8,z=0,x=-1000 # yellow car
)


camera.rotation_y=90
camera.y=2

ILI=Audio('kiku.mp4', pitch=1, loop=True, autoplay=True,volume=0)
knok=Audio('kiku.mp4',pitch=1, loop=True, autoplay=True,volume=0)
kok=Audio('ss.mp3',pitch=.75, loop=True, autoplay=True,volume=.12)
camera.x=-1000
camera.z=0





def update():
    sun.rotation_z=sun.rotation_z-18
    
    sun.rotation_x=sun.rotation_x+.35
    
    sunangle=3.14*sun.rotation_x/180
    sun.x=7000*math.cos(sunangle)
    if sun.rotation_x >=360 :
        sun.rotation_x=0
    if sun.rotation_x<=60 or sun.rotation_x>= 300:
        sun.y=1500*abs(math.sin(3*sunangle))+200
    else :
        sun.y=100*abs(math.sin(3*sunangle))+100
    sky.color=color.rgb(50+70*sun.y/2000,70*sun.y/2000,50+70*sun.y/1500)
    sun.color=color.rgb(130+80*sun.y/1500,100*sun.y/2000,25+100*sun.y/2000)
    if sun.y < 210 and sun.y > 185:pass

    car1.x=car1.x+1
    if abs(camera.x)>-500 and  abs(camera.x)<500:
        ILI.volume=abs(20/(camera.x+20))
    else :
        ILI.volume=0
    if abs(camera.x)>1000 and  abs(camera.x)<2000:
        knok.volume=abs(10/(camera.x-1500))
    else :
        knok.volume=0
          
    if held_keys['e'] and car.parent!=camera.ui:
        car.parent=camera.ui
        car.scale=(.5)
        car.y=-.32
        car.x=0

##############
    if camera.z>=car1.z-1 and camera.z<=car1.z+1 and camera.x>=car1.x-10 and camera.x<=car1.x+250:
        car.rotation_y=car.rotation_y+10
        car.rotation_z=car.rotation_z+10
        camera.y=2*abs(math.sin(.009*car.rotation_y))+2
    else:
        camera.rotation_z=0
        car.rotation_y=-90
        car.rotation_z=0
        camera.y=1

##########

    print ('car1 z=',sun.rotation_x,'   camera=',sun.y)
    
    if held_keys['w']:

        
        if car.parent!=camera.ui:
            camera.x=camera.x+.7*math.sin(3.14*camera.rotation_y/180)
            camera.z=camera.z+.7*math.cos(3.14*camera.rotation_y/180)
            #camera.y=camera.y-10*math.sin(3.14*camera.rotation_x/180)
            camera.y=.3*abs(math.sin(.35*(camera.x+camera.z)))+1
        else:
            camera.x=camera.x+7*math.sin(3.14*camera.rotation_y/180)
            camera.z=camera.z+7*math.cos(3.14*camera.rotation_y/180)



        
        
        
    if held_keys['s']:
        if car.parent!=camera.ui:
            camera.x=camera.x-1*math.sin(3.14*camera.rotation_y/180)
            camera.z=camera.z-1*math.cos(3.14*camera.rotation_y/180)
            camera.y=.5*abs(math.sin(.3*(camera.x+camera.z)))+1
        else:
            camera.x=camera.x-3*math.sin(3.14*camera.rotation_y/180)
            camera.z=camera.z-3*math.cos(3.14*camera.rotation_y/180)
    if held_keys['8']:
        camera.rotation_x=camera.rotation_x+1
    if held_keys['2']:
        camera.rotation_x=camera.rotation_x-1
    if held_keys['d'] :
        camera.rotation_y=camera.rotation_y+2.5

        car.rotation_y=-75
        car.rotation_z=-5
    elif held_keys['a'] :
        camera.rotation_y=camera.rotation_y-2.5

        car.rotation_y=-105
        car.rotation_z=-5
   
    if held_keys['i']:
        camera.y=camera.y+1
    if held_keys['k']:
        camera.y=camera.y-1
###############################################
    if sun.y>=0 and sun.y<=300:
        camera.y=1.5*abs(math.sin(.05*sun.rotation_z))+1
    if sun.y>=0 and sun.y<=250:
        camera.rotation_z=camera.rotation_z+2
    if sun.y>=250 and sun.y<=300:
        camera.rotation_z=camera.rotation_z-2
    if sun.y>=300 and sun.y<=350:
        camera.rotation_z=camera.rotation_z+1
    if sun.y>=400 and sun.y<=450:
        camera.rotation_z=camera.rotation_z-1





    
app.run()
