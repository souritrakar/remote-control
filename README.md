# Xbox 'Remote' Controller

Simple utility script I wrote in collaboration with @aritrakar to relay commands from a PlayStation controller / Browser (key presses) to a web-server hosted on another  end, to control a Xbox remotely to play games.

Future: I plan to create a better, optimized version which would include a proper web-app controller (streaming the visuals) and latency reduction

How it works:

Tech used:

Python, JavaScript (Gamepad API), socket.io, Xbox MyVirtual Joystick 

Note: The latency between the request and the response was too high to play games in (near) real-time, which was the intended purpose.
