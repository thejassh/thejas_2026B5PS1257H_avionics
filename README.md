hii



Name: Thejas Shetty

ID: 2026B5PS1257H



link to task 2 on tinkercad: https://www.tinkercad.com/things/lJaKTK3Ut9Y-state-machine



At first I was overwhelmed on seeing the questions. I started the first task by reading a csv file and extracting its data while looking out for non integer headers. Then i searched which module is best for graphing data in python and one of the results was matplotlib which happened to be already installed on my computer. Then i searched for matplotlib functions and how to graph, and to account for errors my thought processs was



error-->deviation-->STANDARD? devation-->from what-->maybe mean-->there should be some limit to allowed deviation---> some sd's from mean-------------> within m sd's from mean of last n entered values--------> it would stop in the middle as there was too much deviation from the mean value which thus wouldn't update and every next value was outside this (now) fixed range and when sd is 0 re near 0 too pretty much everything got rejected---> i decided to make a limit to how many values can be rejected, which helped a bit, and only appended the coordinates accepted to the list too, and had to decide between adding something to m\*sd or replace it with max(some small but significant number within the acceptable error range, sd), chose the latter.



it may have been better to choose the median but this worked too.

different graphs for different m and n values, included m and n as parameters. when n=5 it's best to take m in the range of 5-10 as per my observation. smaller m will result in a smoother graph but more values rejected and potentially correct/useful information lost, bigger m will result in a graph with more of the given values included, but that means more errors too.



For the second task I was even more daunted than i was when i read the first, but then i got on tinkercad and made an account and it felt pretty much self explanatory with all the connection guides right there on the website, and if I didn't get something I could search about it, or well, tinker and find out! after having fun connecting all the wires, and changing the colors and everything, I realized I'm supposed to program the damn thing. Saw codeblocks, but I think I saw a message in the SEDS WhatsApp group saying not to use blocks (i lurk) so I searched arduino syntax and found out it's just like c (actually c or c++ idk the top of the code said c++) and coded what I thought it's be like by intuition. I then pressed the button expecting open sea but it instead gave me boom visual effect led may damage/have a reduced lifespan due to high voltage and fart noises. After debugging it a lot it finally worked, and the liquidcrystal header file and pulsein function made the job easier. I used the template circuits and connection guides provided in tinkercad for several of the components, and youtube videos including the ones shared in the problem/task file. I also asked gemini about some syntax and functions, especially for the specific lcd screen i'd used which I couldn't find on youtube for some reason, but didn't copy any logic/code, specifically told it not to give me any. This task might still have some errors.



I enjoyed doing these tasks a lot and the new stuff needed to do them was really really interesting, though it was tough(especially debugging) and I don't know how much of what I did is actually right, just tried to do it. 

Thanks for giving these problems! I really learnt a lot from them.

bye



PS: I'm sorry this wasn't exactly brief or informative enough about my logic

