package khaled.alaya.jwt_demo.controller;

import java.util.Collections;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import khaled.alaya.jwt_demo.model.LoginRequest;
import khaled.alaya.jwt_demo.model.RegisterRequest;
import khaled.alaya.jwt_demo.model.user;
import khaled.alaya.jwt_demo.service.TokenService;
import khaled.alaya.jwt_demo.service.userService;

@RequestMapping("/api/auth")
@RestController
public class authController {

    private AuthenticationManager authManager;
    private TokenService tokenService;
    @Autowired
    PasswordEncoder passwordEncoder;
    private userService userService;

    public authController(AuthenticationManager authManager, TokenService tokenService,BCryptPasswordEncoder passwordEncoder,userService userService) {
        this.authManager = authManager;
        this.tokenService = tokenService;
        this.passwordEncoder=passwordEncoder;
        this.userService=userService;
    }


    @PostMapping("/login")
    public ResponseEntity<Map<String, String>> token(@RequestBody LoginRequest user){
        UsernamePasswordAuthenticationToken authRequest = new UsernamePasswordAuthenticationToken(user.username(), user.password());
        System.out.println("Auth request: " + authRequest);
        
        try {
            Authentication authentication = authManager.authenticate(authRequest);
            System.out.println("Authentication result: " + authentication);
            
            if (authentication.isAuthenticated()) {
                System.out.println("Authenticated!");
                String token = tokenService.generateToken(authentication);
                System.out.println("Token: " + token);
                return ResponseEntity.ok().body(Collections.singletonMap("token", token));
            } else {
                System.out.println("Authentication failed!");
                return ResponseEntity.internalServerError().body(Collections.singletonMap("ERROR:","Authentication failed!"));
            }
        } catch (Exception e) {
            System.out.println("Authentication exception: " + e.getMessage());
          return ResponseEntity.badRequest().body(Collections.singletonMap("ERROR:",e.getMessage()));
        }
    }

    @PostMapping("/register")
    public ResponseEntity<Map<String, String>> register(@RequestBody RegisterRequest user){
        try{
       user newUser= userService.newUser(user);
       Authentication authentication=authManager.authenticate(new UsernamePasswordAuthenticationToken(newUser.getName(),user.password()));
       System.out.println(authentication.getCredentials());
        String token = tokenService.generateToken(authentication);
        System.out.println(token);
      return ResponseEntity.ok().body(Collections.singletonMap("token", token));}
    catch(Exception e){
        System.out.println("Authentication exception: " + e.getMessage());
        return ResponseEntity.badRequest().body(Collections.singletonMap("ERROR:",e.getMessage()));
    }
    }

    @DeleteMapping("/logout")
    public ResponseEntity<Map<String, String>> logout() {
        return ResponseEntity.ok().body(Collections.singletonMap("message", "logged out"));
        }
}
