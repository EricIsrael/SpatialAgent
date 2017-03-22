# SpatialAgent

The project was done for a class of mine. 


I used the strategy called Klinokinesis that implants that keeps the velocity constant but moves the orientation. 
The formula implanted in my code is: 
        o = o + t * 1/(1+d)
        o = the orientation of the agent, in radians.
        t = some maximum turning rate
        d =distance from the agent to the food source


I set the velocity to 10 because it is an easy number to use. Then I put if the sensory is less than the memory perform a random walk. If it is not less than the memory use the
Klinokinesis formula above. I set the turning rate equal to 1.5. No real reason why but I thought it was a good number to start with and it's less than pi. 
