# ProGenGalaxy

Solar System Generator

This Project serves as an artifical solar system generator, which will stochasdtically generate stars, and their associated planets based off of real life observations
in main stell ar sequence, light physics, planetary motion and orbiotal mechanics. In its current verrsion this model makes some generalizations including genrating some stellar and planetary parametrers from rng's instead of using the mathamtical relationships that exist betwen these parameters. This will hopefully change as time goes on, with more and more astrophysics equations being implemented into the model. At the time of writing the text bellow ~ 4 years ago I was an inexperienced python
programmer. I now have the experince to say that this project will and should continue in python with pyside2 as the main gui. I should be able to implement all of the below  in native python. I may someday down the road move it to a rest api on a webserver, however for now making a native desktop application in Pyside2 should suffice fof what i am interested in. 

Near Future Additions
    Moon Generation
    Proper Planetary Movement Around the Star (Necessary for Graphics update)
    Surface Generation
        Generated Surface Features - For SImulated Environments
    


List of Anticipated features
1.GUI application 
2. Full planetary simulation
3. Ability to use Any planet as a jumping off point for FlowerSimulation
4. Model/View Framework to save states, export data, and maintain code sepperations from GUI and Model.
5. More rigorous scientific modelling parameters.

This project originated as an idea to generate a solar system procedurally so that each planet could be used as a base for other simulations, dnd games etc. 
When this project was created I did not have a very good grawsp on math, nor did I have a good grasp of gui programming. Originally this was intened to have a gui
interface however, GUI programming in python is incredibly difficult. There are poor libraries for GUI software in python, particularily for graphics. I can easily
create a GUI that consists of buttons and lists, but its as soon as visualization comes in it gets incredibly difficult. Thus I have decided to make some changes, that
I believe will not only benefit me as the developer but also the app in general. 


1. Move the GUI to a web based service. While many people would not like this at all, most if not all of the 
current software that people are using nowadays is based on the web. Sure there are applications where having a dedicated desktop app is useful, like being on a 
research vessel, working remotely without internet, working on the moon etc. These use cases are not very practical for the types of applicatoins that I wish to 
develop in the coming years, which consist of applications where many different people can take advantage of the services that are being provided by the 
applicaiton/script. Thus a server/client based web app, or full stack web app, is the best solution. This will allow me to deploy the application to a server, make a 
backend database and api. At its core that is all this application needs to do, serve data to a variety of people, or privately to me/my friends if I so choose. As I 
have always like gui programming, I would also like to make a front end app as well. This includes an interface to the database of stars, planets, moons etc. This also
includes a way to visualize how each of these Solar systems are laid out. This could be done simply, with stock photos of gas giants, m type stars, habitable planets
etc and then display the unique stats of each plantet. This would be simpler however not very visually appealing. A better option would be to use the planets generated
information to influence the design of each of the plantes in the display. It could be simple like color, size, and orbital period around the sun. This second option
is far more challenging, however it is much more useful/appealing. 


2. Web based service architecture:
	The desire to move to a web based application will give me, the developer, a good project to add to my python, javascript, SQL and API programming skills. All 
  valuable skills in the marketplace. 
  
  
	
	the architecture would be somthing simple.
	
	Flask Web App serving SolarSystemGenerator JSON data through a REST API
	REST API will serve this data from a SQL database
	Front end Javascript app to make API requests, display the data
	
3. Skills Necessary before this project can begin:
	HTML/CSS
	Javascript -> Udemy Class
	Flask -> Free Online Tutorials
	SQP -> Free Online Tutorials
	Python Practice -> Im an experienced python programmer, however I need some practice beore I jump back in again
	
	
