<p align="center">
    <img src="https://p86.f2.n0.cdn.getcloudapp.com/items/6quLGkxx/Image+2020-01-12+at+7.54.25+AM.png?v=fbbc7c9b8d066340031b41993ff776d3" alt="tlm" width=300 height=300>
  <p align="center">
    Automatically scale to handle burst loads during peak hours, or scale down when not in use.
  </p>
</p>
<br>

# Transaction Load Manager (TLM)

Transaction Load Manager (TLM) is an application to allow a multitude of transactions to happen in parallel rather than reverting to a queue structure where one must be completed in order for the next to begin. This reduces the workload of the program while creating a faster experience without compromising efficiency. Instead of having all transactions file through one container, there are several containers that transactions can go through and this quantity scales automatically based on need as not to waste resources thereby reducing cost. A user can choose a number of transactions that simulates the number of requests over a given time period. This simulation is displayed through a dashboard providing valuable information about transactions as well as a graph that computes the TLM.

### Prerequisites

Requires [NodeJS](https://www.npmjs.com/get-npm) installation.
Check that Node has installed

```
node -v
```

Check that npm has installed

```
npm -v
```

### Running

Go into the `\Scripts` directory of the project and run:

```
npm install
```

to install all the dependencies for the project.
Then run the project on localhost:

```
npm run dev
```


## Built With

* [Vue.js](https://vuejs.org/) - The web framework used
* [AWS ECS](https://aws.amazon.com/ecs/) - Container Manager
* [Docker](https://www.docker.com/) - Containerization Technology
* [Python3](https://www.python.org/download/releases/3.0/) - Backend Scripting



