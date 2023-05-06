#include <Adafruit_Sensor.h>

#include "DHT.h"
#include <DHT_U.h>

//#include <Adafruit_CircuitPlayground.h>
//#include <Adafruit_Circuit_Playground.h>

/*
    This sketch sends a string to a TCP server, and prints a one-line response.
    You must run a TCP server in your local network.
    For example, on Linux you can use this command: nc -v -l 3000
*/

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>



//#define DHTTYPE DHT11   // DHT 11
#ifndef STASSID
#define STASSID "Hima_Ext"
#define STAPSK  "RANA@1973"
#endif
#define aref_voltage 3.3 

//#define DHTPin D4//this is were our output data goes

const char* ssid     = STASSID;
const char* password = STAPSK;

const char* host = "192.168.0.44";
const uint16_t port = 1883;
DHT dht(D4, DHT11);   ///
float Temperature; //////
float Humidity;   /////
  WiFiClient client;

ESP8266WiFiMulti WiFiMulti;

void setup() {
  Serial.begin(115200);
  // If you want to set the aref to something other than 5v
  analogReference(EXTERNAL);
  dht.begin();   

  // We start by connecting to a WiFi network
  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP(ssid, password);

  Serial.println();
  Serial.println();
  Serial.print("Wait for WiFi... ");

  while (WiFiMulti.run() != WL_CONNECTED) {
    Serial.println("still not connected");
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  delay(500);
  // Use WiFiClient class to create TCP connections


  while (!client.connect(host, port)) {
    Serial.println("connection failed");
    Serial.println("wait 5 sec...");
    delay(5000);
    return;
    
  }


}


void loop() {
  Serial.print("connecting to ");
  Serial.print(host);
  Serial.print(':');
  Serial.println(port);

  

 Temperature = dht.readTemperature(); // Gets the values of the temperature
 delay(1000);
  Humidity = dht.readHumidity(); // Gets the values of the humidity 

 Serial.print(Temperature);
 
 //testing to see the results  on the serial
 Serial.print("The Temperature is : \n");
 Serial.println(Temperature,1);
 Serial.print("The Humidity is : \n");
 Serial.println(Humidity,1);

 
  // This will send the request to the server
  client.println("2. The Temperature is :"+String(Temperature));
  String line = client.readStringUntil('\r');
  client.println("2. The Humidity is :"+String(Humidity));
   line = client.readStringUntil('\r');
  

  //read back one line from server
  Serial.println("receiving from remote server");
  //client.println("receiving from remote server");
   line = client.readStringUntil('\r');
  Serial.println(line);

  //Serial.println("closing connection");
  //client.stop();

  Serial.println("wait 5 sec...");
  delay(8000);
}

