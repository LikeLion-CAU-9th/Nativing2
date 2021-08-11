Nativing
=======================

 <div class="stack">
   <a href="#"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=JavaScript&logoColor=black"/></a>
  <a href="#"><img src="https://img.shields.io/badge/CSS-1572B6?style=flat&logo=CSS3&logoColor=white"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Html-61DAFB?style=flat&logo=Html&logoColor=white"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Django-339933?style=flat&logo=Django&logoColor=white"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3766AB?style=flat&logo=Python&logoColor=white"/></a>
   </div>

Hello, we are a web service made for people who want to learn Korean.

It's been distributed, so please watch it a lot.


Requirements
============

* PHP >= 5.3.7
* cURL Extension

Installation
============

    composer require buonzz/laravel-4-freegeoip:dev-master

Add the service provider and facade in your config/app.php

Service Provider

    Buonzz\GeoIP\Laravel4\ServiceProviders\GeoIPServiceProvider

Facade

    'GeoIP'            => 'Buonzz\GeoIP\Laravel4\Facades\GeoIP',


Usage
=====

Get country of the visitor

    GeoIP::getCountry();  // returns "United States"
    
Get country code of the visitor

    GeoIP::getCountryCode();  // returns "US"

Get region of the visitor


Credits
=======

* Alexandre Fiori for the awesome http://freegeoip.net web api
* MaxMind for the data
