package khaled.alaya.jwt_demo.service;

import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.stream.Collectors;

import org.springframework.security.core.Authentication;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.oauth2.jwt.JwtClaimsSet;
import org.springframework.security.oauth2.jwt.JwtEncoder;
import org.springframework.security.oauth2.jwt.JwtEncoderParameters;
import org.springframework.stereotype.Service;
@Service
public class TokenService {

    private JwtEncoder encoder;

    public TokenService(JwtEncoder encoder) {
        this.encoder = encoder;
    }

    public String generateToken(Authentication authentication){
    Instant instant=Instant.now();
    System.out.println(authentication.getName());
    String scope= authentication.getAuthorities().stream()
    .map(GrantedAuthority::getAuthority).findFirst().get();
    JwtClaimsSet claims=JwtClaimsSet.builder()
    .issuer("self")
    .issuedAt(instant)
    .expiresAt(instant.plus(1,ChronoUnit.HOURS))
    .subject(authentication.getName())
    .claim("scope", scope)
    .build();
    return this.encoder.encode(JwtEncoderParameters.from(claims)).getTokenValue();
    }

}

