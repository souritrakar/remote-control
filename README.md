# Xbox 'Remote' Controller

A simple utility side project created to play games on an Xbox from a remote location using just your browser / A PS4 Controller

How it works:

A socket.io web server would be running on a local PC, hosted through *ngrok*. The other user (for multiplayer games) can visit the web-app and use keyboard controls to play. The key presses would be broadcasted to the server, which in turn are translated into Virtual Joystick movements, thus controlling the Xbox.

Tech used:

Python, JavaScript (Gamepad API), socket.io, Xbox MyVirtual Joystick 

Note: The latency is much higher than what is feasible for games.
