package khaled.alaya.jwt_demo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.EnableConfigurationProperties;

import khaled.alaya.jwt_demo.config.RSAkeyproprties;

@EnableConfigurationProperties(RSAkeyproprties.class)
@SpringBootApplication
public class JwtDemoApplication {

	public static void main(String[] args) {
		
		SpringApplication.run(JwtDemoApplication.class, args);
	
	}
}
