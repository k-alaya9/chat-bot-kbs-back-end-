package khaled.alaya.jwt_demo.repo;

import java.util.Optional;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import khaled.alaya.jwt_demo.model.user;


@Repository
public interface userRepo extends CrudRepository<user,Long>{

 Optional<user> findByusername(String username);
}
