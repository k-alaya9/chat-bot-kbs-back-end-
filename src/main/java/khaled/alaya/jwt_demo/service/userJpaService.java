package khaled.alaya.jwt_demo.service;

import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import khaled.alaya.jwt_demo.model.userSecurity;
import khaled.alaya.jwt_demo.repo.userRepo;

@Service
public class userJpaService implements UserDetailsService{

    private userRepo userRepo;

    public userJpaService(khaled.alaya.jwt_demo.repo.userRepo userRepo) {
        this.userRepo = userRepo;
    }

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        return userRepo.findByusername(username).map(userSecurity::new).orElseThrow(()->new UsernameNotFoundException("User not found with username:"+username));
    }


}
