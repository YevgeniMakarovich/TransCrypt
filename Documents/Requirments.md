# **Project requirements**

## **1. Introduction**

Nowadays, cryptocurrency is the most progressive tool for online money transactions. Cryptocurrency provides you with anonymity and gives you an opportunity of tracking your "digital money" on it's way from deliver to receiver. 
Cryptocurrency uses cryptography to secure the transactions and to control the creation of additional units, so, the main task of this project is to make choosing of cryptocurrency for mining more convenient and apprehensible.
This application will be used for:
* controlling actual rate of ETH Ethereum, ETC Ethereum Classic and ZEC ZeroCash
* receiving information about currency per hour mining based on model of GPU
* transferring cryptocurrency to US dollar.  


## **2. User requirements**

**2.1 User interface**

![interface](https://github.com/YevgeniMakarovich/TransCrypt/blob/master/Images/Mockups/Mockup.jpg "Interface")

**2.3 User characteristics**

The target audience - people of all ages, who want to start cryptocurrency mining or to keep in touch with latest rates.

**2.4 Assumptions and dependencies**

Without internet connection application won't be able to refresh rates and make transfering without it. Also, there are a lot of differences of cryptocurrencies and GPUs, so, this application can not provides you with a great choice of cryptocurrencies, but amount of supported cryptocurrencies and GPU's will become wider in next updates.


## **3. System requirements**

1. Windows 7/8/10
2. MSBuild 15.0
3. .NET Framework 4.5.1



**3.1 Functional requirements**

1. When choosing a crypto currency, the current rate of this cryptocurrency relative to USD must be displayed in the correspondent field.
2. When choosing a cryptocurrency, its rate for yesterday must be displayed in the corresponding field.
3. The ability to choose models of GPUs.
4. The ability to choose amount of connected devices.
5. When choosing a crypto currency and GPUs, the amount of received crypto currency per hour and the value of this amount of crypto currency in USD must be displayed in the corresponding field.

**3.2 Non-functional requirements**

Completeness of provided information - all rates will be updated after every single launch. GPU’s characteristics are static and already published.
