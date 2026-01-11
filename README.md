# SDN-Based Honeypot
---
This project is part of the "Next Generation Network" course. It implements a security honeypot using SDN over a Kathará network that emulates a company environment, consisting of a server exposing HTTP services, a honeypot, and hosts representing both authorized and unauthorized users. The SDN controller identifies untrusted access requests and, instead of blocking the IP, redirects them to the honeypot. The controller manages IPs in such a way that the malicious host is unaware of the redirection.

## Project description
TODO
---

## Repository Structure

```bash
main
├── build.sh
├── Dockerfiles
│   ├── Dockerfile.host
│   ├── Dockerfile.ryu
│   └── Dockerfile.server
├── Kathara
│   ├── controller.shutdown
│   ├── controller.startup
│   ├── h1.startup
│   ├── h2.startup
│   ├── honeypot.startup
│   ├── lab.conf
│   ├── s1.startup
│   ├── server.startup
│   └── shared
│       ├── controllerSDN
│       │   ├── controller.py
│       │   ├── customLogger.py
│       │   └── NETCONFIG.py      
│       └── scripts
│           └── init.sh
├── LICENSE
├── README.md
└── Services
    ├── HttpController
    │   ├── app.py
    │   ├── static
    │   └── templates
    ├── HttpHpot
    │   ├── app.py
    │   └── templates
    └── HttpServer
        ├── app.py
        └── templates
```

- `/Dockerfiles`: contains containers images for the controller, servers and hosts
- `/Kathara`: contains the Kathara's configuration files and che shared scripts
- `/Services`: containts the HTTP Services of each vitual machine
---

## Usage

### Requirements
- Kathara

### Project setup

1. Clone or download the repository the repository and navigate into it
```bash
git clone `<url>`
cd SDN-based_honeypot/
```

2. Launch the `build.sh` script in order to build the Docker images deployed in the lab
```bash
./build.sh
```

### Project launch

Navigate to the `Kathara` folder and start the lab.

```bash
cd Kathara/
kathara lstart
```
Kathara will automatically deploy the VMs three terminals will appear, one for Host1 (`h1`), one for Host2 (`h2`) and one for the Honeypoy.

Notice that kathara uses xTerm by default, I highly suggest to change the terminal emulator to a more confortable one. To launch Kathara with a custom terminal use the `--terminal-emu` flag fllowed by the <path to terminal> e.g.:

```bash
kathara lstart --terminal-emu /usr/bin/gnome-terminal
```

### The Lab

Open your browser and navigate to the `controller` dashboard by digiting the url `http://localhost:8080/dahsboard`. The web app for the controller shoudl appear. You can navigate through the three sections:

1. Home: contains the server and honeypot status
2. Console: propose the controller terminal
3. Devices: show the devices connected to the switch

You may notice that it's quite empty, that's beacause the SDN controller is not running. Go to the Home page and click on the green `Launch Controller` button.
Console and devices should start to populate and status should go on "on". Wait until the VMs are properly started.
