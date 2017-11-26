#include <Arduino.h>
#include <dht11.h>

dht11 DHT11;

#define SLEEP 60000
#define BOUD_RATE 115200

#define AIR_TEMPERATURE_AND_HUMIDITY 2
#define WATER_TEMPERATURE 3
#define POWER_K1 4
#define POWER_K2 5
#define POWER_K3 6
#define POWER_K4 7
#define LUMINOSITY A0

typedef struct response_t {
    float temperature;
    float humidity;
    float luminosity;
    bool power_k1;
    bool power_k2;
    bool power_k3;
    bool power_k4;
} response;

void JSONResponse(response data) {
    Serial.print("{");

    Serial.print("\"air_humidity\":");
    Serial.print(data.humidity, 2);
    Serial.print(", ");

    Serial.print("\"air_temperature\":");
    Serial.print(data.temperature, 2);
    Serial.print(", ");

    Serial.print("\"luminosity\":");
    Serial.print(data.luminosity, 2);
    Serial.print(", ");

    Serial.print("\"power_k1\":");
    Serial.print(data.power_k1, 2);
    Serial.print(", ");

    Serial.print("\"power_k2\":");
    Serial.print(data.power_k2, 2);
    Serial.print(", ");

    Serial.print("\"power_k3\":");
    Serial.print(data.power_k3, 2);
    Serial.print(", ");
    Serial.print("\"power_k4\":");
    Serial.print(data.power_k4, 2);

    Serial.println("}");
}

response sensor_data() {
    response data;

    if (DHT11.read(AIR_TEMPERATURE_AND_HUMIDITY) != DHTLIB_OK) {
        Serial.println("{\"error\": \"DHT11 Sensor Error\"}");
    }

    data.humidity = (float) DHT11.humidity;
    data.temperature = (float) DHT11.temperature;
    data.luminosity = (float) analogRead(LUMINOSITY);
    data.power_k1 = (bool) digitalRead(POWER_K1);
    data.power_k2 = (bool) digitalRead(POWER_K2);
    data.power_k3 = (bool) digitalRead(POWER_K3);
    data.power_k4 = (bool) digitalRead(POWER_K4);

    return data;
}

void setup() {
    Serial.begin(BOUD_RATE);
    pinMode(POWER_K1, OUTPUT);
    pinMode(POWER_K2, OUTPUT);
    pinMode(POWER_K3, OUTPUT);
    pinMode(POWER_K4, OUTPUT);
}

void loop() {
    response data = sensor_data();
    JSONResponse(data);
    delay(SLEEP);
}
