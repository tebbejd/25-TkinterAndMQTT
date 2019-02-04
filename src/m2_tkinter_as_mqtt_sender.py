"""
Using a fake robot as the receiver of messages.
"""

# DONE: 1. In mqtt_remote_method_calls, set LEGO_NUMBER at line 131
# to YOUR robot's number.

# TODO: 2. Copy your Tkinter/ttk ROBOT gui code from the previous session (m6).
# Then modify it so that pressing a button sends a message to a teammate
# of the form:
#   (for Forward)
#        ["forward", X, y]
#   where X and Y are from the entry box.
#
# Implement and test.

"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Jacob Tebbe.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time

def main():
    """ Constructs a GUI that will be used MUCH later to control EV3. """
    # -------------------------------------------------------------------------
    # DONE: 2. Follow along with the video to make a remote control GUI
    # For every grid() method call you will add a row and a column argument
    # -------------------------------------------------------------------------
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    mqtt_client = com.MqttClient()
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()


    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()  # only grid call that does NOT need a row and column

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=4)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=4)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=4)
    forward_button['command'] = lambda: mqtt_client.send_message('move',[50,50])
    root.bind('<Up>', lambda event: mqtt_client.send_message('move',[50,50]))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=1)
    left_button['command'] = lambda: mqtt_client.send_message('move',[50,100])
    root.bind('<Left>', lambda event: mqtt_client.send_message('move',[50,100]))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=6, column=0)
    stop_button['command'] = lambda: mqtt_client.send_message('end',['stop'])
    root.bind('<space>', lambda event: mqtt_client.send_message('end',['stop']))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=3)
    right_button['command'] = lambda: mqtt_client.send_message('move',[100,50])
    root.bind('<Right>', lambda event: mqtt_client.send_message('move',[100,50]))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=5, column=4)
    back_button['command'] = lambda: mqtt_client.send_message('move',[-50,-50])
    root.bind('<Down>', lambda event: mqtt_client.send_message('move',[-50,-50]))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=2, column=2)
    up_button['command'] = lambda: mqtt_client.send_message('say_it',['up'])
    root.bind('<u>', lambda event: mqtt_client.send_message('say_it',['up']))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=4, column=2)
    down_button['command'] = lambda: mqtt_client.send_message('say_it',['down'])
    root.bind('<j>', lambda event: mqtt_client.send_message('say_it',['down']))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=7, column=2)
    q_button['command'] = lambda: print("Quit button")
    root.bind('<q>', lambda event: print('Quit Key'))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=8, column=4)
    e_button['command'] = lambda: exit()
    root.bind('<Escape>', lambda event: exit())

    root.mainloop()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
