**1. Actors**
User - a person, who use application.

Internet resource - web-site, which provides application with information.

**2. Use cases**

**2.1. Choosing of cryptocurrency** 

**Description.** "Choosing of cryptocurrency" use case allows to choose one of available cryptocurrencies. 

**Main thread.** User press on a button with neccesary cryptocurrency.

**Postdescription.** "Choosing of cryptocurrency" use case let us activate "Checking rates" and "Conversion" use cases.


**2.2. Choosing of GPUs**

**Description.** "Choosing of GPU" use case allows to choose available GPUs. 

**Main thread.** 

1. User presses on a button with neccesary GPUs.
2. User chooses amount of GPUs.

**Postdescription.** "Choosing of GPU" use case let us activate "Conversion" use cases.


**2.3. Checking rates**

**Description.** "Checking rates" use case gives opportunity to check lates cryptocurrency's rates.

**Precondition.** User chooses cryptocurrency.

**Main thread.**
1. The use case starts when user chooses a necessary cryptocurrency.
2. An application takes information from a web-site and displays it.

**2.4. Conversion**

**Description.** "Conversion" use case converts cryptocurrency in USD and displays amount of cryptocurrency which will be mined per hour.

**Precondition.** User chooses cryptocurrency and GPU's.

**Main thread.**

1. Application calculates amount of cryptocurrency which will be mined per hour.
2. Application converts cryptocurrency in USD.
3. Results of previous actions are displayed on a screen. 
 
