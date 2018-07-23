![N|Solid](https://raw.githubusercontent.com/GPortas/Playgroundb/master/doc/logo.png)
#
Playgroundb is a database management learning platform that allows students to learn by solving competitive challenges created by their teachers.

The platform allows students to practise and solve exercises on a web environment with completely preconfigured databases, so they do not need to install any kind of software on their computers.

Teachers create exercises and insert test data for their resolution through exclusive access configuration panels on the web.

The students solve the exercises in an exclusive section designed for them, where they have a command line to execute queries. Students gain points when they solve an exercise. The number of points to obtain depends on different factors: time to solve it, number of dedicated attempts and difficulty of the exercise (determined by the total time allocated to its resolution).

The users with the highest score appear in a ranking within the platform. This provides a competitive factor for students to have fun while they learn by solving exercises.

The main goal of the project is to develop an MVP (Minimum viable product) of the platform with the functionalities previously described. This MVP has to be prepared to be deployed in a real production environment.

To fulfill the described goal, an important work has been done to design an architecture according to the desired solution. This architecture has different modules developed in different technologies and independent of each other. Each module has its own development and architecture and together they ultimately constitute the overall architecture of the system.

For the development of the different modules, the important part of DevOps and test coverage has been taken into account, in order to facilitate the development work and the updating of the platform code.

Docker has been used in each of the modules present in the system, using for the construction of containers customized images to meet the needs of each one.
#
### Overall architecture

![N|Solid](https://raw.githubusercontent.com/GPortas/Playgroundb/master/doc/diagram1.png)

### API architecture

![N|Solid](https://raw.githubusercontent.com/GPortas/Playgroundb/master/doc/diagram2.png)

## Authors

* **Guillermo Portas** - [GPortas](https://github.com/gportas)

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE.md](https://github.com/GPortas/Playgroundb/blob/master/LICENSE) file for details
