package khaled.alaya.jwt_demo.repo;

import java.util.Optional;

import org.springframework.data.jpa.repository.EntityGraph;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import khaled.alaya.jwt_demo.model.chat;
import khaled.alaya.jwt_demo.model.user;

import java.util.List;

@Repository
public interface chatRepo extends CrudRepository<chat,Long>{

    @Query("SELECT c FROM chat c JOIN c.user_id u WHERE u.id = :userId")
    List<chat> findChatsByUserId(@Param("userId") Long userId);
}
