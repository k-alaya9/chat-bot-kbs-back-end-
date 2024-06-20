package khaled.alaya.jwt_demo.config;
import java.security.interfaces.RSAPublicKey;
import java.security.interfaces.RSAPrivateKey;

import org.springframework.boot.context.properties.ConfigurationProperties;

@ConfigurationProperties(prefix = "rsa")
public record RSAkeyproprties(RSAPublicKey publicKey,RSAPrivateKey privateKey) {

}
