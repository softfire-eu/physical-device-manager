  <img src="https://www.softfire.eu/wp-content/uploads/SoftFIRE_Logo_Fireball-300x300.png" width="250"/>

  Copyright © 2016-2018 [SoftFIRE](https://www.softfire.eu/) and [TU Berlin](http://www.av.tu-berlin.de/next_generation_networks/).
  Licensed under [Apache v2 License](http://www.apache.org/licenses/LICENSE-2.0).

# Physical Device Manager
The SoftFIRE Physical Device Manager provides reservation of physical resources. For the third wave, experimenters may reserve UE(s) at the Surrey test bed, and remotely control them using TeamViewer.
The figure below depicts the physical resource reservation process.

![](http://docs.softfire.eu/img/ue-reservation-engine.svg)

For more information on how to use the physical resources visit the [documentation](http://docs.softfire.eu/pd-manager).



## Technical Requirements

The Physical Device Manager requires Python 3.5 or higher.

## Installation and configuration

You can install the Physical Device Manager using pip:

```
pip install physical-device-manager
```

and then start it with the `physical-device-manager` command.

Or you can run it from source code by cloning the git repository, installing the dependencies as specified in the [setup.py](https://github.com/softfire-eu/physical-device-manager/blob/master/setup.py) file and executing the _physical-device-manager_ script.

The Physical Device Manager needs a configuration file present at _/etc/softfire/physical-device-manager.ini_. An example of the configuration file can be found [here](https://github.com/softfire-eu/physical-device-manager/blob/master/etc/physical-device-manager.ini).

## Issue tracker

Issues and bug reports should be posted to the GitHub Issue Tracker of this project.

# What is SoftFIRE?

SoftFIRE provides a set of technologies for building a federated experimental platform aimed at the construction and experimentation of services and functionalities built on top of NFV and SDN technologies.
The platform is a loose federation of already existing testbed owned and operated by distinct organizations for purposes of research and development.

SoftFIRE has three main objectives: supporting interoperability, programming and security of the federated testbed.
Supporting the programmability of the platform is then a major goal and it is the focus of the SoftFIRE’s Second Open Call.

## Licensing and distribution
Copyright © [2016-2018] SoftFIRE project

Licensed under the Apache License, Version 2.0 (the "License");

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

