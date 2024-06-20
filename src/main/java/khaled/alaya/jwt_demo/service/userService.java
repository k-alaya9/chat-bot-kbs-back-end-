package khaled.alaya.jwt_demo.service;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import khaled.alaya.jwt_demo.model.RegisterRequest;
import khaled.alaya.jwt_demo.model.user;
import khaled.alaya.jwt_demo.repo.userRepo;

@Service
public class userService {
    @Autowired BCryptPasswordEncoder passwordEncoder;

     private userRepo userRepo;

    public userService(khaled.alaya.jwt_demo.repo.userRepo userRepo) {
        this.userRepo = userRepo;
    }

    public user newUser(RegisterRequest user){
        user newUser= new user(user.username(),user.email(),passwordEncoder.encode(user.password()));
        System.out.println(newUser);
        return userRepo.save(newUser);
    }

    public Optional<user> getUser(user user){
        return userRepo.findById(user.getId());
    }
}
