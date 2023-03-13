package com.example.realestatemanager;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@EnableScheduling
@SpringBootApplication
public class RealEstateManagerApplication {

    public static void main(String[] args) {
        SpringApplication.run(RealEstateManagerApplication.class, args);
    }

}
