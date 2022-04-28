import cv2
import dropbox
import time
import random
start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret ,frame=videoCaptureObject.read()
        imagename="img"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        start_time=time.time
        result=False
    return imagename
    print("snapshottaken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()  

def uploadfile():
    access_token = 'sl.BGTVzCqKJvK4c-H20VChLjMjovkx7bdN74FRDfl6Tn0VRbqeSivC4rQjZbHNgYu06veB1l9WPXpmoJAqDT3J1KOSCqbAp37bm8i1vtdEgGd0xOUkDOPcdCDZHgfgsdxnb7Xylk7nbGwt'
    
    
    file_from=file
    file_to="/folder/"+(imagename) 
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("filesUploads") 

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)
main()            


