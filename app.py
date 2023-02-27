from flask import Flask, render_template
import video_dir
import car_dir
import motor

#import config

busnum = 1          # Edit busnum to 0, if you uses Raspberry Pi 1 or 0

video_dir.setup(busnum=busnum)
motor.setup(busnum=busnum)     # Initialize the Raspberry Pi GPIO connected to the DC motor. 
video_dir.home_x_y()
 
app = Flask(__name__)
#app.config.from_object(config)
 

@app.route('/forward')
def forward():
    video_dir.move_increase_y()
    return render_template('index.html')

 
@app.route('/')
def index():
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run()
