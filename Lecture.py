from tkinter import*


# Importing required modules 
  
import tkinter as tk 
import tkinter.scrolledtext as st 

def quiz():
        import Quiz
# Creating tkinter window 
win = tk.Tk() 
win.title("Lecture") 
win.geometry("500x600")
win.configure(bg="green")
# Title Label 
tk.Label(win,  text = "The Last Planet",  font = ("Times New Roman", 20),  background = 'green',  foreground = "white").grid(column = 0, row = 10) 

nbutton = Button(win, text=">>", command=quiz, width=5,height=1, bg="green", fg="white", font=("times", 16, "bold"))
nbutton.place(x=400, y=5)
  
# Creating scrolled text area 
text_area = st.ScrolledText(win, width = 44,  height = 25,  font = ("Times New Roman", 15)) 
  
text_area.grid(column = 0, pady = 20, padx = 20) 
  
# Inserting Text which is read only 
text_area.insert(tk.INSERT, 
"""
        Our environment is under distress and it is not a hidden fact anymore. The threat it is facing right now is alarming and it is our duty to save it before it gets too late. As inhabitants of this earth, everyone must come together to do their bit to save our environment. After all, it is because of our activities that our ecological balance has been disturbed. We must make sure that instead of over-exploiting the environment’s resources, we must conserve them. It is important to note that even the littlest of actions impact the environment directly or indirectly.

        The occurrences of natural calamities are increasing day by day which is resulting in loss of lives. Further, the melting of the glaciers is another alarming point as to why we need to save the environment.

        In addition to that, the increase of carbon dioxide in the atmosphere is proving to be more harmful than ever. If we do not take immediate action, we will have to face grave consequences at the hands of nature.

        It is rather important to note that by saving the environment, we will be saving mankind. We have to do this for our survival and not the earth’s survival. Mother earth has survived for millions of years and will continue to do so. It is mankind that is at risk, so we must start now.

        We need to start with the proper handling of waste materials. To do so, one must begin with recycling and proper disposal of waste items. The use of coal must be reduced and we must switch to reusable power like hydro or solar power.

                        MORAL AND LESSON 


        This way, we can adopt a healthy and greener lifestyle. On a bigger level, we see that cities must be planned as per the available water resources. This will help in the conservation of water resources. Avoid using hot water, and make do with cold water when possible. Further, the farmers must use organic fertilizers in place of pesticides.

        Further, air pollution must be reduced at all costs. Everyone must avoid taking their personal cars or bikes if possible. Try carpooling or taking public transport for the same. Do not waste electricity so as to prevent global warming.

        Switch off fans and light when not in use, unplug electrical appliances as well. Try to use recycled products so no unnecessary waste is produced. Moreover, avoid the use of plastic and switch to greener alternatives. For instance, use reusable bags and containers. Do not litter the roads and prevent your loved ones from doing so too.

        Most importantly, plant trees as many as you can. As the amount of carbon dioxide present in the air and the rate of deforestation happening is very disruptive. So, as the trees will enhance the air quality, we must encourage the planting of trees. Moreover, it is equally important to discourage deforestation.
        
        Every year, we are losing our forests which carry the potential to make the air cleaner. It must begin with us and our children. Teach them from a young age to be responsible for the environment and work to save it for a better and greener future.


MARINE LIFE

1. Plastic you put in the bin ends up in landfill. When rubbish is being transported to landfill, plastic is often blown away because it's so lightweight. From there, it can eventually clutter around drains and enter rivers and the sea this way.

2. Fish, seabirds, sea turtles, and marine mammals can become entangled in 	or ingest plastic debris, causing suffocation, starvation, and drowning.

3. Plastic ending up on landfills. The vast majority—79 percent—is accumulating in landfills or sloughing off in the natural environment as litter. Meaning: at some point, much of it ends up in the oceans, the final sink.

4. The majority of pollutants that make their way into the ocean come from human activities along the coastlines and far inland. One of the biggest sources of pollution is nonpoint source pollution, which occurs as a result of runoff.

5. Rising (or even falling) water temperatures can stress coral polyps, causing them to lose algae (or zooxanthellae) that live in the polpys' tissues. This results in “coral bleaching,” so called because the algae give coral their color and when the algae “jump ship,” the coral turns completely white.

6. Many different groups of animals are at risk, including plankton, shrimps, lobsters, gastropods, bivalves, starfish, sea urchins and corals. In the worst case, many species may die out or be outcompeted by other species that are more resistant to acidification.

7. Most areas of the world's oceans are experiencing habitat loss. But coastal areas, with their closeness to human population centers, have suffered disproportionately and mainly from manmade stresses.

8. Mangrove swamps protect coastal areas from erosion, storm surge (especially during hurricanes), and tsunamis. The mangroves' massive root systems are efficient at dissipating wave energy.

9. Nutrient-rich fertilizer runoff and sewage effluent can boost algae growth, which starves the water of oxygen, causing eutrophication. Pollution from land, including hot water releases from power plants, pathogens, and trash, and from marine activities, such as fuel leaks and oil spills, also endangers coral reefs.

10. The cleanup is a great opportunity to beautify local common areas as well. This could be as simple as planting a few flowers, or fixing up a damaged sign or sidewalk. It is amazing how just a few minor changes can improve the look and feel of a community.

FOREST DEGRADATION

1. According to a new study in the journal Nature, soot may be the second biggest contributor to global warming -- just behind the infamous greenhouse gas, carbon dioxide c (CO2). ... A reduction in worldwide soot emissions, he maintains, could prove beneficial in slowing down the disastrous pace of global warming.

2. Deforestation can positively impact the economy in many ways because of the resources it produces. Tourism is many of the rainforest countries main source of economic income. ... So not only is deforestation ruining the habitat of many plants and animals, but it is also ruining the economy.

3. The natural world contains about 8.7 million species, according to a new estimate described by scientists as the most accurate ever. But the vast majority have not been identified - and cataloguing them all could take more than 1,000 years.

4. Tropical rainforests contain more biodiversity than any other ecosystem on Earth. they cover less than two percent of the Earth's total surface area, and are home to 50 percent of the Earth's described plants and animals!

5. Plant a trees, Use less paper, Recycle paper and cardboard,Use recycled products, Buy only sustainable wood products, Don't buy products containing palm oil, Reduce meat consumption, Do not burn firewood excessively.

6. The Holocene extinction, otherwise referred to as the sixth mass extinction or Anthropocene extinction, is an ongoing extinction event of species during the present Holocene epoch (with the more recent time sometimes called Anthropocene) as a result of human activity.

7. A mature leafy tree produces as much oxygen in a season as 10 people inhale in a year." "A 100-foot tree, 18 inches diameter at its base, produces 6,000 pounds of oxygen." "On average, one tree produces nearly 260 pounds of oxygen each year. Two mature trees can provide enough oxygen for a family of four.

8. Forests cover 31 percent of the Earth's land to be exact.

9. Important direct drivers affecting biodiversity are habitat change, climate change, invasive species, overexploitation, and pollution (CF4, C3, C4. 3, S7).

10. Trees produce oxygen and clean carbon dioxide out of the air we breathe. Without trees, life could not continue. Trees have also proved to remove airborne particles from the air and reduce smog, thereby improving the air we breathe, and therefore, our respiratory health.


DISASTER PREPARATION

1. Secure heavy furniture, hanging plants, heavy pictures or mirrors. Keep flammable or hazardous liquids in cabinets or on lower shelves. Maintain emergency food, water and other supplies, including a flashlight, a portable battery-operated radio, extra batteries, medicines, first aid kit and clothing.

2. Think out your plan of action first, then move. Know exit routes if in a commercial building. Take cover and don't move until the shaking stops. If outside, get into an open area away from trees, buildings, walls and power lines.


3. Build an emergency kit and make a family communications plan.

4. Depending on the type of flooding: Evacuate if told to do so.

5. If you have to walk in water, walk where the water is not moving. Use a stick to check the firmness of the ground in front of you. Do not drive into flooded areas. If flood waters rise around your car, abandon the car and move to higher ground if you can do so safely.

6. Review your family preparedness plan. Establish a family communications plan. Assemble a disaster supply kit. Have a family evacuation plan in place.

7. Follow evacuation or shelter orders.

8. Flashlight, Batteries, Water, Canned foods, and radio are essentials to bring in case of emergency.

9. Include food and water for everyone in your household. 

10. Call 911 for every life-threatening emergencies.




                        GAME INSTRUCTIONS

> Press SPACE BAR to fire.

> Press UP ARROW KEY to move up. 

>Press DOWN ARROW KEY to move down. 

>Press RIGHT ARROW KEY to move right. 

>Press LEFT ARROW KEY to move left.


""") 
  
# Making the text read only 
text_area.configure(state ='disabled') 
win.mainloop()